import json
import discord
from discord.ext import commands
from pydactyl import PterodactylClient


with open('Lantern/Resources/configuration.json') as file:
    data = json.load(file)


async def process_command(ctx, command):
    pydapi = PterodactylClient(data.get('PTERO_URL'), data.get('PTERO_KEY'))

    embed = discord.Embed(
        description="Performing action…\nThis will be done shortly.",
        color=discord.Color.embed_background()
    )
    embed.set_thumbnail(url="https://booze.d3rpp.dev/xof.gif")

    await ctx.reply(embed=embed, ephemeral=True)

    try:  # TODO: Rewrite this try statement so it can support the other server options…
        pydapi.client.servers.send_console_command(
            data.get('SERVER_IDS')["menuServer"],
            f"{command}"
        )

        embed = discord.Embed(
            description="Action Completed!",
            color=discord.Color.brand_green()
        )

        await ctx.edit(embed=embed)

    except Exception as e:
        print(e)
        embed = discord.Embed(
            description="An error occurred while performing the action. Please try again later.",
            color=discord.Color.brand_red()
        )

        await ctx.edit(embed=embed)


class PTERODACTYL(commands.Cog):
    def __init__(self, bot):
        self.pypapi = PterodactylClient(data.get('PTERO_URL'), data.get('PTERO_KEY'))
        self.bot = bot

    minecraft = discord.SlashCommandGroup("minecraft")

    @minecraft.command(description="")
    @commands.has_permissions(ban_members=True)  # Note: This is unsecure!! Add a list of allowed guilds and roles
    async def warn(self, ctx, player: str, reasoning: str = None):
        await process_command(ctx, f"warn {player} {reasoning}")

    # TODO: Add personatus


def setup(bot):
    bot.add_cog(PTERODACTYL(bot))
