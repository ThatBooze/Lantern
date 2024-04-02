#run.py
import discord, random, json
from discord.ext import bridge, commands

with open("Lantern/Resources/configuration.json") as file:
    data = json.load(file)

with open("Lantern/Resources/splashes.txt", "r", encoding="utf-8") as s:
    SPLASH = random.choice(s.readlines()).strip()

bot = bridge.Bot(command_prefix="", intents=discord.Intents.all()) #-NOTE: command_prefix is blank on purpose !!



cogs_list = [
    "faq"
    #-! Add more here
]

for cog in cogs_list:
    bot.load_extension(f"Cogs.{cog}")
    print(f"Loaded Cogs.\033[92m{cog}\033[0m")



#-? Shushes discord.ext.commands.errors.CommandNotFound
@bot.event
async def on_message(message):
    if message.author.bot or message.webhook_id:
        await bot.process_commands(message)
    else:
        pass

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(SPLASH))
    print(f"\033[93m{SPLASH}\033[0m | {bot.user} is online!")

bot.run(data["TOKEN"])