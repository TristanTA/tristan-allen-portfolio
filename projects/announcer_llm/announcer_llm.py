from typing import Dict, List
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import time

class AnnouncerLLM:
    def __init__(self, model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0", temperature=0.8, system_style="excited", context=""):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)
        self.system_prompt = self._build_system_prompt(system_style)
        self.context = context
        try:
            with open("initial_context.txt", "r", encoding="utf-8") as f:
                self.initial_context = f.read().strip()
        except FileNotFoundError:
            self.initial_context = ""
            print("Warning: initial_context.txt not found. Proceeding without it.")

    def _build_system_prompt(self, style: str) -> str:
        print("Building Prompt...")
        base = "You are a professional baseball announcer. Respond with commentary that is applicable to current events and score changes. Include players names in your commentary."
        if style == "excited":
            return base + " Speak with enthusiasm and dramatic flair. React naturally to game events and use exciting phrasing. Be personable and engaging for the audience and teams."
        elif style == "calm":
            return base + " Keep your tone neutral and informative. Be clear and concise with minimal emotion. Do not include unnnessasary information."
        elif style == "stat-heavy":
            return base + " Include relevant stats in your commentary. Use a calm and analytical tone. Do not overload the audience, but mention the most applicable stats."
        else:
            return base

    def format_prompt(self, game_state: Dict) -> str:
        prompt = (
            f"Inning: {game_state['inning']} ({game_state['top_bottom']})\n"
            f"Outs: {game_state['outs']}\n"
            f"Count: {game_state['balls']}-{game_state['strikes']}\n"
            f"Bases: {', '.join(game_state['bases']) or 'Empty'}\n"
            f"Batter: {game_state['batter']}\n"
            f"Pitcher: {game_state['pitcher']}\n"
            f"Event: {game_state['event']}\n"
            f"Score: {game_state['score']['home_team']} {game_state['score']['home']}, "
            f"{game_state['score']['away_team']} {game_state['score']['away']}\n"
            f"Announcer Commentary:"
        )
        print("Prompt Complete.")
        return prompt

    def generate_commentary(self, context: str, event: str) -> str:
        print("Generating Commentary...")
        prompt = f"""{self.initial_context}

        Game Situation:
        {context}

        What just happened:
        {event}

        As the announcer, say one exciting sentence reacting to the new play:
        """

        start_time = time.time()

        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.device)
        output_ids = self.model.generate(
            input_ids,
            max_new_tokens=100,
            temperature=0.9,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            eos_token_id=self.tokenizer.eos_token_id,
        )
        output = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

        print("Generation Complete.")
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Response time: {elapsed:.2f} seconds")

        return output[len(prompt):].strip()


class GameMemory:
    def __init__(self, home_team: str, home_record : str, away_team: str, away_record: str, location: str):
        self.home_team = home_team
        self.home_record = home_record
        self.away_team = away_team
        self.away_record = away_record
        self.location = location
        self.events: List[str] = []
        self.score = {home_team: 0, away_team: 0}
        self.inning = 1
        self.top_bottom = "Top"

    def initialize_game(self, inning=1, top_bottom="Top"):
        self.inning = inning
        self.top_bottom = top_bottom
        self.events = []

    def update_score(self, team: str, runs: int):
        if team in self.score:
            self.score[team] += runs

    def add_event(self, event_description: str):
        self.events.append(event_description)

    def update_inning(self, inning: int, top_bottom: str):
        self.inning = inning
        self.top_bottom = top_bottom

    def generate_context(self) -> str:
        score_line = f"Current score: {self.away_team} {self.score[self.away_team]}, {self.home_team} {self.score[self.home_team]}"
        header = f"{self.away_team} vs. {self.home_team} at {self.location}. {score_line}. {self.top_bottom} of the {self.inning}."
        history = "\n- ".join(self.events[-3:])

        return f"{header}\nRecent notable events:\n- {history if history else 'No events yet.'}"
