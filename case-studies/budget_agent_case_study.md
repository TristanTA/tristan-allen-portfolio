---
title: "Budget Agent Case Study"
permalink: /case-studies/budget_agent_case_study/
---

# Budget Agent

Telegram-based personal finance agent built to turn messy budgeting inputs into structured records, analysis, and forward-looking loan and cashflow planning.

## Problem

Personal budgeting often breaks down at the point where information becomes messy. Transactions come from different places, receipts are hard to consolidate, and it is easy to underestimate how much small financial decisions affect debt payoff over time.

Budget Agent was built to reduce that friction by creating a practical assistant for financial intake, budget analysis, and scenario-based planning.

## System Built

Budget Agent is a personal finance agent system with a conversational Telegram interface. It accepts user messages, transaction files, and receipt-style inputs, converts them into structured budget data, stores that data for later use, and routes tasks to specialist agents for database work, analysis, and forecasting.

The goal is not generic financial chat. The goal is a workflow that helps turn raw financial information into decisions.

## Stack and Architecture

- Python-based agent architecture
- Telegram bot interface for lightweight day-to-day interaction
- OpenAI-powered orchestration with specialist sub-agents
- SQLite-backed storage for budget records and persistent financial state
- OCR and file-ingestion flow for receipts and CSV transaction data
- Separate roles for intake parsing, database operations, financial analysis, and forecasting

## Constraints

- Financial decisions depend on clean records and clear assumptions
- User inputs can arrive as text, files, or images rather than neat structured forms
- Forecasting value depends on making projections legible instead of overstated
- The system has to be useful for real budgeting, not just technically interesting

## What Works Today

- Telegram-based conversational intake
- Processing of transaction files and receipt-style inputs
- Structured persistence of financial records
- Specialist-agent routing for analysis, database tasks, and forecasting
- Scenario support for near-term budget review and longer-range planning

## Evidence and Current Status

Budget Agent has been successful as a real personal-use system. Its strongest evidence is not benchmark performance but decision support: it helped identify a repayment path projected to save about $100 per month over the remaining 4 years of loan payments.

That projection is not presented as already realized savings. It is a forecast based on the current numbers and repayment assumptions, but the numbers check out and the result is meaningful enough to show the system's practical value. Over 48 months, that is roughly $4,800 in projected savings.

## Why It Matters

Budget Agent is a strong example of applied AI engineering because it connects models to a real workflow with real stakes. It combines intake, persistence, analysis, and forecasting into a system that helps produce better decisions rather than just nicer summaries.

It also shows a kind of engineering work I care about a lot: building AI systems that are personally useful, operationally grounded, and capable of creating measurable downstream value.

## Next Engineering Milestone

- Strengthen forecast transparency around assumptions and tradeoffs
- Improve transaction normalization and categorization reliability
- Expand scenario comparison for debt payoff, spending cuts, and savings plans
