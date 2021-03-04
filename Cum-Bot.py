import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re
import sys
from discord.ext.commands import has_permissions, CheckFailure
import requests as A_RANCIO_LE_GUSTA_LA_PIJA
import asyncio
import random
from discord import Permissions
from discord.utils import get
import requests as req

client = discord.Client()

bot = commands.Bot(command_prefix="!", case_insensitive=True)
bot.remove_command("help")

# useless things
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Version 1.6", url="http://www.twitch.tv/accountname"))
    print('alr8')

        #moderation  ======================================================================

@bot.command()
@has_permissions(ban_members=True, kick_members=True)
async def ban(ctx, user: discord.Member=None, *, reason="No reason"):
    if user == None:
        await ctx.send("Who do you want me to Cum?")
        await ctx.send("https://tenor.com/view/bo-cum-cumming-came-bo-cum-gif-18507953")
        return
    else:
        await user.ban(reason=reason)
        cum=discord.Embed(title=f"User banned: {user.name}!", description=f"Reason: {reason}\nby: {ctx.author.mention}", color=0xfafafa)
        await ctx.message.delete()
        cum.set_thumbnail(url="https://images.emojiterra.com/openmoji/v12.2/512px/1f95b.png")
        cum.add_field(name="ID:", value=user.id)
        cum.set_footer(text="Cum Bot 🥛 Rancio#9330")
        await ctx.send(embed=cum)

@bot.command()
async def unban(ctx, *, member):
     banned_users = await ctx.guild.bans()
     member_name, member_discriminator = member.split ("#")
     
     for ban_entry in banned_users:
         user = ban_entry.user
         
         if (user.name, user.discriminator) == (member_name, member_discriminator):
             await ctx.message.delete()
             await ctx.guild.unban(user)
             cum=discord.Embed(title=f"User unbaned: {member_name}#{member_discriminator}", description=f"by: {ctx.author.mention}", color=0xfafafa)
             cum.set_thumbnail(url="https://images.emojiterra.com/openmoji/v12.2/512px/1f95b.png")
             cum.add_field(name="ID:", value=user.id)
             cum.set_footer(text="Cum Bot 🥛 Rancio#9330")
             await ctx.send(embed=cum)


@bot.command(name="kick")
@has_permissions(ban_members=True, kick_members=True)
async def kick(ctx, user: discord.Member=None, *, reason="No reason provided"):
    if user == None:
        await ctx.send("Who do you want me to Kick?")
        await ctx.send("https://tenor.com/view/gatto-cibo-cat-bread-hungry-cat-gif-15925702")
        return
    else:
        await user.kick(reason=reason)
        await ctx.message.delete()
        cum=discord.Embed(title=f"User kicked: {user.name}!", description=f"Reason: {reason}\nby: {ctx.author.mention}", color=0xfafafa)
        cum.set_thumbnail(url="https://images.emojiterra.com/openmoji/v12.2/512px/1f95b.png")
        cum.add_field(name="ID:", value=user.id)
        cum.set_footer(text="Cum Bot 🥛 Rancio#9330")
        await ctx.send(embed=cum)

@bot.command(name='VerifyBot')
@has_permissions(administrator=True)
async def verifybot(ctx):
    cum=discord.Embed(title="React to be verified! :)", color=0xfafafa)
    cum.set_author(name="Verify", url="https://cdn.discordapp.com/attachments/786715742493474856/786976092446785546/cum.png", icon_url="https://cdn.discordapp.com/attachments/786715742493474856/786976092446785546/cum.png")
    cum.set_footer(text="CumBot :) - Rancio#9330")
    await ctx.send(embed=cum)

@bot.command(pass_context=True)
@has_permissions(ban_members=True, kick_members=True)
async def clear(ctx, amount=0,):
    channel = ctx.message.channel
    messages = []
    if amount == 0:
       cum=discord.Embed(description="**Choose a number:** 1-100" , color=0xfafafa) 
       cum.set_footer(text="Cum Bot 🥛 Rancio#9330")
       await ctx.send(embed=cum)
       await ctx.message.delete() 
       return
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)
    cum=discord.Embed(title="Clear" , color=0xfafafa)
    cum.set_author(name=ctx.author.display_name, url="https://images.emojiterra.com/openmoji/v12.2/512px/1f95b.png", icon_url=ctx.author.avatar_url)
    cum.set_thumbnail(url="https://images.emojiterra.com/openmoji/v12.2/512px/1f95b.png")
    cum.add_field(name="Messages cleared successfully", value=f"Messages deleted: **{amount}**" , inline=False)
    cum.set_footer(text="Cum Bot 🥛 Rancio#9330")
    await ctx.send(embed=cum)

@bot.command()
async def phone(ctx, *,phone=None):
    if phone==None:
        await ctx.message.channel.send("escribi el numero cabeza")
        return
    phone=phone.replace("-", "").replace(",", "").strip()
    phone=req.get("http://apilayer.net/api/validate?access_key=3cdc7d946faa9e4ad32b57efdde98c8d&number=" + phone +"&format=1")
    cum = discord.Embed(title='', color=0xfafafa, description="\n\n**Number Lookup**\n" + str(str(phone.text).replace("\"", " ").replace("{", " ").replace("}", " "))) 
    cum.set_footer(text="CumBot - Rancio#9330")
    await ctx.channel.send(embed=cum)

