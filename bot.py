import discord
from discord import member
from discord.ext import commands
from discord.ext.commands import has_permissions

    
intents = discord.Intents.all()




client = commands.Bot(command_prefix= "!", intents=intents)
client.remove_command("help")

@client.event
async def on_member_join(member):
    guild = client.get_guild(889882238953598987) 
    welcome_channel = guild.get_channel(909375008663552050)  
    embed=discord.Embed(title="Witaj", description=f"**{member.mention} mam nadzieje że będziesz się dobrze bawił**", color=0x009dff)
    embed.set_author(name="MuziClicker",          icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="MuziClicker")
    await welcome_channel.send(embed=embed)
    await member.send(f'Witaj na serverze MuziClicker {member.mention}  mamy nadzieje że dobrze bendziesz się bawił!')



@client.event
async def on_member_remove(member):
    guild = client.get_guild(889882238953598987) 
    goodbye_channels = guild.get_channel(909375008663552050)  
    embed=discord.Embed(title="Żegnaj", description=f"**Mamy nadzieje że wrócisz {member.mention} **", color=0xd21959)
    embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="MuziClicker")
    await goodbye_channels.send(embed=embed)


@client.event
async def on_ready():   
    print("online")







@client.command()
async def pomoc(ctx):
  embed=discord.Embed(title="Pomoc", color=0x046dbe)
  embed.set_author(name="MuziClicker",  icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
  embed.add_field(name="!Clicker", value="opcje clicker", inline=False)
  embed.add_field(name="!Cenik", value="Cenik żeczy", inline=False)
  embed.set_footer(text="MuziClicker")
  await ctx.send(embed=embed)



@client.command()
async def graj(ctx, game):
    await client.change_presence(activity=discord.Game(name=game))



@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason="Bez Powodu"):
    await member.send(f'{member.mention} Zostałeś zbanowany na serverze **MuziClicker** za {reason} !')
    await member.ban(reason=reason)
    embed=discord.Embed(title="**Pomyślnie Zbanowano!**", description=f"**Użytkownik {member.mention} został zbanowany za {reason}**", color=0xfa009e)
    embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_thumbnail(url=member.avatar_url) 
    embed.set_footer(text="MuziClicker")
    await ctx.send(embed=embed)
    await ctx.guild.ban(member)
    







@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, reason="Bez Powodu"):
    await member.send(f'{member.meniton} Zostałeś wyrzucony na serverze **MuziClicker** za {reason} !')
    await member.kick(reason=reason)
    embed=discord.Embed(title="**Pomyślnie Wyrzucono!**", description=f"**Użytkownik {member.mention} został wyrzucony za {reason}**", color=0xfa009e)
    embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="MuziClicker")
    await ctx.send(embed=embed) 
    await ctx.guild.kick(member) 
    




@client.command(aliases=['ub'])
@has_permissions(ban_members=True)
async def unban(ctx, member: discord.User):
    embed=discord.Embed(title="**Pomyślnie Odbanowano!**", description=f"**Użytkownik {member.mention} został odbanowany na serwerze!**", color=0x00ff99)
    embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="MuziClicker")
    await ctx.send(embed=embed)
    await ctx.guild.unban(member)
    
   


@client.command()
async def Clicker(ctx):
    embed=discord.Embed(title="MuziClikcer", color=0xfa009e)
    embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.add_field(name="Macro", value="LPM/PPM", inline=True)
    embed.add_field(name="Klepa", value="Zmiana Seta/altowanie/wyrzucanie itemów", inline=True)
    embed.add_field(name="Kopanie", value="Wkróce ", inline=True)
    embed.add_field(name="Ustawienia", value="Profil Ustawień", inline=True)
    embed.set_footer(text="MuziClicker")
    await ctx.send(embed=embed)



