# Design Decisions

A running log of design and technical decisions, and the reasoning behind them. When a session reaction turns into a design choice, it graduates here.

## How to use this file

Add new decisions at the top so the most recent are first. Include the date, the decision, and why — the "why" is the most important part.

---

### 2026-03-19 — Outside-in development with approval tests

**Decision**: Drive development outside-in, feature by feature, using approval tests (approvaltests library) to capture CLI output as the verified behavior.

**Why**: Approval tests let us see and approve the exact user experience before locking it in. Outside-in keeps us focused on what the user sees rather than internal structure.

### 2026-03-19 — Python for CLI, TypeScript for web app

**Decision**: CLI prototype in Python, web app in TypeScript. Top-level `cli/` and `web/` directories.

**Why**: Python is simple to get a CLI running (no build step), and the approval-tests library has strong Python support. TypeScript is the natural choice for the web app later. Separating into `cli/` and `web/` keeps them cleanly independent.

### 2026-03-19 — CLI first, then web app

**Decision**: Build a CLI prototype first to validate the guided decomposition loop, then build the real product as a web app.

**Why**: The CLI is the fastest path to experiencing the core loop. Web is the right long-term platform because it supports voice input, AI diff previews, and brain-dump mode more naturally. The CLI validates the data model and loop logic before investing in UI.

### 2026-03-19 — Dynamic prioritization over time-blocking

**Decision**: Priorities live in the tree structure (sibling order), not in time slots.

**Why**: Calendar-based approaches are brittle when plans change. A tree-based approach lets you insert and reorder branches without rebuilding a schedule. The decomposition stays valid even when the timeline doesn't.

### 2026-03-19 — Guided loop is the core differentiator

**Decision**: The software actively walks users through the "Is this small enough to start right now?" question rather than passively displaying a tree.

**Why**: Every existing tool (outliners, project managers, mind maps) gives you a canvas and lets you organize however you want. The guided loop is what makes Discovery Trees a coach rather than a blank page.
