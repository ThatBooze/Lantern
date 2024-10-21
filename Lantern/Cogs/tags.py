import os
import discord
from discord.ext import commands


def generate_list():
    return [f[:-3] for f in os.listdir('Lantern/Resources/Tags') if f.endswith(".md")]


class TAGS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def tag(self, ctx: discord.ApplicationContext,
                  selection: discord.Option(str, choices=generate_list()),
                  target: discord.Member = None):
        await ctx.respond(content=f"{selection} | {target}", ephemeral=(target is None or target == ctx.author))


def setup(bot):
    bot.add_cog(TAGS(bot))
