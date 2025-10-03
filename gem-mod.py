from google import genai
from google.genai import types
from discord.ext import commands
from discord.ext.commands import Bot
import time
import discord
import random

keys = ["", "", "", "", "", ""]
api_key = random(keys)
#Bot setup type shiiii
#This bot doesn't use any command prefixes due to technical limitations with the GenAI SDK
intents = discord.Intents.default()
intents.message_content = True
gem_client = genai.Client()
client = discord.Client(intents=intents)
bot = commands.Bot(intents=intents)

#Honestly idk what any of this does
#I think it just collects a message and blah blah blah all that shit
#Blame dev.to for the horrid code :(
@bot.event
async def on_message(message):
    if message.author == client:
        return
    elif message.author == 1264014388021559491:
        return
    else:
        await bot.process_commands(message)
        print(message.content)
        response = gem_client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction="You, as an AI and moderator of a school Discord server, are to classify each message sent as `NEGATIVE`, `POSITIVE`. `NEGATIVE` content includes words such as 'slime', 'fuh', 'goon' and any other derogatory/offensive slang."
            ),
            contents=message.content
        )
        
        print(response.text)

bot.run('')
