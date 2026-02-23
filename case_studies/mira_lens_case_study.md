---
layout: page
title: Mira Lens Case Study
permalink: /mire_lens_case_study/
---
## Overview
Mira Lens is an offline-first AR/HUD prototype designed to enhance nature engagement through real-time object and audio recognition while minimizing cognitive intrusion.

---

## Problem

Nature-focused AR systems risk increasing attentional load and visual clutter.

**Core Question:**  
How can a wearable AR assistant provide real-time information without degrading situational awareness?

---

## Constraints

- Low-power hardware
- Offline-first requirement
- Real-time latency constraints
- Minimal UI real estate
- Outdoor lighting variability

---

## System Architecture

- Vision pipeline (YOLO-based object detection)
- Audio pipeline (BirdNET / sound classification)
- Local inference stack
- Lightweight UI overlay system

Diagram here (future addition)

---

## Human Factors Considerations

- Visual clutter reduction
- Peripheral awareness preservation
- Attention switching cost
- Information timing strategy
- Alert threshold tuning

---

## Design Decisions & Tradeoffs

| Decision | Tradeoff | Rationale |
|----------|----------|-----------|
| Minimal overlay UI | Less visible info | Reduced cognitive load |
| Offline inference | Limited model size | Privacy + reliability |
| Event-based notifications | Possible missed detections | Lower interruption rate |

---

## Evaluation

- Latency measurements
- Detection accuracy metrics
- Informal cognitive walkthrough
- Planned usability test (future)

---

## Results

- Avg detection latency:
- Model accuracy:
- Power usage impact:
- Key qualitative findings:

---

## Lessons Learned

- What worked
- What failed
- What surprised you

---

## Future Work

- Formal usability testing
- Cognitive load measurement
- Eye-tracking validation
- Hardware optimization