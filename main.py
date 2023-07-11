import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
ENEMY = ''  # Paste your enemy`s discord nickname here
GUILD_ID = 1  # Paste your GUILD_ID here
BOT_TOKEN = ''  # Paste your bot token here


@client.event
async def on_ready() -> None:
    guild = client.get_guild(GUILD_ID)
    for member in guild.members:
        if member.name == ENEMY:
            await member.move_to(None)


@client.command()
async def ping(ctx) -> None:  # a red herring
    await ctx.reply("pong")


@client.event
async def on_voice_state_update(member, before, after) -> None:
    if member.name == ENEMY:
        await member.move_to(None)
        await member.send("")  # Paste your text here


client.run(BOT_TOKEN)
