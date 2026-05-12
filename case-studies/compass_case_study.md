---
title: "Compass Case Study"
permalink: /case-studies/compass_case_study/
---

# Compass

Repository-aware maintenance agent that audits this portfolio, proposes changes, and supports approval-first pull request workflows.

## Problem

Portfolios and technical repos decay quietly over time. Links break, descriptions drift away from implementation reality, and new work never gets surfaced. Manual upkeep is easy to postpone, especially when the work itself is changing quickly.

Compass was built to make maintenance less manual and more systematic.

## System Built

Compass is an agent workflow for portfolio and repository maintenance. Instead of directly editing content without oversight, it inspects repository state, identifies likely improvements, produces a structured change plan, and only proceeds with implementation after approval.

## Stack and Architecture

- Repository scanning over portfolio source files
- Structured analysis of project pages, case studies, and documentation
- Change-plan generation before edits
- Human approval checkpoint
- Pull request oriented execution workflow

## Constraints

- Avoid noisy or low-value automated edits
- Keep the user in control of public-facing changes
- Work from actual repository state rather than assumptions
- Improve professionalism without inflating project claims

## What Works Today

- Auditing of this portfolio repository
- Detection of content, link, and structure issues
- Proposal-oriented workflow for portfolio improvements
- Practical use as part of keeping this site current

## Evidence and Current Status

Compass is best understood as an automation workflow project rather than a model benchmark project. Its evidence comes from usefulness: it helps review the site, identify needed changes, and convert maintenance into a repeatable approval-first process.

That makes it a strong example of the kind of applied AI engineering I enjoy most: systems that improve real workflows through orchestration, structure, and sensible guardrails.

## Why It Matters

Compass demonstrates agentic engineering in a way that is concrete and legible. It is not just a chat interface with tools attached. It is a workflow with repository context, decision points, and a clear success condition: better maintenance with less manual overhead and better change discipline.

## Next Engineering Milestone

- Expand repository analysis depth and change detection
- Improve prioritization of recommendations
- Generalize the workflow beyond a single portfolio repository
