# gem-mod-discord
A Discord bot that uses Google Gemini to moderate your server.

# Requirements
* [Discord.py SDK](https://pypi.org/project/discord.py/)
* [Discord Developer account](https://discord.com/developers/applications)
* [Google GenAI SDK](https://pypi.org/project/google-genai/)
* [Python 3.5+](https://python.org)
* A server (for running the script) The server I am running this implementation is a Hackintosh, but it can realistically be anything with Python on it.

# How it works
Messages are routed from Discord to Google Gemini. Gemini classifies those messages and takes action accordingly. Simple, right?

# Limitations
Python is slow asf. Rate limits and quota limits on Google's end exist. Keys may be banned if anything explicit is sent. I have no clue what I am doing (still not vibe coded tho).
