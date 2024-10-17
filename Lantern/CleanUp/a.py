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
    async def warn(self, ctx, player: str, reasoning: str = None):

        embed = discord.Embed(
            type="rich",  # https://youtu.be/801VAIvdP6I
            description="Applying changes…\nThis shouldn't take long.",
            color=discord.Color.embed_background()
        )
        embed.set_thumbnail(url="https://booze.d3rpp.dev/xof.gif")

        await ctx.reply(embed=embed, ephemeral=True)

        try:
            self.pydapi.client.servers.send_console_command(
                data.get('SERVER_IDS')["menuServer"],
                f"tempwarn {player} 7d {reasoning}"
            )

            embed = discord.Embed(
                description="Changes Applied!",
                color=discord.Color.brand_green()
            )
            embed.set_thumbnail(url=f"https://starlightskins.lunareclipse.studio/render/default/{player}/bust")

            await ctx.edit(embed=embed)

        except Exception as e:
            await ctx.edit(content=e, embed=None)


def setup(bot):
    bot.add_cog(PTERODACTYL(bot))
