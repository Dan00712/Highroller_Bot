import highroller.bot_manager as bm

import discord
from discord.ext import commands

from typing import List
import random
from functools import reduce
import logging

logger = logging.getLogger(__name__)


class Dice:
    def __init__(self, dice: int, dice_count: int = 1):
        self.dice = dice
        self.n = dice_count

    def roll(self) -> List[int]:
        return [random.randint(1, self.dice) for _ in range(self.n)]

    def __str__(self):
        rolls = self.roll()
        rolls_s = reduce(lambda acc, b: acc + str(b) + ",  ", rolls, "")
        sum = reduce(lambda acc, b: acc + b, rolls, 0)
        return f"{self.n}d{self.dice}::\t{rolls_s[:-3]} \t\tsum: {sum}"


class DiceConverter(commands.Converter):
    async def convert(self, ctx, arg) -> Dice:
        dice_t = arg.split('d')
        logger.debug('received converter arg of %s', arg)

        if len(dice_t) != 2:
            raise ValueError("invalid identifier")

        if dice_t[0]:
            dice_count = int(dice_t[0])
        else:
            dice_count = 1

        dice_type = int(dice_t[-1])
        return Dice(dice=dice_type, dice_count=dice_count)


async def quick_roll(
        ctx: discord.Interaction,
        rolls: commands.Greedy[DiceConverter]
        ):
    msg = ""

    try:
        msg = reduce(
                lambda acc, b: acc + str(b) + "\n",
                rolls,
                "these are thy results\n"
                )
        logger.debug("sending response \n%s", msg)
        await ctx.send(msg)
    except Exception as e:
        logger.critical("error received %s", e)


def register_commands():
    bot = bm.get_bot()
    logger.debug("registering cmd quick_roll with bot %s", bot)

    bot.command(name='qroll')(quick_roll)
