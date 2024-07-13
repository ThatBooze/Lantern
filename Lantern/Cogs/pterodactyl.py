import json
import discord
from discord.ext import commands
from pydactyl import PterodactylClient

with open('Lantern/Resources/configuration.json') as file:
    data = json.load(file)


class PTERODACTYL(commands.Cog):
    def __init__(self, bot):
        self.pydapi = PterodactylClient(data.get('PTERO_URL'), data.get('PTERO_KEY'))
        self.bot = bot

    minecraft = discord.SlashCommandGroup("minecraft")

    @minecraft.command(description="")
    @commands.has_permissions(ban_members=True)
    async def warn(self, ctx, player: str, reasoning: str):

        embed = discord.Embed(
            description="Applying changes…\nThis shouldn't take long.",
            color=discord.Color.embed_background()
        )
        embed.set_thumbnail(url="https://booze.d3rpp.dev/xof.gif")

        await ctx.reply(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(PTERODACTYL(bot))
