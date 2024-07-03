import discord
from discord.ext import commands 
import asyncio

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='_', intents=intents)

@bot.event
async def on_guild_channel_delete(channel):
    logs = await channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete).flatten()
    if logs:
        entry = logs[0]
        user = entry.user
        # Nejsi admin, kick
        if not user.guild_permissions.administator:
            await channel.guild.kick(user, reason ="Apolena Nuke: Maže role")
            print(f"{user} byl kicknut za mázaní rolí")

@bot.event
async def on_member_ban(guild, user):
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
    if logs
        entry = logs[0]
        repsponsible_user = entry.user
        # Kick = dokud není admin
        if not repsponsible_user.guild_permissions.adminstator:
            await guild.kick(repsponsible_user, reason = "Apolena Nuke: Banuje členy!")
            print(f"{repsponsible_user} byl moc kicknut za banování členů!")

# Bot login 
bot.run('DISCORD_TOKEN')
