import os
import json
import discord
from discord.ext import commands

with open('Lantern/Resources/configuration.json') as config:
    data = json.load(config)


def generate_choices():
    return [f[:-3] for f in os.listdir('Lantern/Resources/Tags') if f.endswith(".md")]


async def parse_markdown(ctx, selection, target):  # TODO: Add support for Webhooks.
    try:  # TODO: Simplify try statement?
        with open(f"Lantern/Resources/Tags/{selection}.md", 'r', encoding='utf-8') as markdown:
            await ctx.send_response(content=f"{target} | {markdown.read()}", ephemeral=True)

    except FileNotFoundError as e:
        print(e, flush=True)

        embed = discord.Embed(
            color=discord.Color.brand_red(),
            description="Whoops!\nFile not found."
        )
        await ctx.send_response(embed=embed, ephemeral=True)


class TAGS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def tag(self, ctx: discord.ApplicationContext,
                  selection: discord.Option(str, choices=generate_choices()),
                  target: discord.Member = None):
        await parse_markdown(ctx, selection, target)  # TODO: Write prefix command.
        # await ctx.respond(content=f"{selection} | {target}", ephemeral=(target is None or target == ctx.author))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith(f"{data.get('PREFIX')}tag"):
            await message.channel.send(f"{message.content[5:]}")


def setup(bot):
    bot.add_cog(TAGS(bot))
