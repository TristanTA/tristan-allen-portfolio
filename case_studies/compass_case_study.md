---
title: "Compass Case Study"
permalink: /case-studies/compass_case_study/
---

**An Autonomous Portfolio Maintenance Agent**

---

## 1. Overview

### Problem

Maintaining a technical portfolio over time is difficult. Projects evolve, repositories change, documentation becomes outdated, and links silently break.  

Even well-maintained portfolios gradually accumulate:

- Broken repository links  
- Missing project updates  
- Outdated descriptions  
- Typos or formatting issues  
- New projects that never get added  

The result is a portfolio that no longer accurately reflects the current state of a developer's work.

### Hypothesis

A lightweight autonomous agent can continuously maintain a portfolio by:

- Periodically auditing the repository
- Detecting inconsistencies or missing updates
- Proposing improvements
- Automatically submitting pull requests

Compass was built to test this hypothesis.

---

## 2. System Concept

Compass is an **AI-powered portfolio maintenance agent** designed to act as a long-term caretaker for a GitHub portfolio repository.

Rather than manually reviewing the portfolio, the system:

1. **Audits the repository automatically**
2. **Identifies potential improvements**
3. **Creates a structured plan of changes**
4. **Requests approval**
5. **Submits pull requests implementing those improvements**

The goal is **continuous portfolio quality control** with minimal manual maintenance.

---

## 3. Current Role in This Portfolio

Compass currently manages the maintenance of **this portfolio website repository**.

Specifically, it performs automated audits of the portfolio repository:
tristan-allen-portfolio

These audits focus on improving:

- Portfolio professionalism
- Accuracy of project listings
- Documentation quality
- Case study updates
- Broken or outdated links
- Structural consistency

The agent periodically reviews files such as:

- project_list.md
- case_study_index.md
- case study pages
- README documentation
- portfolio configuration files

When Compass detects potential improvements, it produces a **change plan** and proposes updates via pull requests.

This turns the portfolio into a **self-maintaining system** rather than a static website.

---

## 4. System Architecture

Compass follows a simple agent workflow.

### Weekly Audit Pipeline

1. **Repository Scan**

The agent inspects the portfolio repository structure and key documentation files.

Typical checks include:

- Missing project entries
- Outdated case studies
- TODO markers
- inconsistent formatting
- broken links


2. **Change Proposal Generation**

The system produces a structured improvement plan containing:

- proposed file edits
- reasoning for each change
- expected impact

Example categories:

- Documentation improvement
- Portfolio completeness
- Professional tone improvements
- structural cleanup


3. **Human Approval**

Before implementing changes, Compass sends the plan to the portfolio owner for approval.

This prevents unwanted automated edits.


4. **Automated Pull Request**

Once approved, Compass:

- generates code changes
- commits updates
- opens a pull request to the portfolio repository

The portfolio owner can then review and merge the changes.

---

## 5. Key Design Principles

### Human-in-the-Loop Control

Compass does **not** modify the repository without approval.

All changes must be reviewed first.

This preserves control while still enabling automation.

---

### Minimal, High-Impact Changes

The agent is designed to avoid unnecessary edits.

It prioritizes:

- meaningful improvements
- clear fixes
- professional polish

rather than constant churn.

---

### Repository-Aware Reasoning

Compass reads the actual repository files before proposing changes.

This allows it to:

- understand project structure
- detect missing portfolio entries
- identify new repositories that should be added
- align edits with existing documentation

---

### Portfolio as a Living System

Rather than treating the portfolio as static documentation, Compass treats it as a **living system** that evolves alongside the developer's work.

---

## 6. Current System Status

Compass is currently operational in an **early autonomous maintenance phase**.

### What Exists

- Weekly audit system
- GitHub repository scanning
- automated change plan generation
- human approval step
- pull request generation pipeline
- integration with the portfolio repository

Compass is already capable of maintaining:

- project listings
- case study references
- repository link accuracy
- documentation clarity

---

### What Is Still Developing

Future improvements include:

- deeper repository analysis
- automated typo detection
- project discovery across all GitHub repos
- case study update detection
- documentation quality scoring
- multi-repository maintenance

The long-term vision is a **general portfolio management agent** capable of maintaining complex developer portfolios across many repositories.

---

## 7. Long-Term Vision

Compass represents an early prototype of a broader idea:

**AI systems that maintain and improve technical artifacts over time.**

Potential future capabilities include:

- automatically detecting new projects that belong in the portfolio
- recommending case study updates when code changes
- identifying missing documentation
- suggesting research write-ups for completed projects
- monitoring portfolio quality continuously

In the long term, Compass could evolve into a **general AI project curator** that maintains professional portfolios automatically.

---

## 8. Relationship to Other Projects

Compass is part of a broader ecosystem of AI tools designed to support development workflows.

Examples include:

- **LifeNotes** — an intelligent learning notebook system :contentReference[oaicite:0]{index=0}  
- **Alden** — an ambient AI assistant
- **MIRA** — a modular residential AI agent system

Within this ecosystem, Compass fills a specific role:

**maintaining the public representation of projects as they evolve.**

---

## 9. Takeaway

Compass demonstrates a simple but powerful idea:

Instead of manually maintaining a portfolio, **an AI agent can continuously improve it**.

By combining repository analysis, structured planning, human approval, and automated pull requests, Compass turns portfolio maintenance into an **ongoing autonomous process**.

This case study itself exists in a portfolio that **Compass actively maintains.**