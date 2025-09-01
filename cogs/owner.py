"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.3.0 (py-cord)
"""

import discord
from discord.ext import commands


class Owner(commands.Cog, name="owner"):
    def __init__(self, bot) -> None:
        self.bot = bot

    # 保留前綴指令用於同步
    @commands.command(name="sync", description="同步 slash commands")
    @commands.is_owner()
    async def sync_prefix(self, ctx, scope: str = "guild") -> None:
        """
        使用前綴指令同步 slash commands
        
        :param ctx: 指令內容
        :param scope: 同步範圍 (guild 或 global)
        """
        if scope == "global":
            await self.bot.sync_commands()
            embed = discord.Embed(
                description="Slash commands 已全域同步",
                color=0xBEBEFE,
            )
            await ctx.send(embed=embed)
        elif scope == "guild":
            await self.bot.sync_commands(guild_ids=[ctx.guild.id])
            embed = discord.Embed(
                description="Slash commands 已在此伺服器同步",
                color=0xBEBEFE,
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description="範圍必須是 `global` 或 `guild`", 
                color=0xE02B2B
            )
            await ctx.send(embed=embed)

    @discord.slash_command(name="reload", description="重新載入 cog")
    @discord.option(name="cog", description="要重新載入的 cog 名稱")
    @discord.default_permissions(administrator=True)
    async def reload(self, ctx: discord.ApplicationContext, cog: str) -> None:
        """
        重新載入指定的 cog
        
        :param ctx: ApplicationContext
        :param cog: cog 名稱
        """
        # 檢查是否為 owner
        if ctx.author.id != self.bot.owner_id:
            await ctx.respond("你沒有權限使用此指令！", ephemeral=True)
            return
            
        try:
            self.bot.reload_extension(f"cogs.{cog}")
            embed = discord.Embed(
                description=f"成功重新載入 `{cog}` cog", 
                color=0xBEBEFE
            )
            await ctx.respond(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                description=f"無法重新載入 `{cog}` cog: {str(e)}", 
                color=0xE02B2B
            )
            await ctx.respond(embed=embed)

    @discord.slash_command(name="shutdown", description="關閉機器人")
    @discord.default_permissions(administrator=True)
    async def shutdown(self, ctx: discord.ApplicationContext) -> None:
        """
        關閉機器人
        
        :param ctx: ApplicationContext
        """
        # 檢查是否為 owner
        if ctx.author.id != self.bot.owner_id:
            await ctx.respond("你沒有權限使用此指令！", ephemeral=True)
            return
            
        embed = discord.Embed(
            description="正在關機... 再見！ :wave:", 
            color=0xBEBEFE
        )
        await ctx.respond(embed=embed)
        await self.bot.close()


def setup(bot):
    bot.add_cog(Owner(bot))
