import dbl
import discord
from discord.ext import commands, tasks
import os

import asyncio
import logging


class TopGG(commands.Cog):
    """Handles interactions with the top.gg API"""

    def __init__(self, bot):
        self.bot = bot
        with open("./lib/bot/topgg.txt", "r", encoding="utf-8") as tf:
            self.token = tf.read() # set this to your DBL token
        self.dblpy = dbl.DBLClient(self.bot, self.token, webhook_path='/dblwebhook', webhook_auth=something, webhook_port=5000)

    # The decorator below will work only on discord.py 1.1.0+
    # In case your discord.py version is below that, you can use self.bot.loop.create_task(self.update_stats())

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        print('Received an upvote')
        print(data)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("TopGG")


def setup(bot):
    global logger
    logger = logging.getLogger('bot')
    bot.add_cog(TopGG(bot))