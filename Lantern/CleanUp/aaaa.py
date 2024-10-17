import json
import discord
from discord.ext import commands
from pydactyl import PterodactylClient

with open('Lantern/Resources/configuration.json') as file:
    data = json.load(file)


async def process_command(ctx, server, command):
    pydapi = PterodactylClient(data.get('PTERO_URL'), data.get('PTERO_KEY'))

    embed = discord.Embed(
        description="Executing command…\nThis will take a few moments.",
        color=discord.Color.embed_background()
    )
    embed.set_thumbnail(url="https://booze.d3rpp.dev/xof.gif")

    await ctx.respond(embed=embed, ephemeral=True)

    try:
        if server == "*":
            print('Selected all servers.')
        elif server.startswith("!"):
            print('Exempted all servers EXCEPT ' + server[1:])
        else:
            print('Selected a single server.')
        # You should perform the actual command here
        # Example: pydapi.client.send_console_command(...)
    except Exception as e:
        print(e)
        error_embed = discord.Embed(
            description="An error occurred while performing the action. Please try again later.",
            color=discord.Color.brand_red()
        )

        await ctx.edit_message(embed=error_embed)


class PTERODACTYL(commands.Cog):
    def __init__(self, bot):
        self.pypapi = PterodactylClient(data.get('PTERO_URL'), data.get('PTERO_KEY'))
        self.servers = data.get('SERVER_IDS')
        self.bot = bot

    minecraft = discord.SlashCommandGroup("minecraft")

    @minecraft.command(description="Warn a player with a specified reason")
    async def warn(ctx: discord.ApplicationContext,
                   player: str,
                   reasoning: str = None,
                   server: discord.Option(str, choices=["a,b"], required=False)):
        await process_command(ctx, server, f"warn {player} {reasoning}")


def setup(bot):
    bot.add_cog(PTERODACTYL(bot))
