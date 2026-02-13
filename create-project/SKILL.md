---
name: project-creation
description: This skill teaches you how to determine project types according to user request, and prepare cronJobs and Heartbeat for different project types.
---
# What is a Proactive Project
A proactive project is a project that will be actively and frequently accomplished according to user's request.
A template project is divided into two parts:
- Frequent Signal Gathering: accumulating ingredients for output. Eg, gathering trending recipes and dishes as inspirations for chocolate product RND.
- Output Creation, creating standard output using signals as input. Eg, creating chocolate product RND report by picking the best inspiration of the day as input.

# Supported Project Types
- ProductRnD (project-types/productRnd.md)
- CompetitiveIntel (project-types/competitiveIntel.md)
- TrendStrategy (project-types/brandTrendStrategy.md)
- PRCrisisMonitor (project-types/prCrisisMonitor.md)
- UserInsight (project-types/userInsight.md)
For each supported project types, you must read the corresponding instruction for more creation details.
For unsupported Project types, read similar types for reference and create suitable tasks. If user approves, save the new type under the `project-types` dir for future reference.

# Project ID Naming
Format: `YYYY-MM-DD-<Project-Keywords>-<ProductType>`
Eg: `2026-02-01-Chocolate-Biscuit-ProductRnD`

# CronJob vs. Heartbeat
## Heartbeat
Runs at regular intervals (default: every 30 minutes)
Batches multiple tasks in one turn
Context-aware: uses full main session history
Management: edit HEARTBEAT.md in the workspace

## Cron Job
Runs at exact times (cron expressions, ISO timestamps, or intervals)
Precise timing: exact execution time
Management: via CLI, Gateway API, or the cron tool
Lacks context information, thus must make sure there is enough context information about the task when creating a new cronjob.

# Output and Notification
Project's every output of both Frequent Signal Gathering and Output Creation, aside from each project types' demand, needs to send a notification message notifying the user that an new output can be accessed. The method of messaging is not through any channel, but recorded in `messages/YYYYMMDD-HHMMSS.md`(named with output time) directory in below markdown format.

## Output Format
All output, if not specified, should follow this Markdown format with yaml header:
```
---
time: (YYYYMMDD-HHMMSS)
projectId: 
title: 
description: (Optional, 200 char max)
url: (optional)
---
(Optional output content that does not fit the above metadata fields, eg. Exceptions, Troubleshoot, Long Markdown Output, etc.)
```