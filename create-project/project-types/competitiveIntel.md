# Competitive Intelligence Signal Gathering
- Create a cronjob that works every hour, 10 min timeout, and remember to enable it.
- cronjob message should tell the isolated agent to use `competitive-intel-research` skill.
- Remind it to add the following yaml header in the output report md file, include the following format into the cronjob message EXACTLY:
```
---
time: YYYYMMDD-HHMMSS
projectId: {projectId}
title: Attracting Title
Impact: Few words describe what impact will this output bring for the user. eg: 
description: [Brief summarization, max 200 chars]
---
```
- `competitive-intel-research` skill has its own saving directory in `projects/<projectId>/signals/`, remind the cronjob to make a COPY of the output into the `messages` dir.