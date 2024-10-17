import json
import discord
from discord.ext import commands

# from pydactyl import PterodactylClient


with open('Lantern/Resources/configuration.json') as file:
    data = json.load(file)
    servers = data.get('SERVER_IDS', [])


async def process_command(ctx, server, command):
    # pydapi = PterodactylClient(data.get('PTERO_URL'), data.get('PTERO_KEY'))

    embed = discord.Embed(
        description="Performing action…\nThis will be done shortly.",
        color=discord.Color.embed_background()
    )
    embed.add_field(name="", value=f"{server} | {command}")
    embed.set_thumbnail(url="https://booze.d3rpp.dev/xof.gif")

    await ctx.send_response(embed=embed, ephemeral=True)


class REWRITE(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    minecraft = discord.SlashCommandGroup("minecraft")

    @minecraft.command(description="")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: discord.ApplicationContext,
                  player: discord.Option(str, required=True, description=""),
                  server: discord.Option(str="menuServer", choices=servers, description="All: * | Exempt: !"),
                  reason: discord.Option(str, description="")):
        # TODO: Add localizations https://guide.pycord.dev/hi/interactions/application-commands/localizations
        await process_command(ctx, server, f"ban {player} {reason}")


def setup(bot):
    bot.add_cog(REWRITE(bot))
