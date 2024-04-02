#faq.py
import discord, os
from discord.ext import commands



class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    #-? Generate a list of available FAQs/tags
    async def generateTags(self, ctx: discord.ApplicationContext):
        tags = [file.replace(".json", "") for file in os.listdir("Lantern/Resources/Questions") if file.endswith(".json")]
        print(f"Generated tags: \033[92m{tags}\033[0m")
        return tags



    #-? Slash Command Method (Messy !!)
    @discord.slash_command(description="")
    async def faq(self, ctx: discord.ApplicationContext, tag: str = discord.Option(autocomplete=generateTags)): #-TODO: Find a way to use choice instead of autocomplete
        await ctx.reply(tag)

def setup(bot):
    bot.add_cog(FAQ(bot))