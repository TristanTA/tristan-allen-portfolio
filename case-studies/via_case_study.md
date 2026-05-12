---
title: "Via Case Study"
permalink: /case-studies/via_case_study/
---

# VIA

Human-in-the-loop object detection workflow combining real-time vision models, label refinement, and structured evaluation.

## Problem

Real-time object detection systems often produce outputs that are technically plausible but operationally messy. Labels can be noisy, confidence thresholds can be poorly tuned, and downstream usefulness depends heavily on how the system handles ambiguity.

VIA explores how human feedback and refinement can improve the reliability of model-assisted perception workflows.

## System Built

VIA is a computer vision pipeline built around real-time detection and post-detection refinement. The system treats prediction quality as an iterative engineering problem rather than a one-time model choice.

## Stack and Architecture

- YOLO-based detection pipeline
- Real-time inference workflow
- Refinement stage for ambiguous or weak labels
- Human correction loop for higher quality outputs
- Structured evaluation through error analysis and threshold tuning

## Constraints

- Real-time latency requirements
- Limited training data
- Risk of poor labels propagating through the workflow
- Need to balance automation quality with manual correction effort

## What Works Today

- Detection pipeline architecture
- Evaluation framing around precision, recall, and false positives
- Human-in-the-loop improvement workflow
- Stronger engineering understanding of where model outputs break down

## Evidence and Current Status

VIA is an active prototype. I am not presenting benchmark numbers here because the current value of the project is in the architecture, the evaluation workflow, and the refinement loop rather than a finalized production-grade model result.

That said, it is an important project for showing that I am comfortable with applied ML work that includes model behavior, dataset limitations, and iterative improvement rather than only interface-level AI features.

## Why It Matters

VIA is the clearest classical ML project in the portfolio. It shows how I think about prediction systems in a disciplined way: model output quality, failure analysis, human feedback, and the engineering steps needed to improve reliability over time.

## Next Engineering Milestone

- Expand the curated dataset for cleaner evaluation
- Tighten refinement logic for ambiguous detections
- Compare threshold and model configuration choices more systematically
