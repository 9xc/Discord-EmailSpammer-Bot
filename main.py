import discord
from discord.ext import commands
import time
import asyncio
import smtplib
import datetime
from configparser import ConfigParser
import os
import sys
from colorama import Fore, init
init(convert=True)
os.system("title EmailSpammer!")
config = ConfigParser()

config.read('cfg.ini')

emale = config.get('SETTINGS', 'email')
pas = config.get('SETTINGS', 'password')
token = config.get('SETTINGS', 'bottoken')

def type(words):
    words
    for char in words:
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)


bot = commands.Bot(command_prefix='!', description="peepee")
bot.remove_command("help")
@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Streaming(name="egirlraper on github", url="https://www.twitch.tv/egirlraper"))
    type(f""""{Fore.RED}
    ███████╗███╗   ███╗ █████╗ ██╗██╗         
    ██╔════╝████╗ ████║██╔══██╗██║██║         
    █████╗  ██╔████╔██║███████║██║██║         
    ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         
    ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    
    ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    
                                              
    ███████╗██████╗  █████╗ ███╗   ███╗██╗    
    ██╔════╝██╔══██╗██╔══██╗████╗ ████║██║    
    ███████╗██████╔╝███████║██╔████╔██║██║    
    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║╚═╝    
    ███████║██║     ██║  ██║██║ ╚═╝ ██║██╗    
    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝    
                                             
""")
count = 10
#penusssss
@bot.command()
async def email(ctx,count=None,bomb_email=None,*,message=None):
    if count == None or bomb_email == None or message == None:
        await ctx.send("Format - !email [count] [email] [message] - e.g !email 10 test@gmail.com LoL!")
    else:
        x = int(count)
    if x > 50:
        await ctx.send("`That's too much. Do 50 or less!`")
    else:
        currentDT = datetime.datetime.now()
        hour = str(currentDT.hour)
        minute = str(currentDT.minute)
        second = str(currentDT.second)
        print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} [Command used] - {ctx.author.name}#{ctx.author.discriminator}:{Fore.RESET} !email {count} {bomb_email} {message}")
        counting = int(0)
        embed=discord.Embed(title=f"{counting}/{count}", url="https://github.com/egirlraper", color=0xff0000)
        embed.set_author(name="Email sent!", url="https://github.com/egirlraper")
        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
        embed.add_field(name=f'Sending "{message}"', value=f'**to {bomb_email}**', inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        msg = await ctx.send(embed=embed)
        for i in range(x):
            mail = smtplib.SMTP('smtp.gmail.com',587) #you can put whatever smtp you wanna use
            mail.ehlo()
            mail.starttls()
            mail.login(emale,pas)
            mail.sendmail(emale,bomb_email,message)
            mail.close() 
            currentDT = datetime.datetime.now()
            hour = str(currentDT.hour)
            minute = str(currentDT.minute)
            second = str(currentDT.second)
            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Message Sent:{Fore.RESET} {message} {Fore.GREEN}To {Fore.RESET}{bomb_email}")
            counting = counting + 1
            embed=discord.Embed(title=f"{counting}/{count}", url="https://github.com/egirlraper", color=0xff0000)
            embed.set_author(name="Email sent!", url="https://github.com/egirlraper")
            embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
            embed.add_field(name=f'Sending "{message}"', value=f'**to {bomb_email}**', inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
            await msg.edit(embed=embed)
        embed=discord.Embed(title="Please consider following!", url="https://github.com/egirlraper", color=0xff0000)
        embed.set_author(name="Done spamming!", url="https://github.com/egirlraper")
        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
        await msg.edit(embed=embed)



bot.run(token)