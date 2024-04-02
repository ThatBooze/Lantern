#run.py
import discord, random, json
from discord.ext import bridge

with open('Lantern/Resources/configuration.json') as file:
    data = json.load(file)

bot = bridge.Bot(command_prefix="", intents=discord.Intents.all())



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('SPLASH'))
    print(f"\033[93mSPLASH\033[0m | {bot.user} is online!")

bot.run(data["TOKEN"])