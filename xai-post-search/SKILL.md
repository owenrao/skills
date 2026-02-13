---
name: xai-post-search
description: Search X (Twitter) posts using XAI Grok with server-side x-search tool. Uses Grok's built-in search capabilities to find trending and engaging posts.
metadata:
  {
    "openclaw":
      {
        "emoji": "🔍",
        "requires": { "bins": ["uv"], "env": ["XAI_API_KEY"] },
        "primaryEnv": "XAI_API_KEY",
        "install":
          [
            {
              "id": "uv-brew",
              "kind": "brew",
              "formula": "uv",
              "bins": ["uv"],
              "label": "Install uv (brew)",
            },
          ],
      },
  }
---

# XAI Post Search

Search X (Twitter) posts using XAI Grok's server-side x-search tool. Grok uses its built-in search capabilities to find relevant, trending, and engaging posts based on your query.

## Search Posts

```bash
uv run {baseDir}/scripts/xai-search.py "your search query"
```

You can use advanced X search operators in your query:
- `"exact phrase"` - exact phrase matching
- `from:username` - posts from specific user
- `lang:en` - language filter
- `-is:retweet` - exclude retweets
- `filter:media` - posts with media
- `since:YYYY-MM-DD` - date range
- `OR` / `AND` - boolean operators

Examples:
```bash
uv run {baseDir}/scripts/xai-search.py "AI lang:en -is:retweet"
uv run {baseDir}/scripts/xai-search.py "from:elonmusk OR from:xai"
uv run {baseDir}/scripts/xai-search.py "trending topic since:2025-01-01"
```

## API Key

The `XAI_API_KEY` is automatically injected from `skills.entries.xai-post-search.apiKey` in `~/.openclaw/openclaw.json`. You do NOT need to provide it manually.

## Notes

- Uses `grok-4-1-fast-non-reasoning` model for fast responses
- Server-side x-search tool executes automatically - no manual setup needed
- Grok handles advanced query parsing and search optimization
- Returns relevant posts with engagement metrics when available
- Requires `uv` for Python dependency management (installed automatically via brew if needed)






