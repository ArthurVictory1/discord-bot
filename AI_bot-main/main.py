import discord
from discord.ext import commands
from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('hello')
async def hello(ctx):
    await ctx.send("Привет мир")


@bot.command('duck')
async def duck(ctx):
    '''По команде duck возвращает фото утки'''
    print('hello')
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command("check")
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Вы забыли загрузить картинку :(")


@bot.command("info")
async def info(ctx):
    await ctx.send("Интересный факт про глобальное потепление: В октябре 2018 года МГЭИК опубликовала Специальный доклад о глобальном потеплении на 1,5 °C. В докладе освещается ряд последствий изменения климата, которых можно было бы избежать, ограничив глобальное потепление 1,5 °C по сравнению с 2 °C, или более того. Например, к 2100 году глобальное повышение уровня моря будет на 10 см ниже при глобальном потеплении на 1,5 °C по сравнению с 2 °C. По оценкам, при глобальном потеплении на 1,5 °C Северный Ледовитый океан был бы свободен летом от морского льда один раз в столетие, а в случае потепления на 2 °C — один раз в десятилетие. Количество коралловых рифов сократится на 70—90 процентов при глобальном потеплении на 1,5 °C, тогда как практически все они (> 99 процентов) будут утрачены при потеплении на 2 °C.")
    

bot.run('MTE5ODU1OTIyNTA1MjQxODIxMQ.GBq20T.hXPslqRC1hGUulzKQsne31fOwY2DrAusx9vyAg')