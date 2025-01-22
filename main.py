import discord
from discord.ext import commands
import os

# Bot setup
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}!")

# Load cogs
async def load_cogs():
    for cog in ["roles", "missions", "factions", "events"]:
        await bot.load_extension(f"cogs.{cog}")

# Main startup
async def main():
    async with bot:
        await load_cogs()
        await bot.start("YOUR_BOT_TOKEN")

import asyncio
asyncio.run(main())
