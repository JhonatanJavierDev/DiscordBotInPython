# Simple Bot in Python Code By JhonCorellaDev
# Free Proyect Suport CodeBlack

import discord
from discord.ext import commands
from discord.utils import get
import datetime

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents = intents)


# Comandos
@client.command(name = 'anuncio')

@commands.has_permissions(manage_messages = True)

async def anuncio(ctx, *, anuncio):
    channel = client.get_channel(1036029967219294298)
    embed = discord.Embed(title = anuncio, color = 0xFF0000)
    await channel.send(embed = embed)
    await ctx.send(f'Anuncio enviado correctamente al canal {channel.mention}.')


@client.command(name = 'saludo')

async def saludo(ctx):
    await ctx.send('Hola, ¿cómo estás?')


@client.command(name = 'hora')

async def hora(ctx):
    await ctx.send(f'La hora actual es {datetime.datetime.now().time()}')


@client.command(name = 'fecha')

async def fecha(ctx):
    await ctx.send(f'La fecha actual es {datetime.datetime.now().date()}')


@client.command(name = 'ban')

@commands.has_permissions(ban_members = True)

async def bannear(ctx, member: discord.Member, *, motivo):
    await ctx.guild.ban(member, reason = motivo)
    await ctx.send(f'Se baneo a {member.mention} por el motivo {motivo}.')


@client.command(name = 'desban')

@commands.has_permissions(ban_members = True)

async def desbannear(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Se desbaneo a {user.mention}.')
            return


@client.command(name = 'emoji')

async def emoji(ctx, emoji):
    await ctx.send(f'<:{emoji}:>')

@client.command(name = 'borrar')

@commands.has_permissions(manage_messages = True)

async def borrar(ctx, limit = 1):
    await ctx.channel.purge(limit = limit)


@client.command(name = 'serverinfo')

async def serverinfo(ctx):
    embed = discord.Embed(title = 'Información del Servidor', color = 0xFF0000)
    embed.add_field(name = 'Nombre del Servidor', value = ctx.guild.name)
    embed.add_field(name = 'ID del Servidor', value = ctx.guild.id)
    embed.add_field(name = 'Creado el', value = ctx.guild.created_at.strftime('%d de %B del %Y'))
    embed.add_field(name = 'Dueño del Servidor', value = ctx.guild.owner)
    embed.add_field(name = 'Miembros', value = f'{len(ctx.guild.members)}')
    embed.add_field(name = 'Cantidad de Roles', value = len(ctx.guild.roles))
    embed.add_field(name = 'Emojis', value = len(ctx.guild.emojis))
    embed.add_field(name = 'Canales de Voz', value = len(ctx.guild.voice_channels))
    embed.add_field(name = 'Canales de Texto', value = len(ctx.guild.text_channels))
    embed.add_field(name = 'Region', value = str(ctx.guild.region))
    embed.set_thumbnail(url = ctx.guild.icon_url)
    await ctx.send(embed = embed)


@client.command(name = 'userinfo')

async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title = 'Información del Usuario', color = 0xFF0000)
    embed.add_field(name = 'Nombre', value = member.name)
    embed.add_field(name = 'ID', value = member.id)
    embed.add_field(name = 'Estado', value = member.status)
    embed.add_field(name = 'Rol mas alto', value = member.top_role)
    embed.add_field(name = 'Se unio el', value = member.joined_at.strftime('%d de %B del %Y'))
    embed.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed = embed)


@client.command(name = 'clear')

@commands.has_permissions(manage_messages = True)

async def clear(ctx, amount = 2):
    await ctx.channel.purge(limit = amount)


@client.command(name = 'kick')

@commands.has_permissions(kick_members = True)

async def kick(ctx, member:discord.Member,*,motivo):
    await member.kick(reason=motivo)
    await ctx.send(f'Se kicko a {member.mention} por el motivo {motivo}')


@client.command(name = 'mute')

@commands.has_permissions(manage_roles = True)

async def mute(ctx, member:discord.Member):
    role = discord.utils.get(ctx.guild.roles, name = 'Muted')

    await member.add_roles(role)
    await ctx.send(f'Se muteo a {member.mention}.')


@client.command(name = 'unmute')

@commands.has_permissions(manage_roles = True)

async def unmute(ctx, member:discord.Member):
    role = discord.utils.get(ctx.guild.roles, name = 'Muted')

    await member.remove_roles(role)
    await ctx.send(f'Se desmuteo a {member.mention}.')


@client.command(name = 'lock')

@commands.has_permissions(manage_channels = True)

async def lock(ctx, channel:discord.TextChannel):
    await channel.set_permissions(ctx.guild.default_role, send_messages = False)
    await ctx.send(f'Canal {channel.mention} cerrado.')


@client.command(name = 'unlock')

@commands.has_permissions(manage_channels = True)

async def unlock(ctx, channel:discord.TextChannel):
    await channel.set_permissions(ctx.guild.default_role, send_messages = True)
    await ctx.send(f'Canal {channel.mention} abierto.')


@client.command(name = 'decir')

@commands.has_permissions(manage_messages = True)

async def decir(ctx, *, mensaje):
    await ctx.message.delete()
    await ctx.send(mensaje)


@client.command(name = 'ping')

async def ping(ctx):
    await ctx.send(f'Latencia: {round(client.latency * 1000)}ms.')


@client.command(name = 'invite')

async def invite(ctx):
    await ctx.send(f'Invita a tus amigos a tu servidor mediante el siguiente enlace: {discord.utils.oauth_url(client.user.id)}')


@client.command(name = 'ayuda')

async def ayuda(ctx):
    embed = discord.Embed(title = 'Ayuda', color = 0xFF0000)
    embed.add_field(name = 'Comandos disponibles', value = 'saludo, hora, fecha, ban, desban, emoji, borrar, serverinfo, userinfo, clear, kick, mute, unmute, lock, unlock, decir, ping, invite')
    await ctx.send(embed = embed)

#YOUR TOKEN
client.run("TOKEN")
