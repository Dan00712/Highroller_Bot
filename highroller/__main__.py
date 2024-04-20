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
logger.info("loaded .env")


logger.debug("loading bot...")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
bm.set_bot(bot)
logger.info("loaded bot")

# load other modules that are needed


@bot.event
async def on_ready():
    logger.info("bot ready")
    await bot.tree.sync()
    logger.debug("synced")


@bot.command()
async def sync(ctx):
    await bot.tree.sync()

import highroller.dice


def main():
    logger.info("starting bot")
    token = os.environ["DISCORD_BOT_TOKEN"]
    bot.run(token)


if __name__ == '__main__':
    main()
