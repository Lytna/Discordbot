import discord
from discord.ext import commands
import fonk
import random


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
    await ctx.send("Merhaba discorda hoş geldiniz.")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx):
    await ctx.send(f'İyi ki geldin {ctx.author}')

@bot.command()
async def topla(ctx, s1 = 0, s2 = 0):
    await ctx.send(f"{s1}+{s2} = {s1+s2}")

@bot.command()
async def toplama(ctx,*args):
    try:
        #toplam = sum(float(arg) for arg in args)
        a = 0
        for i in args:
            a+=float(i)
        await ctx.send(f"Cevap {a}")
    except:
        await ctx.send("Sayi girmeniz lazım. ")
        
@bot.command()
async def çarp(ctx, s1 = 1, s2 = 1):
    await ctx.send(f"{s1}x{s2} = {s1*s2}")

@bot.command()
async def böl(ctx, s1 = 1, s2 = 1):
    await ctx.send(f"{s1}÷{s2} = {s1/s2}")

@bot.command()
async def çıkar(ctx, s1 = 0, s2 = 0):
    await ctx.send(f"{s1}-{s2} = {s1-s2}")
        
@bot.command()
async def olustur(ctx,s=1):
    await ctx.send(fonk.fonksiyon(s))

@bot.command()
async def oyun(ctx,a):
    if a.lower() not in ["yazı", "tura"]:
        await ctx.send("Lütfen 'yazı' veya 'tura' olarak geçerli bir tahmin yapın.")
        return 
    sonuc = "yazı" if random.randint(1, 2) == 1 else "tura"
    if a.lower() == sonuc:
        await ctx.send("Doğru tahmin")
    else:
        await ctx.send("Yanlış tahmin")

        """sonuc = ""
        if random.randint(0,1) == 0:
            sonuc = "YAZI"
        elif random.randint(0,1) == 1:
            sonuc = "TURA"   
        await ctx.send(sonuc)"""

bot.run("")
