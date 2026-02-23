---
layout: page
title: LifeNotes Case Study
---
**A Research-Driven Intelligent Learning Notebook**

---

## 1. Overview

### Problem

Most note-taking systems optimize for storage and organization rather than learning. Users capture information but rarely revisit it in cognitively effective ways. Notes become passive archives instead of active memory tools.

### Hypothesis

Integrating evidence-based learning mechanisms directly into a note workflow — specifically:

- Active Recall  
- Spaced Repetition  
- Interleaving  
- Retrieval-Based Testing  

— will significantly improve long-term retention and transfer compared to passive review.

LifeNotes is being built to test and implement this hypothesis.

---

## 2. Research Foundation

### 2.1 Active Recall (Retrieval Practice)

Core finding: Attempting to retrieve information strengthens memory more than re-reading.

Key research:
- Roediger & Karpicke (2006) – The testing effect  
- Karpicke & Blunt (2011) – Retrieval practice vs concept mapping  

**Design Implication**

Notes should generate retrieval prompts rather than simply display stored information.

Planned integration:
- Auto-generated quiz questions from notes  
- Prompt-first interface (question → reveal answer)  
- Weekly recall sessions  

---

### 2.2 Spaced Repetition

Core finding: Distributed practice produces stronger long-term retention than massed review.

Key research:
- Cepeda et al. (2006) – Spacing effect meta-analysis  
- Ebbinghaus – Forgetting curve  

**Design Implication**

Notes should resurface at adaptive intervals based on prior performance.

Planned integration:
- Adaptive resurfacing schedule  
- Retrieval-success-based interval growth  
- Lightweight decay model per note  

---

### 2.3 Interleaving

Core finding: Mixing related topics improves discrimination and transfer compared to blocked practice.

Key research:
- Rohrer & Taylor (2007)  
- Kornell & Bjork (2008)  

**Design Implication**

Weekly quizzes should mix topics rather than group by folder.

Planned integration:
- Cross-folder quiz generator  
- Topic diversity balancing  
- Avoid consecutive related prompts  

---

### 2.4 Desirable Difficulties

Core finding: Learning improves when difficulty is increased appropriately, even if learning feels harder.

Key research:
- Bjork (1994) – Desirable difficulties framework  

**Design Implication**

The system should delay answers, require effortful recall, and track confidence.

Planned integration:
- Delayed answer reveal  
- Confidence rating  
- Adaptive difficulty escalation  

---

## 3. Current System Status

LifeNotes is currently in early-stage development.

### What Exists

- Streamlit-based UI prototype  
- Note storage system  
- Basic organizational structure  
- Early semantic search experimentation  

### What Is Not Yet Implemented

- Offline-first architecture  
- Completed voice transcription pipeline  
- Audio playback system  
- FAISS semantic search integration  
- LLM-based classification  
- Spaced repetition engine  
- Retrieval quiz generation  
- Interleaving system  
- APK deployment  

The current version functions as a prototype note capture interface, not yet a full learning engine.

---

## 4. Learning Engine Design, Validation Plan, and Roadmap

### 4.1 Learning Engine Architecture (Planned)

#### Quiz Generator Pipeline

Input:
- Note content  
- Topic metadata  
- Prior retrieval performance  

Process:
- Extract core propositions  
- Convert into structured prompts:
  - Definition questions  
  - Short answer recall  
  - Application questions  

Output:
- Structured quiz objects (JSON-based schema)

---

#### Adaptive Spacing Model

Variables:
- Retrieval success  
- Confidence rating  
- Time since last retrieval  

Model:
- Exponential interval growth  
- Reset or shorten interval on failure  
- Lightweight per-note memory record  

Example schema:

```json
{
  "note_id": "123",
  "difficulty_score": 0.42,
  "success_rate": 0.78,
  "last_retrieved": "timestamp",
  "next_due": "timestamp"
}