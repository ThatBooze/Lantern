import json
import discord
from discord.ext import commands

# from pydactyl import PterodactylClient


with open('Lantern/Resources/configuration.json') as file:
    data = json.load(file)
    servers = data.get('SERVER_IDS', [])

with open('Lantern/Resources/localizations.json', 'r', encoding="utf-8") as f:
    localizations = json.load(f)


def get_localized_text(language, key):
    return localizations.get(language, {}).get(key, key)


async def process_command(ctx, server, command, language="en"):
    embed = discord.Embed(
        description=get_localized_text(language, "performing_action"),
        color=discord.Color.embed_background()
    )
    embed.add_field(name="", value=get_localized_text(language, "ban_response").format(server=server, command=command))
    embed.set_thumbnail(url="https://booze.d3rpp.dev/xof.gif")

    await ctx.send_response(embed=embed, ephemeral=True)


class REWRITE(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    minecraft = discord.SlashCommandGroup("minecraft")

    @minecraft.command(description=get_localized_text("en", "ban_description"))
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: discord.ApplicationContext,
                  player: discord.Option(str, required=True, description=""),
                  server: discord.Option(str="menuServer", choices=servers, description="All: * | Exempt: !"),
                  reason: discord.Option(str, description="")):
        await process_command(ctx, server, f"ban {player} {reason}")


def setup(bot):
    bot.add_cog(REWRITE(bot))
