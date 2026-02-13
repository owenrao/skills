# Timed task for brand hot topic selection
- Create a cronjob that works every hour, 10 min timeout, and remember to enable it.
- cronjob message should tell the isolated agent to use `brand-trend-strategy` skill.
- Explore existing signals in `projects/<projectId>/signals/` directory to gain inspiration and avoid duplication.
- Output the strategies as mardown file in the `projects/<projectId>/signals/` dir, meanwhile remind the cronjob to make a COPY of the output into the `messages` dir.

## Output Header Format (include EXACTLY in cronjob message)
```
---
time: YYYYMMDD-HHMMSS
projectId: {projectId}
title: Title with informative keywords
Impact: Few words describe what impact will this output bring for the user, or why the user should read this. eg: "Saves 40% of Your Time!"
description: [Brief summarization, max 200 chars]
---
Only include the final BRIEF according to the skill.
```

## Critical Output Instruction (MUST include in cronjob message)
```
Only include the final BRIEF according to the skill.
```