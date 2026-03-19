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

- **Guided decomposition** — the software walks you through the "Is this actionable?" question rather than leaving you to organize a blank canvas. This is the core innovation (see [design doc](docs/design.md#the-guided-decomposition-loop)).
- **Dynamic prioritization** — priorities live in the tree structure, not in time slots. When something urgent arrives, insert a branch and reorder — the guided loop picks it up automatically. No need to rebuild a calendar.
- **Externalizing memory** — the tree holds the plan so your brain doesn't have to
- **Eliminating decision fatigue** — the next action is always visible
- **Breaking overwhelm** — big goals become small, concrete steps
- **Showing progress** — completed branches give a visual sense of momentum
- **Supporting late discovery** — new sub-tasks can be added anytime as you learn more

This is especially valuable for people with ADHD or anyone who struggles with traditional flat task lists.

## How This Differs From Existing Tools

| Tool Type | Examples | Limitation |
|---|---|---|
| Flat task lists | [Todoist](https://todoist.com), [Google Tasks](https://support.google.com/tasks), [Microsoft To Do](https://todo.microsoft.com) | No hierarchy; can't model decomposition |
| Kanban boards | [Trello](https://trello.com), [GitHub Projects](https://github.com/features/issues), [Kanbanize](https://kanbanize.com) | Good for workflow status, poor for breaking down work |
| Mind maps | [Miro](https://miro.com), [MindMeister](https://www.mindmeister.com), [XMind](https://xmind.app) | Good for brainstorming, but lack task status/workflow |
| Project managers | [Asana](https://asana.com), [Jira](https://www.atlassian.com/software/jira), [Monday.com](https://monday.com) | Hierarchy exists but no guided decomposition process |
| Outliners | [Workflowy](https://workflowy.com), [Dynalist](https://dynalist.io), [Logseq](https://logseq.com) | Excellent decomposition, but passive — no guidance, no task state, no process |
| Second brain tools | [Obsidian](https://obsidian.md), [Notion](https://notion.so), [Roam Research](https://roamresearch.com) | Rich knowledge management, but tasks are an afterthought — no decomposition loop, no guided workflow |
| Calendar time-blocking | [Akiflow](https://akiflow.com), [Sunsama](https://sunsama.com), [Reclaim](https://reclaim.ai) | Forces commitment to specific time slots, but brittle when priorities shift |

### Dynamic Prioritization

Calendar-based approaches like zero-based time budgeting assume you know in advance what your day looks like. In practice, priorities shift constantly — an inbound lead from a high-profile client, an urgent issue, a meeting that runs long. When a time-blocked calendar breaks, you have to manually rebuild the whole schedule.

Discovery Trees handle this naturally because **priorities live in the tree structure, not in time slots**. When something urgent arrives:

- Insert the new branch wherever it belongs
- Reorder siblings to reflect the new priority
- The guided loop picks it up automatically — no need to rearrange a calendar

The tree doesn't care *when* you work on something, only *what* matters most right now. This makes it inherently resilient to change. The decomposition stays valid even when the schedule doesn't.

## Documentation

- [Design](docs/design.md) — requirements, data model, guided loop design, AI features, open questions
- [Decisions](docs/decisions.md) — running log of design and technical decisions with rationale
- [Session notes](docs/sessions/) — pairing session logs capturing what we built, reactions, and discoveries

## References

- [Discovery Trees: Visualizing Tasks (Software as Craft)](https://softwareascraft.com/adhd/discovery-trees-visualizing-tasks/)
- [Product Mapping and Discovery Trees (FAST Agile)](https://www.fastagile.io/method/product-mapping-and-discovery-trees)
- [Working With Discovery Trees (Industrial Logic)](https://www.industriallogic.com/blog/discovery-trees/)

## License

TBD
