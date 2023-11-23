import discord
from discord.ext import commands
from config import BOT_TOKEN
from music import music  # Import the Music cog

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
