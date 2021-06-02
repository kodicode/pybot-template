import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('>help'))
	print('Bot working, bitch!')

@client.event
async def on_member_join(member):
	role = discord.utils.get(member.guild.roles, id = 780020533428224032)
	await member.add_roles(role)

@client.command()
async def boom(ctx):
	author = ctx.message.author
	await ctx.channel.purge(limit = 1)
	await ctx.send(f'{author}, взорвался!')

@client.command()
@commands.has_permissions(view_audit_log = True)
async def clear(ctx, amount = 999999999999):
	author = ctx.message.author
	await ctx.channel.purge(limit = amount)
	await ctx.send(f'{author}, очистил сообщения')

@client.command()
@commands.has_permissions(view_audit_log = True)
async def kick(ctx, member: discord.Member, *, reason = "Нарушение правил"):
	await ctx.channel.purge(limit = 1)
	await member.kick(reason = reason)

client.run('') # Set token
