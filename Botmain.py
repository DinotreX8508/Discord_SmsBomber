import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

Link = "https://replit.com/@yildirimlord/Sms-Bomber-for-Free#sms.py"  # Uygun bir URL ile doldurun

@Bot.command()
async def sms(ctx, user):
    await ctx.send(f"Tamamdır {Link} adresine giderek 'Run' tuşuna basarak işlemleri gerçekleştirebilirsin {user}!!")

Bot.run("MTE1MDUxMjE4NTY1MTUwMzEzNA.G5pDo6.lFhLvwUsU_d1ySot-a0Skkr5ZoL5rr-j9BjTAI")
