#These grab the token from the .env file
from dotenv import load_dotenv
import os
#These are required to make the discord bot run
import discord
from discord.ext import commands
#These are used for various commands
import random
import sys

load_dotenv() #Grabs the token from the .env file

description = '''A bot that does an undetermined amount of things that are in a variety of catagories.'''

#Initializing variables that will be used for the bot
intents = discord.Intents.default()
keyword = "?"

bot = commands.Bot(command_prefix=keyword, description=description, intents=intents) #Initializes the bot


@bot.event
async def on_ready(): #A check for when the bot has logged in
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your requests"))


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def prefix(ctx, prefix):
    """Changes the prefix of the bot to be whatever the user chooses"""
    bot.command_prefix = prefix
    await ctx.send(f"Prefix is now {prefix}")


# This runs the bot
bot.run(os.getenv('TOKEN'))