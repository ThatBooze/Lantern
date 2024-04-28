#faq.py
import discord, json, os
from discord.ext import commands

with open('Lantern/Resources/configuration.json') as file:
    data = json.load(file)



class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    #-? Generate a list of available FAQs/tags
    async def generateTags(self, ctx: discord.ApplicationContext): #-TODO: Add a cooldown to this function to prevent spamming and just use a cached table 
        try: #-? Making sure nothing explodes!!
            tags = [file.replace(".json", "") for file in os.listdir("Lantern/Resources/Questions") if file.endswith(".json")]
            print(f"Generated tags: \033[92m{tags}\033[0m : faq.py")
            return tags
        except Exception as e:
            print(f"\033[91m[ERROR]\033[0m An error occurred while generating tags: {e} : faq.py")
            return None



    #-? Slash Command Method (Messy !!)
    @discord.slash_command(description="")
    async def faq(self, ctx: discord.ApplicationContext, tag: str = discord.Option(autocomplete=generateTags)): #-TODO: Find a way to use choice instead of autocomplete
        file_path = f"Lantern/Resources/Questions/{tag}.json"

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                tag = json.load(file)

                #-? Embed (for Discord)
                if "embed" in tag:
                    embed = discord.Embed(
                        colour = int(tag["embed"][0].get("colour", "0xffffff"), 16)
                    )
                    embed.add_field(name=tag["embed"][0].get("name", ""), value=tag["embed"][0].get("value", ""))
                
                if "delete_after" in tag["embed"][0]:
                    await ctx.reply(embed=embed, delete_after=tag["embed"][0]["delete_after"], silent=True)
                else:
                    await ctx.reply(embed=embed)



                #-? Message (for Minecraft)
                if "message" in tag:
                    if "delete_after" in tag["message"][0]:
                        await ctx.reply(tag["message"][0]["message"], delete_after=tag["message"][0]["delete_after"], silent=True)
                    else:
                        await ctx.reply(tag["message"][0]["message"])
        else:
            print(f"\033[91m[ERROR]\033[0m File not Found: {tag}.json : faq.py")
    


    #-? Prefixed Command Method (eww, outdated way)
    @commands.Cog.listener()
    async def on_message(self, message):
        prefix = data["PREFIX"]

        if message.author == self.bot.user:
            return

def setup(bot):
    bot.add_cog(FAQ(bot))