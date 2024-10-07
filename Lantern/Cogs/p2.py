import json
import discord
from discord.ext import commands
from pydactyl import PterodactylClient


with open('Lantern/Resources/configuration.json') as file:
    data = json.load(file)


async def process_command(ctx, command):
    embed = discord.Embed(
        description="Applying changes…\nThis shouldn't take long.",
        color=discord.Color.embed_background()
    )
    embed.set_thumbnail(url="https://booze.d3rpp.dev/xof.gif")

    await ctx.reply(embed=embed, ephemeral=True)

    try:
        print(
            data.get('SERVER_IDS')["menuServer"],
            f"{command}"
        )

        embed = discord.Embed(
            description="Changes Applied!",
            color=discord.Color.brand_green()
        )

        await ctx.edit(embed=embed)

    except Exception as e:
        print(e)
        embed = discord.Embed(
            description="An error occurred while processing your request. Please try again later",
            color=discord.Color.brand_red()
        )

        await ctx.edit(embed=embed)


class P2(commands.Cog):
    def __init__(self, bot):
        self.pydapi = PterodactylClient(data.get('PTERO_URL'), data.get('PTERO_KEY'))
        self.bot = bot

    minecraft = discord.SlashCommandGroup("minecraft")

    @minecraft.command(description="")
    @commands.has_permissions(ban_members=True)
    async def warn(self, ctx, player: str, reasoning: str = None):
        await process_command(ctx, f"warn {player} {reasoning}")


def setup(bot):
    bot.add_cog(P2(bot))
