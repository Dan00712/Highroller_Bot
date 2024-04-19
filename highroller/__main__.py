import logging
import os

import dotenv
import discord
from discord.ext import commands

import highroller.logging
import highroller.bot_manager as bm


highroller.logging.load_config()
logger = logging.getLogger(__name__)

logger.debug("loading .env...")
dotenv.load_dotenv()
logger.debug("loaded .env")


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
bm.set_bot(bot)

# load other modules that are needed


def main():
    token = os.environ["DISCORD_BOT_TOKEN"]
    bot.run(token)


if __name__ == '__main__':
    main()