@client.command()
async def v(ctx):
    embed=discord.Embed(title="**Weryfikacja**", description=f"**ABY SIĘ ZWERYFKOWAĆ KLIKNIJ REAKCJE**", color=0x14c81a)
    embed.set_author(name="MuziClikcer", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_footer(text="MuziClicker")
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("✅")

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 909053647621599242:
        if payload.emoji.name == '✅': 
            guild = client.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            rola = discord.utils.get(guild.roles, id=889882239071027204)
            await member.add_roles(rola)

@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 909053647621599242:
        if payload.emoji.name == "✅": 
            guild = client.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            rola = discord.utils.get(guild.roles, id=889882239071027204)
            await member.remove_roles(rola) 


@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000, 1)
    embed=discord.Embed(title="**Ping** ", description=f"**MuziClicker - {latency}ms**")
    embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_footer(text="MuziClicker")
    await ctx.send(embed=embed)



@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason="Bez Powodu"):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    await member.add_roles(mutedRole, reason=reason)
    embed=discord.Embed(title="**Pomyślnie zmutowano** ", description=f"**Użytkownik {member.mention} został zmutowany za {reason}**")
    embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png") 
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)
    await member.send(f'Zostałeś zmutowany na serverze **MuziClicker** za {reason} !')


@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(mutedRole)
    embed=discord.Embed(title="**Pomyślnie Odmutowano** ", description=f"**Odmutowano Użytkownika {member.mention}**")
    embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)
    await member.send(f'Zostałeś odmutowany na serverze **MuziClicker** !')  




@client.command()
@has_permissions(administrator=True)
async def clear(ctx, a=5):
    a = int(a)
    await ctx.channel.purge(limit=a)
    embed=discord.Embed(title="**Pomyślnie Wyczyszczono**", description=f"**Wyczyszczono wiadomości**")
    embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
    embed.set_footer(text="MuziClicker")
    await ctx.send(embed=embed)
     


@client.command()
async def a(ctx):
  embed=discord.Embed(title="Ogłoszenie", description="**Naprawiliśmy weryfikacje dzięki frimc#5468 wielkie podziękowania dla nie go**", color=0x046dbe)
  embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
  embed.set_footer(text="MuziClicker")
  await ctx.send(embed=embed)

@client.command()
async def Cenik(ctx):
  embed=discord.Embed(title="Cenik", color=0x046dbe)
  embed.set_author(name="MuziClicker",  icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
  embed.set_thumbnail       (url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
  embed.add_field(name="Autorski Bot Discord - 10zł psc,paypal", value="bot discord", inline=False)
  embed.add_field(name="MuziClicker - 10zł psc,paypal", value="clicker", inline=False)
  embed.set_footer(text="MuziClicker")
  await ctx.send(embed=embed)



@client.command()
@has_permissions(administrator=True)
async def alert(ctx, *, wiadomosc = None):
    if wiadomosc == None:
        embed=discord.Embed(title="Błąd", description="**Nie podales co chcesz zebym wyslał**", color=0x046dbe)
        embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
        embed.set_footer(text="MuziClicker")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = "Ogłoszenie",
            description = f"**{wiadomosc}**", color=0x046dbe)
        embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
        embed.set_footer(text="MuziClicker")
        await ctx.send(embed=embed)


@client.command()
@has_permissions(administrator=True)
async def nowe(ctx, *, wiadomosc = None):
    if wiadomosc == None:
        embed=discord.Embed(title="Błąd", description="**Nie podales co chcesz zebym wyslał**", color=0x046dbe)
        embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
        embed.set_footer(text="MuziClicker")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = "Dodano",
            description = f"**```{wiadomosc}```**", color=0x046dbe)
        embed.set_author(name="MuziClicker", icon_url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/839131900915351612/905168773537992714/PROFILOWE.png")
        embed.set_footer(text="MuziClicker")
        await ctx.send(embed=embed)




client.run('OTA1MTE2NDkyNzAwNDgzNTk0.YYFZbA.fXTuuKhsSD0Uq-l6qm0YbSVPnbE') 









