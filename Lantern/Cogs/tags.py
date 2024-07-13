import discord
from discord.ext import commands


class TAGS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="")
    async def tag(self, ctx, target: discord.Member = None):
        if target is None:
            await ctx.reply(content="You did not include a target, which is fine.", ephemeral=True)
        else:
            await ctx.reply(content=f"Did include a target! hii {target.mention}")


def setup(bot):
    bot.add_cog(TAGS(bot))
