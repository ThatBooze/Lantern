import discord
from discord.ext import commands
import os


# TODO: Rewrite everything.

class Tags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tags_dir = 'Lantern/Resources/Tags/'  # Directory where markdown files are stored

    @commands.slash_command(name="tag", description="Read and display a markdown tag.")
    async def tag(self, ctx, tag_name: str):
        await self.display_tag(ctx, tag_name)

    async def display_tag(self, ctx, tag_name: str):
        file_path = os.path.join(self.tags_dir, f"{tag_name}.md")

        if not os.path.exists(file_path):
            await ctx.reply(f"Tag `{tag_name}` not found.", ephemeral=True)
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        await self.process_md_content(ctx, content)

    async def process_md_content(self, ctx, content: str):
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
                    pass  # Invalid color code; ignore it.

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
            if embed_params["image"]:
                embed.set_image(url=embed_params["image"])

        # Send plain text messages first
        if text_content:
            for text in text_content:
                await ctx.send(text)

        # Send the embed message if it exists
        if embed:
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Tags(bot))
