---
title: "DataInsight Case Study"
permalink: /case-studies/datainsight_case_study/
---

# DataInsight

AI-powered data analysis platform built to help non-technical users move from raw business data to actionable insight through natural language, structured planning, and agentic analysis workflows.

## Problem

Most business datasets are only useful to people who already know how to clean them, inspect them, frame the right analytical questions, and interpret the results. That creates a gap between the people who need answers and the people who can reliably extract them.

DataInsight is built to close that gap by turning natural-language requests into guided data analysis workflows that can work through messy, imperfect real-world data.

## System Built

DataInsight is an applied AI platform for conversational analytics. Instead of treating analysis as a single prompt-response step, the system breaks the work into modular stages that can clean data, plan an analysis path, ask follow-up questions when needed, run statistical exploration, and return useful findings in a form non-technical users can act on.

## Stack and Architecture

- Python-based backend architecture
- FastAPI for API-driven orchestration
- Streamlit frontend for interactive user workflows and streaming responses
- OpenAI APIs for planning, reasoning, and response generation
- Modular processor architecture for cleaning, planning, analysis, and response generation
- Agent-based replanning flow when the first analysis path is incomplete or blocked

## Constraints

- Real-world datasets are messy, incomplete, and inconsistent
- Non-technical users need clarity without losing analytical rigor
- The system has to recover gracefully when data quality or user intent is unclear
- Analysis should be structured and inspectable rather than a black-box model response

## What Works Today

- Natural-language entry point for data analysis requests
- Automated preprocessing and cleaning workflow
- AI-generated planning before analysis execution
- Clarification loops when the request or dataset needs more context
- Modular architecture that can evolve toward richer multi-agent behavior

## Evidence and Current Status

DataInsight is a strong example of practical AI engineering beyond simple model calls. Planning, analysis, recovery, and user interaction work together as a single pipeline rather than as disconnected scripts.

It combines LLM orchestration, backend system design, user experience, and fault tolerance in one product-oriented system.

## Why It Matters

DataInsight demonstrates end-to-end AI/ML engineering that translates model capabilities into a usable product. It shows architecture thinking, modular backend design, agentic workflow design, and the ability to build around ambiguity instead of assuming perfect inputs.

It also reflects the kind of work I want to keep building: pipeline-style systems where models, tools, and user interaction cooperate reliably under real constraints.

## Next Engineering Milestone

- Expand the planning and replanning loop for more complex analytics tasks
- Improve robustness around imperfect schema and missing data
- Push the modular architecture further toward multi-agent analytics workflows
