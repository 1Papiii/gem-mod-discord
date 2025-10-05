from google import genai
from google.genai import types
from discord.ext import commands
import discord

api_key = ""
print(api_key)


# Bot setup type shiiii
intents = discord.Intents.default()
intents.message_content = True
gem_client = genai.Client(api_key=api_key)
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="/", intents=intents)

def prefix_fix(bot, message): # This is to fix a MASSIVE bug on macOS that led to me almost bricking my system (don't ask how)
    if message.channel.id != 1:
        return ""
    else:
        return "nuh uh"


# Honestly idk what any of this does
# I think it just collects a message and blah blah blah all that shit
# Blame dev.to for the horrid code :(
@bot.event
async def on_message(message):
    prefix_fix(bot, message)
    await bot.process_commands(message)
    print(message.content)
    if message.author == client.user:
        return
    else:
        response = gem_client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction="You, as an AI and moderator of a school Discord server, are to classify each message sent as NEGATIVE, POSITIVE. NEGATIVE content includes words such as 'slime', 'fuh', 'goon' and any other derogatory/offensive slang. However, simple swear words such as 'fuck' or 'shit' are allowed by technicality. Those words are POSITIVE in this case and should not be marked as NEGATIVE. If there are any links sent, treat them as 'NULL' and respond with NULL."
                ),
            contents=message.content
            )

        print(response.text)
        if response.text == "NEGATIVE":
            await message.delete()
            await message.channel.send("Message deleted. Inappropriate content detected.")
    elif response.text == "POSITIVE":
        return

bot.run('')
