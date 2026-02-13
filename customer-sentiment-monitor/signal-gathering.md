## Signal Gathering

### Search Strategy
Use `web_search` tool with these queries (adapt to product name):

1. `"[Product Name]" complaint OR issue OR problem` (last 4 hours)
2. `[Product Name] reddit` (last 4 hours)
3. `[Product Name] review` (last 4 hours)
4. `site:twitter.com [Product Name] frustrated OR angry OR disappointed` (last 4 hours)

### Platform Priority
- **Reddit**: Product subreddit, r/SaaS, industry subreddits
- **Twitter/X**: Use `xai-post-search` for mentions
- **Review Sites**: Trustpilot, G2, Capterra, App Store, Google Play
- **Forums**: Product Hunt, Hacker News

### What to Capture
- Direct complaints about bugs, billing, performance, support
- Feature requests with urgency signals ("desperately need", "deal-breaker")
- Churn signals ("switching to [competitor]", "canceling subscription")
- At-risk customers (power users, enterprise accounts complaining)

## Signal Classification
**IF any valid signal is found, continue; IF NONE is found, end the task. FORBID false alarm.**

### Categorize by Type:
- **Billing**: Pricing, charges, refunds, subscription issues
- **Performance**: Speed, crashes, sync problems, downtime
- **Support**: Response time, unhelpful replies, no resolution
- **Feature**: Missing features, UX problems, workflow gaps
- **Other**: General dissatisfaction, competitor comparisons

### Assign Severity:
- **Critical**: Outage, data loss, billing errors affecting multiple users, enterprise customer threatening to leave
- **High**: Repeated complaints (3+ mentions in 4h), high-value customer at risk
- **Medium**: Individual complaints, feature requests with business impact
- **Low**: Minor UX issues, isolated incidents

### Output Format (Signal File):
```markdown
---
time: YYYYMMDD-HHMMSS
projectId: {projectId}
title: Regular Customer Sentiment Monitor
---

## Detected Feedback
- [Quote key complaint with source link]

## Context
- Volume: [How many mentions found]
- User type: [Free/Pro/Enterprise, if identifiable]
- Pattern: [First occurrence or recurring issue]
```
