# Customer Sentiment Monitor - Product & Customer Success Intelligence
- Create a cronjob that gathers new customer feedback every 4 hours, 10 min timeout, and remember to enable it.
- cronjob message should tell the isolated agent to use `customer-sentiment-monitor` skill, and check previous signals in the project directory to track sentiment trends and avoid duplication.
- Output signal files to `projects/<projectId>/signals/` dir, meanwhile remind the cronjob to make a COPY into the `messages` dir.
- Remind it to add the following yaml header in the output report md file, include the following format into the cronjob message EXACTLY:
```
---
time: YYYYMMDD-HHMMSS
projectId: {projectId}
title: Regular Customer Sentiment Monitor
---
```

# Daily Summary Report
- create a cronjob that runs every day 9 AM, summarizes all the signals of yesterday from `projects/<projectId>/signals/` dir.
- cronjob message should tell the isolated agent to use `customer-sentiment-monitor` skill.
- Remind it to add the following yaml header in the output report md file, include the following format into the cronjob message EXACTLY:
```
---
time: YYYYMMDD-090000
projectId: {projectId}
title: Daily Customer Sentiment Summary
impact: [severity: Highest severity from yesterday's signals]
description: [Max 200 chars summary]
---
```