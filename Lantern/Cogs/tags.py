import os
import discord
from discord.ext import commands


def generate_list():
    return [f[:-3] for f in os.listdir('Lantern/Resources/Tags') if f.endswith('.md')]


class TAGS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @discord.slash_command(description="testing")
        async def tag(
                ctx: discord.ApplicationContext,
                selection: discord.Option(str, "", choices=generate_list(), required=True),
                target: discord.Member = None):

            if target is None:
                await ctx.respond(content="You did not include a target, which is fine.", ephemeral=True)
            else:
                await ctx.respond(content=f"You did include a target! Hi {target.mention}. {selection}")

        self.bot.add_application_command(tag)


def setup(bot):
    bot.add_cog(TAGS(bot))
