"""
Usage:

python main.py <token var name> <status no.> <name> <bot=True|False>
"""
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv

import os
import sys

client = commands.Bot(command_prefix=":",
                      intents=discord.Intents.all(),
                      self_bot=True)
load_dotenv()


def get_cmd():
    if sys.argv[2] == "1":
        # Setting `Playing` status
        return client.change_presence(
            status=discord.Status.dnd, activity=discord.Game(name=sys.argv[3])
        )

    elif sys.argv[2] == "2":
        # Setting `Streaming ` status
        return client.change_presence(
            activity=discord.Streaming(
                name=sys.argv[3], url="https://www.twitch.tv/marcoronco"
            )
        )

    elif sys.argv[2] == "3":
        # Setting `Listening ` status
        return client.change_presence(
            status=discord.Status.dnd,
            activity=discord.Activity(
                type=discord.ActivityType.listening, name=sys.argv[3]
            ),
        )

    elif sys.argv[2] == "4":
        # Setting `Watching ` status
        return client.change_presence(
            status=discord.Status.dnd,
            activity=discord.Activity(
                type=discord.ActivityType.watching, name=sys.argv[3]
            ),
        )


@client.event
async def on_ready():
    print(f"\n [!] Logged in as {client.user}")
    await get_cmd()


if sys.argv[4].lower() == "true":
    is_bot = True
else:
    is_bot = False
try:
    client.run(os.getenv(f"{sys.argv[1]}"), bot=is_bot)
except Exception:
    logging.getLogger("Bot Generator").warning(
            " [!] Dummy Accounts Can't Login")
