import discord
from discord.ext import commands
import os, random
import requests
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def cevre(ctx):
    print("Merhaba! Ben cevre botu. Cevreyi korumak icin calisiyorum.")
    print("Insanlar yere cop attigindan dolayi dunyamiz kirleniyor. Insanlara cevre kirliligini ogretmek icin insanlara bazi fotograflar buldum. Bakmak istersen $cevre yazip gorebilirsin!.")
    img_name = random.choice(os.listdir('cevreresim'))
    with open(f'cevreresim/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)


bot.run("MTM2MTM4MzUyMDI5MDg2OTI3OA.GwUh1k.jMJcHA6FBvmT0ylHZH8e_D0iCEBG8_QC7Va74s")
