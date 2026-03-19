# Design Decisions

A running log of design and technical decisions, and the reasoning behind them. When a session reaction turns into a design choice, it graduates here.

## How to use this file

Add new decisions at the top so the most recent are first. Include the date, the decision, and why — the "why" is the most important part.

---

### 2026-03-19 — CLI first, then web app

**Decision**: Build a CLI prototype first to validate the guided decomposition loop, then build the real product as a web app.

**Why**: The CLI is the fastest path to experiencing the core loop. Web is the right long-term platform because it supports voice input, AI diff previews, and brain-dump mode more naturally. The CLI validates the data model and loop logic before investing in UI.

### 2026-03-19 — Dynamic prioritization over time-blocking

**Decision**: Priorities live in the tree structure (sibling order), not in time slots.

**Why**: Calendar-based approaches are brittle when plans change. A tree-based approach lets you insert and reorder branches without rebuilding a schedule. The decomposition stays valid even when the timeline doesn't.

### 2026-03-19 — Guided loop is the core differentiator

**Decision**: The software actively walks users through the "Is this small enough to start right now?" question rather than passively displaying a tree.

**Why**: Every existing tool (outliners, project managers, mind maps) gives you a canvas and lets you organize however you want. The guided loop is what makes Discovery Trees a coach rather than a blank page.
