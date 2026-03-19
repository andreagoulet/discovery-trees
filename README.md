# Discovery Trees

A task management tool built on the Discovery Trees methodology — where the software actively guides you through decomposing work, dynamically prioritizing what matters, and making progress visible at every level.

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

- **Guided decomposition** — the software walks you through the "Is this actionable?" question rather than leaving you to organize a blank canvas. This is the core innovation (see [The Guided Decomposition Loop](#the-guided-decomposition-loop) below).
- **Dynamic prioritization** — priorities live in the tree structure, not in time slots. When something urgent arrives, insert a branch and reorder — the guided loop picks it up automatically. No need to rebuild a calendar. (See [Dynamic Prioritization](#dynamic-prioritization) below.)
- **Externalizing memory** — the tree holds the plan so your brain doesn't have to
- **Eliminating decision fatigue** — the next action is always visible
- **Breaking overwhelm** — big goals become small, concrete steps
- **Showing progress** — completed branches give a visual sense of momentum
- **Supporting late discovery** — new sub-tasks can be added anytime as you learn more

This is especially valuable for people with ADHD or anyone who struggles with traditional flat task lists.

## How This Differs From Existing Tools

| Tool Type | Limitation |
|---|---|
| Flat task lists ([Todoist](https://todoist.com), [Google Tasks](https://support.google.com/tasks), etc.) | No hierarchy; can't model decomposition |
| Kanban boards ([Trello](https://trello.com), etc.) | Good for workflow status, poor for breaking down work |
| Mind maps ([Miro](https://miro.com), etc.) | Good for brainstorming, but lack task status/workflow |
| Project managers ([Asana](https://asana.com), etc.) | Hierarchy exists but no guided decomposition process |
| Outliners ([Workflowy](https://workflowy.com), etc.) | Excellent decomposition, but passive — no guidance, no task state, no process |
| Second brain tools ([Obsidian](https://obsidian.md), [Notion](https://notion.so)) | Rich knowledge management, but tasks are an afterthought — no decomposition loop, no guided workflow |
| Calendar time-blocking ([Akiflow](https://akiflow.com), [Sunsama](https://sunsama.com), [Reclaim](https://reclaim.ai)) | Forces commitment to specific time slots, but brittle when priorities shift — one unexpected change cascades through the whole schedule |

### Dynamic Prioritization

Calendar-based approaches like zero-based time budgeting assume you know in advance what your day looks like. In practice, priorities shift constantly — an inbound lead from a high-profile client, an urgent issue, a meeting that runs long. When a time-blocked calendar breaks, you have to manually rebuild the whole schedule.

Discovery Trees handle this naturally because **priorities live in the tree structure, not in time slots**. When something urgent arrives:

- Insert the new branch wherever it belongs
- Reorder siblings to reflect the new priority
- The guided loop picks it up automatically — no need to rearrange a calendar

The tree doesn't care *when* you work on something, only *what* matters most right now. This makes it inherently resilient to change. The decomposition stays valid even when the schedule doesn't.

## Requirements

### Core Data Model

- Tree of nodes where each node represents a task or goal
- Nodes can be decomposed into children at any time (discovery is ongoing, not upfront)
- Status per node: not started, in progress, done, blocked
- A node is "actionable" when it's leaf-sized — small enough to start right now
- Completing all children may auto-complete the parent, or require explicit confirmation

### The Guided Decomposition Loop

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

### AI-Assisted Organization

Beyond the guided loop, AI can play a key role in tree management:

- **Brain dump mode** — a freeform input where you pour out unstructured thoughts. The AI organizes them into the tree, placing new leaves where they make sense, suggesting structure, and flagging duplicates.
- **Reorganization suggestions** — the AI can propose moves, merges, or deletions as the tree evolves.
- **Decomposition assistance** — when you say "break it down," the AI can suggest child tasks rather than requiring you to think of them from scratch.

The user should always see what the AI plans to do before it reshuffles the tree (like a diff preview), preserving trust and agency.

### Platform Direction

1. **CLI first** — nail the data model and guided loop logic with a minimal command-line prototype. This validates the core experience before investing in UI.
2. **Web app** — the real product, with keyboard-first navigation, voice-to-text input (via the Web Speech API), and AI-assisted organization. Web is the right platform because voice input, AI diff previews, and brain-dump mode are all much more natural in a browser.

The CLI becomes the backend prototype, not the product.

### Open Design Questions

1. **Persistence** — Local-first (file-based)? Cloud? Both?
2. **Collaboration** — Solo tool first, or multi-user from the start?
3. **Integration** — Import/export with Todoist, GitHub Issues, etc.?
4. **Visualization** — Horizontal tree? Vertical? Zoomable canvas?

## MVP: The Guided Loop on the CLI

The goal of the first build session is to create the smallest thing that lets you *experience* the guided decomposition loop — not design it in the abstract, but feel it with real tasks. The tool itself is being built using the Discovery Tree methodology: start simple, use it, and let the reactions guide what to build next.

### What the MVP does

1. Create a new tree with a root goal
2. The system asks: "Is this small enough to start right now?"
3. **Yes** → marks it "in progress"
4. **No** → prompts you to add child tasks, then recurses into the first child
5. Mark a task done → system moves to the next sibling (or back up to the parent)
6. Print the tree after each step so you can see where you are

That's it. No AI, no voice, no fancy rendering. Just the loop.

### Example session

```
$ dt new "Launch landing page"

🌱 New tree: Launch landing page

Is "Launch landing page" small enough to start right now? (y/n): n

What needs to happen first? (enter tasks, blank line to finish):
> Write the copy
> Design the hero section
> Set up hosting

Added 3 children. Focusing on the first one...

Launch landing page
├── → Write the copy
├── ○ Design the hero section
└── ○ Set up hosting

Is "Write the copy" small enough to start right now? (y/n): y

✅ "Write the copy" is now in progress. Let me know when you're done.

$ dt done

✅ "Write the copy" is complete!

Launch landing page
├── ✅ Write the copy
├── → Design the hero section
└── ○ Set up hosting

Is "Design the hero section" small enough to start right now? (y/n): n

What needs to happen first? (enter tasks, blank line to finish):
> Pick a layout
> Choose images

Launch landing page
├── ✅ Write the copy
├── 🔵 Design the hero section
│   ├── → Pick a layout
│   └── ○ Choose images
└── ○ Set up hosting

Is "Pick a layout" small enough to start right now? (y/n): y

✅ "Pick a layout" is now in progress.
```

### What to pay attention to while using it

The MVP is a discovery tool for its own requirements. While using it, notice your reactions:

- "I lost track of where I am" → we need better navigation
- "I want to see the whole tree" → we need a zoom-out view
- "That felt like too many steps" → the loop is too rigid
- "I want to go back to something else" → we need free navigation, not just linear flow
- "I wish it would suggest tasks for me" → that's the AI feature

These reactions are the real requirements. Write them down as you go — they're more valuable than any spec written in advance.

### Technical starting point

- **Language**: TBD (discuss with your pairing partner)
- **Storage**: JSON file on disk (simplest possible persistence)
- **Scope**: just the loop above — no config, no undo, no multiple trees

## References

- [Discovery Trees: Visualizing Tasks (Software as Craft)](https://softwareascraft.com/adhd/discovery-trees-visualizing-tasks/)
- [Product Mapping and Discovery Trees (FAST Agile)](https://www.fastagile.io/method/product-mapping-and-discovery-trees)
- [Working With Discovery Trees (Industrial Logic)](https://www.industriallogic.com/blog/discovery-trees/)

## License

TBD
