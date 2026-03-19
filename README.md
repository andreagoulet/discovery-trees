# Discovery Trees

A task management tool based on the Discovery Trees methodology — a mind-map-like approach to visualizing and decomposing work that makes progress visible and decisions simple.

## What Are Discovery Trees?

Discovery Trees are visual, hierarchical task structures where:

- **Root** = primary goal
- **Branches** = sub-tasks needed to achieve it
- **Sub-branches** = further decomposition when something isn't actionable yet

The core loop is a single question: **"Is this small enough to start right now?"**

- If **no** → break it down further ("What's the most important part that doesn't exist yet?")
- If **yes** → mark it "in progress" and start working
- When **done** → mark complete, return to the parent, pick the next item

This cycle of decompose → do → reassess is what makes Discovery Trees a *discovery* process rather than upfront planning.

## Why This Approach Works

Discovery Trees address common task management challenges by:

- **Externalizing memory** — the tree holds the plan so your brain doesn't have to
- **Eliminating decision fatigue** — the next action is always visible
- **Breaking overwhelm** — big goals become small, concrete steps
- **Showing progress** — completed branches give a visual sense of momentum
- **Supporting late discovery** — new sub-tasks can be added anytime as you learn more
- **Dynamic prioritization** — priorities live in the tree structure, not in time slots, so when things change you reorder branches instead of rebuilding a schedule

This is especially valuable for people with ADHD or anyone who struggles with traditional flat task lists.

## How This Differs From Existing Tools

| Tool Type | Limitation |
|---|---|
| Flat task lists (Todoist, etc.) | No hierarchy; can't model decomposition |
| Kanban boards (Trello, etc.) | Good for workflow status, poor for breaking down work |
| Mind maps (Miro, etc.) | Good for brainstorming, but lack task status/workflow |
| Project managers (Asana, etc.) | Hierarchy exists but no guided decomposition process |
| Outliners (Workflowy, etc.) | Excellent decomposition, but passive — no guidance, no task state, no process |
| Second brain tools (Obsidian, Notion) | Rich knowledge management, but tasks are an afterthought — no decomposition loop, no guided workflow |
| Calendar time-blocking (zero-based budgeting) | Forces commitment to specific time slots, but brittle when priorities shift — one unexpected change cascades through the whole schedule |

The unique value of a Discovery Tree tool is the **guided decomposition loop** — the software actively walks you through the "Is this actionable?" question rather than passively displaying a tree.

### Dynamic Prioritization

Calendar-based approaches like zero-based time budgeting assume you know in advance what your day looks like. In practice, priorities shift constantly — an inbound lead from a high-profile client, an urgent production issue, a meeting that runs long. When a time-blocked calendar breaks, you have to manually rebuild the whole schedule.

Discovery Trees handle this naturally because **priorities live in the tree structure, not in time slots**. When something urgent arrives:

- Insert the new branch wherever it belongs
- Reorder siblings to reflect the new priority
- The guided loop picks it up automatically — no need to rearrange a calendar

The tree doesn't care *when* you work on something, only *what* matters most right now. This makes it inherently resilient to change. The decomposition stays valid even when the schedule doesn't.

Second brain tools like Obsidian and Notion are powerful for capturing and linking knowledge, but they treat tasks as just another note type. There's no guided process for breaking work down, no status propagation, no "what should I do next?" loop. You can build task systems in them (and many people do), but you're assembling it yourself from generic primitives rather than using a tool purpose-built for decomposition and discovery.

### Workflowy: The Closest Comparison

Workflowy is the closest existing tool — both are infinite outliners with hierarchical decomposition. The overlap is real: infinite nesting, zoom into any node, frictionless child creation, collapse/expand. But the differences are fundamental:

- **Passive vs. active** — Workflowy is a blank canvas. Discovery Trees actively drive a cognitive loop, prompting "Is this small enough to start right now?" at each node. That single question forces a binary decision: either produce action or decompose further.
- **Task state as a first-class concept** — Workflowy nodes are just text. Discovery Trees treat status (not started, in progress, done, blocked) as core — it's how progress propagates up the tree and how the system knows what to prompt you about next.
- **Navigation with intent** — In Workflowy you browse. In Discovery Trees, the system guides you — after completing a task, it surfaces the next sibling or walks you back up to the parent. You're not choosing where to look; the tree tells you where attention is needed.
- **Progress visualization** — Workflowy shows structure. Discovery Trees show *momentum* — which branches are complete, which are stalled, where the frontier of work is.

In short: Workflowy nails decomposition but is entirely missing the guided part. It's a blank canvas, not a coach.

## Requirements

### Core Data Model

- Tree of nodes where each node represents a task or goal
- Nodes can be decomposed into children at any time (discovery is ongoing, not upfront)
- Status per node: not started, in progress, done, blocked
- A node is "actionable" when it's leaf-sized — small enough to start right now
- Completing all children may auto-complete the parent, or require explicit confirmation

### Key Interactions

- **Guided decomposition** — the central UX prompts: "Is this small enough to do right now?" → Yes (start) or No (break it down)
- **Quick decomposition** — adding child nodes must be frictionless
- **Navigation** — zoom into a subtree or zoom out to see the big picture
- **Reordering/prioritizing** among sibling nodes
- **Progress visualization** — see at a glance what's done, in progress, and remaining

### The Guided Decomposition Loop

The guided loop is the core innovation — the thing that separates this from every outliner and task manager. The software doesn't just display a tree; it actively walks you through it.

The loop works like this:

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

### AI-Assisted Organization

Beyond the guided loop, AI can play a key role in tree management:

- **Brain dump mode** — a freeform input where you pour out unstructured thoughts. The AI organizes them into the tree, placing new leaves where they make sense, suggesting structure, and flagging duplicates.
- **Reorganization suggestions** — the AI can propose moves, merges, or deletions as the tree evolves.
- **Decomposition assistance** — when you say "break it down," the AI can suggest child tasks rather than requiring you to think of them from scratch.

The user should always see what the AI plans to do before it reshuffles the tree (like a diff preview), preserving trust and agency.

### Platform Direction

The planned approach is:

1. **CLI first** — nail the data model and guided loop logic with a minimal command-line prototype. This validates the core experience before investing in UI.
2. **Web app** — the real product, with keyboard-first navigation, voice-to-text input (via the Web Speech API), and AI-assisted organization. Web is the right platform because voice input, AI diff previews, and brain-dump mode are all much more natural in a browser.

The CLI becomes the backend prototype, not the product.

### Open Design Questions

1. **Persistence** — Local-first (file-based)? Cloud? Both?
2. **Collaboration** — Solo tool first, or multi-user from the start?
3. **Integration** — Import/export with Todoist, GitHub Issues, etc.?
4. **Visualization** — Horizontal tree? Vertical? Zoomable canvas?

## References

- [Discovery Trees: Visualizing Tasks (Software as Craft)](https://softwareascraft.com/adhd/discovery-trees-visualizing-tasks/)
- [Product Mapping and Discovery Trees (FAST Agile)](https://www.fastagile.io/method/product-mapping-and-discovery-trees)
- [Working With Discovery Trees (Industrial Logic)](https://www.industriallogic.com/blog/discovery-trees/)

## License

TBD
