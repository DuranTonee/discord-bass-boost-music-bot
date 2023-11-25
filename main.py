import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from music import music  # Import the Music cog

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix=["!", '😎 '], intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    await bot.change_presence(activity=discord.Game(name='bass boosted music'))
    await bot.add_cog(music(bot))

bot.run(BOT_TOKEN)
