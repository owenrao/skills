
# Daily Summary Report

### Aggregate Previous Day's Signals
Read all signal files from yesterday in `projects/<projectId>/signals/`
If None, skip the task. FORBID false alarm.

### Report Structure:
```markdown
---
time: YYYYMMDD-090000
projectId: {projectId}
title: Daily Customer Sentiment Summary
impact: [severity: Highest severity from yesterday's signals]
description: [Max 200 chars summary]
---

## Top Complaint Themes (Past 24h)
1. [Category]: [X mentions] - [Brief description]
2. [Category]: [X mentions] - [Brief description]
3. [Category]: [X mentions] - [Brief description]

## Sentiment Trend
- Overall: [Positive/Negative/Mixed]
- Change vs. previous day: [Improving/Worsening/Stable]
- Volume: [Spike/Normal/Declining]

## Priority Actions
[Action 1]: [Why and what to do, 2-3 sentences]
[Action 2]: [Why and what to do, 2-3 sentences]
[Action 3]: [Why and what to do, 2-3 sentences]

## At-Risk Customers
- [Customer identifier if available]: [Issue] - [Recommended outreach]

## Monitoring Notes
- Total signals: [Count]
- Critical issues: [Count]
- New patterns: [Any emerging trends]
```

## Best Practices

### DO:
- ✅ Prioritize recent feedback (last 4 hours for signals)
- ✅ Flag enterprise/high-value customers explicitly
- ✅ Note recurring issues (check previous signals)
- ✅ Include direct quotes with source links
- ✅ Provide specific metrics (complaint counts, sentiment shifts)

### DON'T:
- ❌ Ignore positive feedback (can amplify in marketing)
- ❌ Treat every complaint as crisis (filter noise)
- ❌ Duplicate signals already captured
- ❌ Miss time-sensitive issues (billing errors, outages)
- ❌ Forget to copy daily reports to messages directory