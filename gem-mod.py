from google import genai
from google.genai import types
from discordwebhook import Discord as hook
import random

# API key randomizer (bc im broke) and chat setup
# No keys are provided in this repo
# NEVER share your API key with ANYONE
keys = ["", "", "", "", "", "", "", "", "", ""]
api_key = random(keys)

# Bot setup type shiiii
# This bot doesn't use any command prefixes due to technical limitations with the GenAI SDK
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)

# Honestly idk what any of this does
# I think it just collects a message and blah blah blah all that shit
# Blame dev.to for the horrid code :(
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    print(message.content)

# The blank space is your token
# NEVER leave your token out kids
bot.run('')
