#faq.py
import discord, os
from discord.ext import commands



class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def generateList(self, ctx: discord.ApplicationContext):
        list = [file.replace(".md", "") for file in os.listdir("Lantern/Resources/Questions") if file.endswith(".md")]
        print(f"Generated List: \033[92m{list}\033[0m")
        return list

    @commands.Cog.listener()
    async def on_ready(self, ctx):
        await self.generateList()



    @discord.slash_command(description="")
    async def faq(self, ctx: discord.ApplicationContext, question: str = discord.Option(autocomplete=list)):
        await ctx.reply(question)

def setup(bot):
     bot.add_cog(FAQ(bot))