import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True  # For receiving messages
intents.guilds = True    # For server-specific commands

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send('Hello! I am a bot of The God Empire, bestowed with intents!')
    await bot.process_commands(message)


bot.run('your_token_here')