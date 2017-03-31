import discord
from discord.ext import commands
import asyncio
import configparser
import inspect

config = configparser.ConfigParser()
config.read("config.ini")
try:
    token = config['Config']['token']
except KeyError:
    print("Please assign your token in config.ini")
    input()
if token == "":
    print("Please assign your token in config.ini")
    input()
try:
    snip = config['Config']['snip']
except KeyError:
    print("Please assign your snip directory in config.ini")
    input()
if token == "":
    print("Please assign your token in config.ini")
    input()

# Set's bot's desciption and prefixes in a list
description = ""
bot = commands.Bot(command_prefix=['musicself.'], description=description, self_bot=True)

###################
## Startup Stuff ##
###################

bot.remove_command('help')

@bot.event
async def on_ready():
    # Outputs login data to console
    print("---------------------------")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("---------------------------")
    song = pull_song()
    savesong = song
    await bot.change_presence(afk=True, status=discord.Status.idle, game=discord.Game(name="\u266B {}".format(song)))
    print("Now playing: {}".format(song.encode("ascii", "ignore").decode()))
    while True:
        song = pull_song()
        if savesong != song:
            await bot.change_presence(afk=True, status=discord.Status.idle, game=discord.Game(name="\u266B {}".format(song)))
            savesong = song
            print("Now playing: {}".format(song.encode("ascii", "ignore").decode()))
        await asyncio.sleep(5)

def pull_song():
    file = open(snip, encoding="utf8")
    song = file.read()
    return song

# Ping Pong
# Testing the response of the bot
@bot.command()
async def ping():
    """Pong. Test's responsiveness of bot"""
    await bot.say("Music: Pong")

@bot.command(pass_context=True, name="eval")
async def eval_(ctx, *, code: str):
    """Evaluates a line of code provided"""
    code = code.strip("` ")
    server = ctx.message.server
    message = ctx.message
    try:
        result = eval(code)
        if inspect.isawaitable(result):
            result = await result
    except Exception as e:
        await bot.say("```py\nInput: {}\n{}: {}```".format(code, type(e).__name__, e))
    else:
        await bot.say("```py\nInput: {}\nOutput: {}\n```".format(code, result))
    await bot.delete_message(message)

##############################
## FANCY TOKEN LOGIN STUFFS ##
##############################

print("Logging in")
try:
    bot.run(token, bot=False)
except discord.errors.LoginFailure:
    print("Invalid token")
