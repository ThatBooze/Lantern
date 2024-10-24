import json
import random
import discord
from discord.ext import commands


with open("Lantern/Resources/configuration.json") as file:
    data = json.load(file)

with open("Lantern/Resources/splashes.txt", "r", encoding="utf-8") as s:
    SPLASH = random.choice(s.readlines()).strip()

bot = commands.Bot(command_prefix="", intents=discord.Intents.all())

cogs_list = [
    "random",
    "tags"
]

for cog in cogs_list:
    try:
        bot.load_extension(f"Cogs.{cog}")
        print(f"Loaded Cogs.\033[92m{cog}\033[0m")
    except Exception as e:
        print(f"Failed to load Cogs.\033[91m{cog}\033[0m: {e}")


@bot.event
async def on_message(message):
    if message.author.bot or message.webhook_id:
        await bot.process_commands(message)
    else:
        pass


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(SPLASH))
    print(f"\033[93m{SPLASH}\033[0m | {bot.user.name} is online!")


bot.run(data["TOKEN"])
