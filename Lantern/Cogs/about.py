import discord
from discord.ext import commands



class ABOUT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(description="")
    async def about(self, ctx):
        await ctx.reply('Nothing much, this was a test command lol. For actual Infomation, check out my profile')

def setup(bot):
    bot.add_cog(ABOUT(bot))