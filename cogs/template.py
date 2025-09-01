"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.3.0 (py-cord)
"""

import discord
from discord.ext import commands


# Here we name the cog and create a new class for the cog.
class Template(commands.Cog, name="template"):
    def __init__(self, bot) -> None:
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @discord.slash_command(
        name="testcommand",
        description="這是一個測試指令，什麼都不做。",
    )
    async def testcommand(self, ctx: discord.ApplicationContext) -> None:
        """
        這是一個測試指令，什麼都不做。

        :param ctx: The application command context.
        """
        # Do your stuff here
        await ctx.respond("這是一個測試指令的回應！")

    @discord.slash_command(
        name="hello",
        description="向使用者打招呼",
    )
    @discord.option(name="name", description="要打招呼的名字", required=False)
    async def hello(self, ctx: discord.ApplicationContext, name: str = None) -> None:
        """
        向使用者打招呼

        :param ctx: The application command context.
        :param name: 要打招呼的名字
        """
        if name:
            await ctx.respond(f"你好，{name}！")
        else:
            await ctx.respond(f"你好，{ctx.author.mention}！")

    @discord.slash_command(
        name="ping",
        description="檢查機器人延遲",
    )
    async def ping(self, ctx: discord.ApplicationContext) -> None:
        """
        檢查機器人延遲

        :param ctx: The application command context.
        """
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"延遲: {latency}ms",
            color=0xBEBEFE
        )
        await ctx.respond(embed=embed)


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(Template(bot))
