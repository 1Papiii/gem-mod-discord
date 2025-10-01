from google import genai
from google.genai import types
from discordwebhook import Discord as hook
import random

# API key randomizer (bc im broke) and chat setup
keys = ["", "", "", "", "", "", "", "", "", ""]
api_key = random(keys)
