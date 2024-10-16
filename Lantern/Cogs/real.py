import os
import discord
from discord.ext import commands


def generate_list():
    return [f[:-3] for f in os.listdir("Lantern/Resources/Tags") if f.endswith(".md")]


async def process_markdown(ctx, selection, target):
    with open(f"Lantern/Resources/Tags/{selection}.md", 'r', encoding='utf-8') as file:
        content = file.read()
        lines = content.splitlines()
        embed = None
        text_content = []

        embed_params = {
            "title": None,
            "description": "",
            "color": None,
            "thumbnail": None,
            "image": None
        }

        for line in lines:
            if line.startswith("# "):
                embed_params["title"] = line[2:]

            elif line.startswith("!color:"):
                try:
                    embed_params["color"] = discord.Color(int(line[7:].strip(), 16))
                except ValueError:
                    pass

            elif line.startswith("!thumbnail:"):
                embed_params["thumbnail"] = line[11:].strip()

            elif line.startswith("!image:"):
                embed_params["image"] = line[7:].strip()

            elif line.startswith("!text:"):
                text_content.append(line[6:].strip())

            else:
                embed_params["description"] += line + "\n"

        if embed_params["title"] or embed_params["description"]:
            embed = discord.Embed(
                title=embed_params["title"],
                description=embed_params["description"],
                color=embed_params["color"]
            )
            if embed_params["thumbnail"]:
                embed.set_thumbnail(url=embed_params["thumbnail"])

        if embed:
            await ctx.reply(embed=embed, ephemeral=(target is None or target == ctx.author))

        if text_content:
            for text in text_content:
                await ctx.send(text, delete_after=0)


class REAL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @discord.slash_command(description="")
        async def tag(ctx: discord.ApplicationContext,
                      selection: discord.Option(str, choices=generate_list(), required=True),
                      target: discord.Member = None):
            await process_markdown(ctx, selection, target)
            # await ctx.respond(content=f"{selection} | {target}", ephemeral=(target is None or target == ctx.author))

        self.bot.add_application_command(tag)


def setup(bot):
    bot.add_cog(REAL(bot))
