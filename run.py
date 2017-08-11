import asyncio
import configparser
import inspect
import sys
import time
import os

import discord
from discord.ext import commands
from logbook import Logger, StreamHandler, FileHandler

logger = Logger("Discord Music")
logger.handlers.append(StreamHandler(sys.stdout, bubble=True))
logger.handlers.append(FileHandler("last-run.log", bubble=True))

logger.debug("Loading config files")

config = configparser.ConfigParser()

token = ""
snip = ""

if os.path.exists("config.ini"):
    config.read("config.ini")

    try:
        token = config['Config']['token']
    except KeyError:
        logger.critical("No token found in config, please ensure that the config formatting is correct")
        time.sleep(5)
        exit(1)

    if token == "":
        logger.critical("No token set! Exiting")
        time.sleep(5)
        exit(1)

    try:
        snip = config['Config']['snip']
    except KeyError:
        logger.critical("No path to snip found in config, please ensure that the config formatting is correct")
        time.sleep(5)
        exit(1)

    if snip == "":
        logger.critical("No path to snip set! Exiting")
        time.sleep(5)
        exit(1)

else:
    logger.error("No config file, creating one now")
    with open("default.config.ini") as f:
        config = f.read()
    with open("config.ini", 'w') as f:
        f.write(config)
    logger.info("Config created, please set config!")
    time.sleep(3)
    exit(0)

logger.info("Config loaded")

bot = commands.Bot(command_prefix=['m.'], self_bot=True)
bot.remove_command('help')


@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user.name} with ID {bot.user.id}")
    logger.info("Ready to start")


@bot.command(name="quit")
async def _quit():
    await bot.say("Logging out...")
    logger.info("Logging out")
    await bot.logout()
    exit(0)


async def music_loop():
    await bot.wait_until_ready()
    await asyncio.sleep(1)
    last_song = ""
    while not bot.is_closed:
        song = pull_song()
        if song != last_song:
            await bot.change_presence(afk=True, status=discord.Status.invisible, game=discord.Game(name=song))
            last_song = song
            logger.info(f"Set Discord status to {song.encode('ascii', 'ignore').decode()}")
        await asyncio.sleep(8)


def pull_song():
    with open(snip, encoding="utf8") as f:
        return f.read()


try:
    logger.info("Logging in")
    bot.loop.create_task(music_loop())
    bot.run(token, bot=False)
except discord.errors.LoginFailure:
    logger.critical("Log in failed, check token!")
    time.sleep(5)
    exit(1)
