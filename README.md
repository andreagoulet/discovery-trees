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

This is especially valuable for people with ADHD or anyone who struggles with traditional flat task lists.

## How This Differs From Existing Tools

| Tool Type | Limitation |
|---|---|
| Flat task lists (Todoist, etc.) | No hierarchy; can't model decomposition |
| Kanban boards (Trello, etc.) | Good for workflow status, poor for breaking down work |
| Mind maps (Miro, etc.) | Good for brainstorming, but lack task status/workflow |
| Project managers (Asana, etc.) | Hierarchy exists but no guided decomposition process |

The unique value of a Discovery Tree tool is the **guided decomposition loop** — the software actively walks you through the "Is this actionable?" question rather than passively displaying a tree.

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

### Open Design Questions

1. **Platform** — Web app? Desktop? CLI? Mobile?
2. **Persistence** — Local-first (file-based)? Cloud? Both?
3. **Collaboration** — Solo tool first, or multi-user from the start?
4. **Integration** — Import/export with Todoist, GitHub Issues, etc.?
5. **Visualization** — Horizontal tree? Vertical? Zoomable canvas?
6. **Guided mode** — Active coaching through the decomposition loop vs. passive tree display?

## References

- [Discovery Trees: Visualizing Tasks (Software as Craft)](https://softwareascraft.com/adhd/discovery-trees-visualizing-tasks/)
- [Product Mapping and Discovery Trees (FAST Agile)](https://www.fastagile.io/method/product-mapping-and-discovery-trees)
- [Working With Discovery Trees (Industrial Logic)](https://www.industriallogic.com/blog/discovery-trees/)

## License

TBD
