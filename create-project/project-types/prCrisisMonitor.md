# PR Crisis Monitor - Public Relations & Reputation Management
- Create a cronjob that works every 1 hours, 10 min timeout, and remember to enable it.
- cronjob message should tell the isolated agent to use `pr-crisis-monitoring` skill, and check previous signals in the project directory to track narrative evolution and avoid duplication.
- Output the monitoring reports as markdown file in the `projects/<projectId>/signals/` dir, meanwhile remind the cronjob to make a COPY of the output into the `messages` dir.
- Remind it to add the following yaml header in the output report md file, include the following format into the cronjob message EXACTLY:
```
---
time: YYYYMMDD-HHMMSS
projectId: {projectId}
title: [Concise alert title]
impact: [Sentiment: Positive/Negative/Mixed/Neutral | Severity: Critical/High/Medium/Low]
description: [Brief summarization, max 200 chars]
---
```