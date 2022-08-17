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


@bot.slash_command(name="add")
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.respond(left + right)


@bot.slash_command(name="roll")
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.respond('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.respond(result)


@bot.slash_command(name="choose", description='For when you wanna settle the score some other way')
async def choose(ctx, choices):
    """Chooses between multiple choices."""
    options = choices.split(", ")
    choice = random.choice(options)
    await ctx.respond(str(choice))


@bot.slash_command(name="repeat")
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.respond(content)

@bot.slash_command(name="shutdown")
@commands.is_owner()
async def shutdown(ctx):
    exit()

# This runs the bot
bot.run(os.getenv('TOKEN'))