#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "xai-sdk>=1.3.1",
# ]
# ///
"""
Search X (Twitter) posts using XAI Grok with server-side x-search tool.
API key: XAI_API_KEY env var (injected from openclaw.json config)

Usage:
    uv run xai-search.py <search query>
"""

import os
import sys
from datetime import datetime
from xai_sdk import Client
from xai_sdk.chat import system, user
from xai_sdk.tools import x_search

def current_time():
    """Return current date and hour in a readable format: YYYY-MM-DD HHh"""
    current = datetime.now().strftime("%Y-%m-%d %Hh")
    return f"Current Time: {current}"

def main():
    query = ' '.join(sys.argv[1:])
    
    if not query:
        print('Usage: xai-search.py <search query>', file=sys.stderr)
        sys.exit(1)
    
    api_key = os.environ.get('XAI_API_KEY')
    
    if not api_key:
        print('''❌ XAI_API_KEY not set.

Configure in ~/.openclaw/openclaw.json:
{
  "skills": {
    "entries": {
      "xai-post-search": {
        "apiKey": "YOUR_XAI_API_KEY_HERE"
      }
    }
  }
}
''', file=sys.stderr)
        sys.exit(1)

    try:
        # Create client and chat with x_search tool enabled
        client = Client(api_key=api_key)
        chat = client.chat.create(
            model="grok-4-1-fast-non-reasoning", 
            tools=[x_search()],  # Enable server-side x-search tool
        )
        
        # Add system prompt
        chat.append(system(f'You are a trending X Post discovery expert specializing in finding trending Posts on X (Twitter). Your task is to find the most trending 5 X (Twitter) posts in the past 24 hours using the x-search provider tool. When given a search query, use x-search to find relevant posts. You should use advanced X search operators in your queries to retrieve better results. Return the most relevant and trending(engaging) posts you find with 1. Post Author, 2. Post Content Summary, 3. Post Engagement metrics when available. Be honest with your work and result, feedback if tool has error or result is empty.\n{current_time()}'))
        
        # Add user query
        chat.append(user(query))
        
        # Get response (server-side tools execute automatically)
        response = chat.sample()
        
        # Output the response
        print(response.content)
        
    except Exception as e:
        print(f'❌ Failed: {e}', file=sys.stderr)
        if os.environ.get('DEBUG'):
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()

