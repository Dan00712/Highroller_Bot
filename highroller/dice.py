import highroller.bot_manager as bm

from discord.ext import commands

from typing import List
import random
from functools import reduce

bot = bm.get_bot()


class Dice:
    def __init__(self, dice: int, dice_count: int = 1):
        self.dice = dice
        self.n = dice_count

    def roll(self) -> List[int]:
        return [random.randint(1, self.dice) for _ in range(self.n)]

    def __str__(self):
        rolls_s = reduce(lambda acc, b: acc + b + ", ", self.roll(), "")
        return f"{self.n}d{self.dice}::{rolls_s}"


class DiceConverter(commands.Converter):
    async def convert(self, ctx, arg) -> Dice:
        (dice_n, dice_type) = arg.split('d')
        return Dice(dice=dice_type, dice_count=dice_n)


@bot.command()
async def quick_roll(ctx, *args):
    await ctx.send(reduce(lambda acc, b: acc + b + "\n",
                   [DiceConverter.convert(arg) for arg in args],
                   ""
                   ))
