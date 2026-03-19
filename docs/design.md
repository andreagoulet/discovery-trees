# Design

Working design notes for Discovery Trees. This document captures requirements, design explorations, and open questions as the project evolves.

## Core Data Model

- Tree of nodes where each node represents a task or goal
- Nodes can be decomposed into children at any time (discovery is ongoing, not upfront)
- Status per node: not started, in progress, done, blocked
- A node is "actionable" when it's leaf-sized — small enough to start right now
- Completing all children may auto-complete the parent, or require explicit confirmation

## The Guided Decomposition Loop

The guided loop is the core innovation — the thing that separates this from every outliner and task manager. The software doesn't just display a tree; it actively walks you through it.

1. **Focus** — the system presents a single node and asks: "Is this small enough to start right now?"
2. **Decide** — Yes → mark it "in progress" and start working. No → break it down.
3. **Decompose** (if no) — prompt: "What's the most important part that doesn't exist yet?" Add children, then recurse into the first one.
4. **Complete** (if yes) — when done, mark complete. The system auto-navigates to the next sibling, or walks back up to the parent if all siblings are done.
5. **Repeat** — the loop continues until the root goal is complete.

The key design tension is **agency vs. guidance**. Too much guidance and power users feel constrained. Too little and it's just another outliner. Possible approaches:

- **Focus mode** — a modal, step-by-step flow that walks through one node at a time. Maximum guidance, but can feel constraining.
- **Inline prompts** — keep the full tree visible, attach contextual prompts to nodes that need attention. Less guided, but preserves context.
- **Sidebar coach** — the tree lives in the main panel; a persistent sidebar shows the current focus and the decomposition question. Guidance without taking over.
- **Hybrid** — default view is a normal tree, but you can enter "focus mode" on any subtree to get the guided loop. Best of both worlds.

## AI-Assisted Organization

Beyond the guided loop, AI can play a key role in tree management:

- **Brain dump mode** — a freeform input where you pour out unstructured thoughts. The AI organizes them into the tree, placing new leaves where they make sense, suggesting structure, and flagging duplicates.
- **Reorganization suggestions** — the AI can propose moves, merges, or deletions as the tree evolves.
- **Decomposition assistance** — when you say "break it down," the AI can suggest child tasks rather than requiring you to think of them from scratch.

The user should always see what the AI plans to do before it reshuffles the tree (like a diff preview), preserving trust and agency.

## Platform Direction

1. **CLI first** — nail the data model and guided loop logic with a minimal command-line prototype. This validates the core experience before investing in UI.
2. **Web app** — the real product, with keyboard-first navigation, voice-to-text input (via the Web Speech API), and AI-assisted organization. Web is the right platform because voice input, AI diff previews, and brain-dump mode are all much more natural in a browser.

The CLI becomes the backend prototype, not the product.

## Open Design Questions

1. **Persistence** — Local-first (file-based)? Cloud? Both?
2. **Collaboration** — Solo tool first, or multi-user from the start?
3. **Integration** — Import/export with Todoist, GitHub Issues, etc.?
4. **Visualization** — Horizontal tree? Vertical? Zoomable canvas?
