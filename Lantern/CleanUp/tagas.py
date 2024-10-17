import os
import discord
from discord.ext import commands


def generate_list():
    return [f[:-3] for f in os.listdir('Lantern/Resources/Tags') if f.endswith('.md')]


class TAGS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @discord.slash_command(description="")
        async def tag(ctx: discord.ApplicationContext,
                      selection: discord.Option(str, choices=generate_list(), required=True),
                      target: discord.Member = None):
            await ctx.respond(content=f"{selection} | {target}", ephemeral=(target is None or target == ctx.author))

        self.bot.add_application_command(tag)  # TODO: Rewrite everything again as the old code was off


def setup(bot):
    bot.add_cog(TAGS(bot))
