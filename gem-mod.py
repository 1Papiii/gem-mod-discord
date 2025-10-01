from google import genai
from google.genai import types
from discordwebhook import Discord as hook
import random

# API key randomizer (bc im broke) and chat setup
# No keys are provided in this repo
# NEVER share your API key with ANYONE
keys = ["", "", "", "", "", "", "", "", "", ""]
api_key = random(keys)

# Initialize client and chat ONLY if an API key is available
try:
    client = genai.Client(api_key=api_key)
    chat = client.chats.create(model="gemini-2.5-flash")
except Exception as e:
    print(f"Failed to initialize Gemini client or chat: {e}")
    print("Please check your API key and try again. Exiting.")
    time.sleep(1)
    exit()
