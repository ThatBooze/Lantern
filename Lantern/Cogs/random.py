import json
import discord
from discord.ext import commands

with open('Lantern/Resources/configuration.json') as file:
    data = json.load(file)  # TODO: Find a secure yet compact way to retrieve keys?


async def process_command(ctx, server, command):
    embed = discord.Embed(
        description="Performing action…\nThis will be done shortly.",  # TODO: Reword this.
        color=discord.Color.embed_background()
    )
    embed.add_field(name=f"{server}", value=f"```py\n{command}\n```")
    embed.set_thumbnail(url="https://placehold.co/128x128")

    await ctx.send_response(embed=embed, ephemeral=True)  # TODO: Add logic using pydactyl.


class RANDOM(commands.Cog):  # TODO: /chatdisabler enablechat <true/false>
    def __init__(self, bot):
        self.bot = bot

    minecraft = discord.SlashCommandGroup("minecraft")

    @minecraft.command()
    async def warn(self, ctx: discord.ApplicationContext,
                   player: discord.Option(str),
                   reason: discord.Option(str, required=False)):
        await process_command(ctx, "menuServer", f"warn {player} {reason}")

    @minecraft.command()
    async def kick(self, ctx: discord.ApplicationContext,
                   player: discord.Option(str),
                   reason: discord.Option(str, required=False)):
        await process_command(ctx, "menuServer", f"kick {player} {reason}")

    @minecraft.command()
    async def ban(self, ctx: discord.ApplicationContext,
                  player: discord.Option(str),
                  reason: discord.Option(str, required=False)):
        await process_command(ctx, "menuServer", f"ban {player} {reason}")

    @minecraft.command()
    async def personatus(self, ctx: discord.ApplicationContext,
                         options: discord.Option(str, choices=["1", "2", "3"]),
                         player: discord.Option(str, required=True),
                         spoofed: discord.Option(str, required=False)):
        await process_command(ctx, "menuServer", f"personatus {options} {player} {spoofed}")


def setup(bot):
    bot.add_cog(RANDOM(bot))
