import os
import discord
from discord.ext import commands


def generate_list():
    return [f[:-3] for f in os.listdir('Lantern/Resources/Tags') if f.endswith('.md')]


def read_markdown_file(filename):
    filepath = f'Lantern/Resources/Tags/{filename}.md'
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


class TAGS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @discord.slash_command(description="testing")
        async def tag(ctx: discord.ApplicationContext, selection: discord.Option(str, "", choices=generate_list(), required=True), target: discord.Member = None):

            file_content = read_markdown_file(selection)
            embed = discord.Embed(
                description=file_content,
                color=discord.Color.embed_background()
            )

            if target is None:
                await ctx.respond(embed=embed, ephemeral=True)
            else:
                await ctx.respond(content=f"{target.mention}", embed=embed)

        self.bot.add_application_command(tag)


def setup(bot):
    bot.add_cog(TAGS(bot))
