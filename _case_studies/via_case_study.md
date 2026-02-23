---
title: "Via Case Study"
---
## Overview
VIA is a human-in-the-loop object detection and labeling system combining real-time computer vision with LLM-based refinement.

---

## Problem

Raw object detection systems produce noisy or context-agnostic outputs.

**Core Question:**  
How can human feedback improve model accuracy and contextual relevance?

---

## Constraints

- Real-time inference requirement
- GPU memory limitations
- Limited training data
- Model hallucination risk

---

## System Architecture

- YOLO detection pipeline
- Cropped image refinement stage
- LLM-based label enhancement
- Human correction feedback loop
- Dataset update mechanism

---

## Evaluation Strategy

- Precision/Recall tracking
- False positive analysis
- Confidence threshold tuning
- Comparative model performance

---

## Design Decisions & Tradeoffs

| Decision | Tradeoff | Rationale |
|----------|----------|-----------|
| Two-stage detection | Added latency | Higher classification accuracy |
| LLM refinement | Possible hallucination | Contextual enhancement |
| Active learning | Manual overhead | Continuous improvement |

---

## Results

- Baseline accuracy:
- Post-refinement accuracy:
- Average inference time:
- Observed improvement rate:

---

## Lessons Learned

- Confidence calibration importance
- Model bias patterns
- Feedback integration challenges

---

## Future Work

- Automated threshold optimization
- Larger curated dataset
- Cross-model benchmarking