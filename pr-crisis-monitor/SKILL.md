---
name: pr-crisis-monitoring
description: Monitors online discourse about a company, detects sentiment patterns and emerging narratives, provides concise multi-dimensional PR response strategies for crisis prevention and reputation management.
---

# PR Crisis Monitoring Skill

## Objective
Scan online sources for company mentions, identify sentiment trends and emerging narratives, assess reputation risks, and deliver actionable PR recommendations in 3 sentences max per dimension.

## Step 1: Signal Gathering

### Web Search Strategy
Use `web_search` tool with these queries (adapt to company name):
1. `"[Company Name/Industry]" news` (last 24-48 hours)
2. `[Company Name/Industry] stock OR shares OR investors`
3. `[Company Name/Industry] controversy OR criticism OR lawsuit`
4. `[Company Name/Industry] policy OR regulation OR compliance`

### Social Media Monitoring
Use `xai-post-search` skill to search for:
- Company mentions in last 48 hours
- Relevant hashtags and trending topics
- Posts from influential accounts (analysts, journalists, activists)

### Red Flags to Watch:
- Sudden spike in mention volume
- Coordinated campaigns (bot-like patterns, repetitive content)
- Verified account criticisms
- Regulatory/legal language
- Stock price movements mentioned alongside company

## Step 2: Sentiment & Narrative Analysis

### Classify Each Signal:
1. **Sentiment**: Positive / Negative / Neutral / Mixed
2. **Severity**: Critical / High / Medium / Low
3. **Narrative Type**:
   - Rumor/Misinformation
   - Policy/Regulatory Impact
   - Market Reaction
   - Operational Issue
   - Reputation Attack
   - Positive Momentum

### Pattern Detection:
- Isolated incident or trend?
- Multiple sources reporting same narrative?
- Sentiment shift vs. previous cycles?
- Early warning signs of escalation?

## Step 3: Multi-Dimensional PR Recommendations

Provide 3-5 actionable recommendations covering different stakeholder perspectives. **3 sentences max per dimension.**

### Key Dimensions (choose relevant ones):

**Investor Relations**: Messaging to calm market concerns, data points to emphasize

**Media Strategy**: Proactive vs. reactive response, which outlets to engage, spokesperson selection

**Regulatory/Government Affairs**: Compliance messaging, political sensitivities

**Social Media**: Response tone and timing, third-party validators

**Internal Communications**: Employee talking points, morale management

**Long-term Reputation**: Strategic repositioning opportunities

### Style Guide:
✅ **Good**: "Issue brief statement to stock exchange within 24h clarifying policy impact affects <10% revenue, citing diversified client base. Emphasize recent contract wins as business continuity evidence. Lead with facts, avoid defensive tone."

❌ **Bad**: "The company should think carefully about how investors might be feeling... It's important to communicate, but we need to make sure we don't say anything that could be misinterpreted..."

## Step 4: Crisis Escalation Indicators

**Trigger immediate alert** if detected:
- Stock price drop >5% with company in financial media
- Government/regulatory body public criticism
- Coordinated campaign >10K engagements in 24h
- Top-tier media running investigative pieces
- Legal action announced

For Critical/High severity:
```
⚠️ ESCALATION RECOMMENDED: [Reason]
Immediate actions: [1-2 concrete steps]
```

## Step 5: Output Generation

### Report Structure:
```
1. Detected Signals
[Key findings with source links]

2. Sentiment Snapshot
- Overall: [Positive/Negative/Mixed]
- Trend: [Improving/Worsening/Stable]
- Volume: [Spike/Normal/Declining]

3. PR Recommendations
[Dimension Name]: [3 sentences max]
[Dimension Name]: [3 sentences max]
[Continue for other optional dimensions]

4. Monitoring Notes
- Sources checked: [List]
- Narrative evolution: [vs. previous signals]
- Next check priority: [What to watch]
```

## Best Practices

### DO:
- ✅ Prioritize recent (24-48h) signals
- ✅ Distinguish credible sources from fringe claims
- ✅ Provide specific metrics (%, volume, engagement)
- ✅ Suggest response timing ("within 24h", "before market close")
- ✅ Note AI-generated or bot content patterns

### DON'T:
- ❌ Write long essays—keep directives clear and fast
- ❌ Recommend legally impossible actions
- ❌ Ignore positive signals (can be amplified)
- ❌ Treat every mention as crisis (filter noise)
- ❌ Duplicate previous recommendations without new context

---

**Goal**: Early detection + rapid, strategic response. Keep it sharp, keep it actionable.