#moderation  ======================================================================

#======== COSAS RE CUALQUIERAS  ============#

@bot.command()
async def culoblusted(ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/787004723302498343/787471362129526784/image0.png')

@bot.command()
@has_permissions(administrator=True)
async def infomessage(ctx):
    await ctx.message.delete() 
    cum=discord.Embed(title="", url="https://images.emojiterra.com/openmoji/v12.2/512px/1f95b.png", color=0xfafafa)
    cum.set_author(name="Mensaje para la gente de SnakeSilent discord", url="https://cdn.discordapp.com/attachments/786715742493474856/786976092446785546/cum.png", icon_url="https://cdn.discordapp.com/attachments/786715742493474856/786976092446785546/cum.png")
    cum.set_thumbnail(url="https://images.emojiterra.com/openmoji/v12.2/512px/1f95b.png")
    cum.add_field(name="Actualmente el discord de zsnake ha sido cumeado", value=":)", inline=True)
    cum.add_field(name="Autores:", value="Ravager, Pyhro & Rancio", inline=False)
    cum.add_field(name="Razones:", value="Snake es un pelotudo, se cree la gran cosa por solamente bypassear con 32 bits a un trial-mod, no es la gran cosa si se ponen a pensar.", inline=False)
    cum.add_field(name="Que ganamos:", value="Hacer mierda a un creido ngl", inline=False)
    cum.add_field(name="Hacia los servidores que snake les hizo algo:", value="Denada por cumearlo", inline=False)
    cum.set_footer(text="#CanadianMafia - Rancio#9330")
    await ctx.send(embed=cum)

@bot.command()
async def cum(ctx):
        await ctx.send('https://tenor.com/view/why-do-you-cum-cum-cyberpunk-gif-19751361') 

@bot.command()
async def gatoalqueleavientanunpitote(ctx):
        await ctx.send('https://tenor.com/view/gatto-cibo-cat-bread-hungry-cat-gif-15925702') 

@bot.command()
async def developers(ctx):
    cumg=discord.Embed(title="", url="https://instagram.com/edher_uwu", color=0xfafafa)
    cumg.set_author(name="Developer Info (Glory)", url="https://www.instagram.com/edher_uwu/", icon_url="https://cdn.discordapp.com/attachments/787004723483770886/795441233044439050/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f.jpeg")
    cumg.set_thumbnail(url="https://cdn.discordapp.com/attachments/787004723483770886/795441233044439050/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f.jpeg")
    cumg.add_field(name="Name:", value="Glory", inline=False)
    cumg.add_field(name="Contact:", value="change this, https://t.me/GloryV3, Glory#0027, https://twitter.com/psykhe25061664", inline=False)
    cumg.add_field(name="Snapchat:", value="https://snapchat.com/gloryuwu", inline=False)
    cumg.add_field(name="Lenguage Knowledge:", value="HTML & css", inline=False)
    cumg.set_footer(text="CumBot Developer Info - Glory#0027")
    await ctx.send(embed=cumg)
    cumr=discord.Embed(title="", url="https://www.instagram.com/lgog15/", color=0xfafafa)
    cumr.set_author(name="Developer Info (Lucas)", url="https://www.instagram.com/lgog15/", icon_url="https://cdn.discordapp.com/attachments/791149140817739786/795426503072022568/Pinguino2.png")
    cumr.set_thumbnail(url="https://cdn.discordapp.com/attachments/791149140817739786/795426503072022568/Pinguino2.png")
    cumr.add_field(name="Name:", value="Lucas", inline=False)
    cumr.add_field(name="Contact:", value="+54 9 11 3408-2328, https://t.me/Rancio777, Rancio#9330, https://twitter.com/Rancio777", inline=False)
    cumr.add_field(name="Instagram:", value="https://www.instagram.com/lgog15/", inline=False)
    cumr.add_field(name="Lenguage Knowledge:", value="Python :(", inline=False)
    cumr.set_footer(text="CumBot Developer Info - Rancio#9330")
    await ctx.send(embed=cumr)

@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send("Avatar:")
    await ctx.send(userAvatarUrl)
        


#======== COSAS RE CUALQUIERAS  ============#

#======== non relevant things ============#



@client.event
async def on_message(message):
    if message.content.find('!ip') != -1:
        if str(message.content) == '!ip':
            canal = client.get_channel(message.channel.id)
            await canal.send("put an ip adress")
        else:
            canal = client.get_channel(message.channel.id)
            try:
                #--- general 
                ip = message.content.replace("!ip ", "") #get ip 
                urls="http://extreme-ip-lookup.com/json/"+ str(ip) # add ip in url
                ipinfo = A_RANCIO_LE_GUSTA_LA_PIJA.get(urls)#request api
                
                cum = discord.Embed(title='', color=0xfafafa, description="\n\n**IP Lookup**\n" + str(str(ipinfo.text).replace("\"", "").replace("{", "").replace("}", ""))) 
                cum.set_footer(text="CumBot 🥛 Mr20cps#5607 - Cum for " + str(ip))
                await canal.send(embed=cum)
            except:
                pass
                

@bot.command(name="say")
async def say(ctx, *, something):
    """say something!"""
    if something == None:
        await ctx.send("Usage: !say (Word)")
        return
    if something == "@everyone":
        await ctx.send("Dont tag everyone :(")
        return
    if something == "@here":
        await ctx.send("Dont tag here :(")
        return
    await ctx.message.delete()    
    await ctx.send(f"**{something}**")


@bot.command(name="whois")
async def whois(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    cum = discord.Embed(timestamp=ctx.message.created_at, title=f"User Info - {member}",  color=0xfafafa)
    cum.set_thumbnail(url=member.avatar_url)
    cum.set_footer(text=f"Requested by {ctx.author}")

    cum.add_field(name="ID:", value=member.id)
    cum.add_field(name="Display Name:", value=member.display_name)

    cum.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    cum.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    cum.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=cum)

#======== non relevant things ============#
# 
#======== help commands ============#  

@bot.command(name='commands')
async def commands(ctx):
    await ctx.message.delete() 
    cum=discord.Embed(title="Cum-bot command list :)", url="https://images.emojiterra.com/openmoji/v12.2/512px/1f95b.png", color=0xfafafa)
    cum.set_thumbnail(url="https://images.emojiterra.com/openmoji/v12.2/512px/1f95b.png")
    cum.add_field(name="!sinfo", value="Shows server info", inline=True)
    cum.add_field(name="!youtube", value="Search, play & reveal info for your search", inline=False)
    cum.add_field(name="!dev", value="Shows developer information and contact", inline=False)
    cum.add_field(name="!ban", value="Ban a guy", inline=False)
    cum.add_field(name="!unban", value="Unban a guy", inline=False)
    cum.add_field(name="!mute", value="Mute a guy", inline=False)
    cum.add_field(name="!unmute", value="Unmute a guy", inline=False)
    cum.add_field(name="!ip", value="Actually shows ip non-private info", inline=False)
    cum.add_field(name="!phone ", value="Reveal phone Non-relevant info", inline=False)
    cum.add_field(name="!clear", value="Purge an number of messages **1-100**", inline=False)
    cum.add_field(name="!rrole", value="Config ur own rainbow role", inline=False)
    cum.add_field(name="!say", value="Say everything you want :)", inline=False)
    cum.add_field(name="!whois ", value="Reveal user non-relevant info", inline=False)
    cum.add_field(name="!bping ", value="Bot Ping ", inline=False)
    cum.add_field(name="!bsv ", value="Server List", inline=False)
    cum.add_field(name="!snipe ", value="Resend the last deleted message", inline=False)
    cum.set_footer(text="Cum Bot :) 🥛 Rancio#9330")
    await ctx.send(embed=cum)
    
@bot.command(name='help')
async def help(ctx):
    await ctx.message.delete() 
    cum=discord.Embed(title="Cum-Bot Support zone", url="https://images.emojiterra.com/openmoji/v12.2/512px/1f95b.png", color=0xfafafa)
    cum.set_thumbnail(url="https://images.emojiterra.com/openmoji/v12.2/512px/1f95b.png")
    cum.add_field(name="Support", value="You can open a ticket in the ticket-channel to get support.", inline=True)
    cum.add_field(name="Information", value="You can get it on the #Information channel.", inline=False)
    cum.add_field(name="Where i view the bot updates?", value="in #changelog channel", inline=False)
    cum.add_field(name="Invite!", value="[Click here for invite me](https://discord.com/oauth2/authorize?client_id=785939793179443200&permissions=8&scope=bot)", inline=False)
    cum.set_footer(text="Cum Bot :) 🥛 Rancio#9330")
    await ctx.send(embed=cum)
    

@bot.command()
async def bping(ctx):
    
	latency = bot.latency
	cum=discord.Embed(title="CumBot" , color=0xfafafa)
	cum.add_field(name="Ping:", value=f"{bot.latency}", inline=False)
	await ctx.send(embed=cum)



@bot.command()
async def bsv(ctx):

	servers_on = bot.guilds
	cum=discord.Embed(title="CumBot" , color=0xfafafa)
	cum.add_field(name="Server list", value=f"{bot.guilds}", inline=False)
	await ctx.send(embed=cum)

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@bot.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.name
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None

@bot.command()
async def snipe(message):
    if snipe_message_content==None:
        await message.channel.send("**Theres nothing to snipe.**")
    else:
        cum=discord.Embed(title="Message Snipe" , color=0xfafafa)
        cum.add_field(name=f"{snipe_message_content}", value=":)", inline=True)
        cum.set_footer(text=f"Sniped by: {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
        cum.set_author(name= f"{snipe_message_author}")
        await message.channel.send(embed=cum)
        return



bot.run("ur token")
