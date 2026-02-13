# Signal Gathering
- Create a cronJob that uses kimi k2.5(remember to enable): 
- use xai-post-search Skill to find those **trending** post content from social media platform X (Twitter); propose a relevant and creative rnd inspiration for each
- Atmost 5 most trending posts
- Search related: 
    Search strategy should find inspirations in a cross field manner. Eg, search for chocolate product rnd inspirations by searching for trending desserts, recipes and international dishes. This widens the search spectrum and introduces diversity and creativity for this inspiration.
    Utilize the query operators. 
    Optimizing the query by standing in the perspective of post authors.
- For each post, record as much detail as possible, include specific post content/details, and report engagement metrics (replies, likes, retweets, views if available).
- Propose a relevant and creative rnd inspiration for each recorded post.
- Post quality (engagement) over post quantity
- When: Every hour.
- Aside from saving in `messages`, Extra Output Location: `projects/<projectId>/signals/YYYYMMDD-HHMM.md`
- Output Format specified in SKILL.md

# Output Creation
- Create a cronJob that has 1 hour timeout(remember to enable), that uses atypica-research skill to create a product rnd research.

**CRITICAL**: When creating the cronJob, copy the following message template EXACTLY into the cronJob message. Replace {} placeholders with actual values dependent on project details. Can edit, but DO NOT summarize, paraphrase, or omit any part.

```
Use atypica-research skill to create a product RND research for project `{projectId}`.

Execution requirements:
1. Pick and find a recent best inspiration from `projects/{projectId}/signals`. Use it to create a new research in Chinese, specifying a. what is the product that requires innovation; b. In detail what is the inspiration, why is it trending and what is its major selling points or reason-to-believe; c. specify you need a product RND report.
2. You can find ATYPICA_API_KEY in USER.md
3. Follow the atypica-research skill instructions strictly
4. Poll every 60 seconds using: sleep 60 && call atypica_study_get_messages
5. Use `tail` parameter to prevent message explosion: call atypica_study_get_messages with `{userChatToken: "<TOKEN>", tail: 1}` (start with 1, increase if more context needed, but never exceed 3)
6. Complete necessary interactions and confirm/fix the plan provided by Atypica.
7. After plan confirmation, increase poll interval to 5 minutes
8. Check only `isRunning` status and latest tool states from returned messages
9. You are not allowed to create subagent in this cronjob.

Output requirements:
- Each output (replay URL, etc.) must be recorded in a separate file: messages/YYYYMMDD-HHMMSS.md (use current timestamp as filename)
- Output format:
'''
---
time: YYYYMMDD-HHMMSS
projectId: {projectId}
title: Atypica Research Complete - [Research Title from User Query]
description: [Brief description, max 200 chars]
url: https://atypica.ai/study/<RESEARCH_TOKEN>/share?replay=1
---
[Any additional content: exceptions, troubleshooting, long markdown output, etc.]
'''
Continue polling until research is complete, then save the replay URL to the message file following the format above.
```