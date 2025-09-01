"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.3.0
"""

import random
import io
import importlib

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

from ui.embeds import DefaultEmbed
from core.types.embed import EmbedType


class Fun(commands.Cog, name="fun"):
    zodiac_list = ["牡羊座","金牛座","雙子座","巨蟹座","獅子座","處女座","天秤座","天蠍座","射手座","摩羯座","水瓶座","雙魚座"]
    request_list = ["本日運勢", "本週運勢", "本月運勢"]
    vote_func_list = ["創建投票", "查看投票", "終止投票"]
    raffle_func_list = ["創建抽獎", "查看抽獎", "終止抽獎"]
    
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name="狗勾", description="給我一隻狗勾")
    @app_commands.describe(breed="選擇你想要的狗狗品種")
    @app_commands.choices(breed=[
        app_commands.Choice(name="隨機狗勾", value="random"),
        app_commands.Choice(name="伯恩山犬", value="bernese"),
        app_commands.Choice(name="邊牧", value="collie/border"),
        app_commands.Choice(name="柯基", value="corgi"),
        app_commands.Choice(name="柴柴", value="shiba"),
        app_commands.Choice(name="吉娃娃", value="chihuahua"),
        app_commands.Choice(name="薩摩耶", value="samoyed"),
        app_commands.Choice(name="哈士奇", value="husky"),
        app_commands.Choice(name="博美", value="pomeranian")
    ])
    async def dog_command(self, context: Context, breed: app_commands.Choice[str]) -> None:
        """
        獲取指定品種的狗勾圖片
        
        :param context: 指令內容
        :param breed: 選擇的狗勾品種
        """
        breed_value = breed.value
        
        # 根據選擇建立 API URL
        if breed_value == "random":
            url = "https://dog.ceo/api/breeds/image/random"
        else:
            url = f"https://dog.ceo/api/breed/{breed_value}/images/random"
        
        await context.defer()
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    image_url = data["message"]
                    async with session.get(image_url) as image_response:
                        if image_response.status == 200:
                            image_data = await image_response.read()
                            file_buffer = io.BytesIO(image_data)
                            file = discord.File(fp=file_buffer, filename="dog.jpg")
                            await context.interaction.followup.send(
                                content='狗....................勾',
                                file=file)
                else:
                    await context.interaction.followup.send("API 發生問題，請稍後再試")

    @commands.hybrid_command(name="貓貓", description="給我一隻貓貓")
    @app_commands.describe(breed="選擇你想要的貓貓品種")
    @app_commands.choices(breed=[
        app_commands.Choice(name="隨機貓貓", value="random"),
        app_commands.Choice(name="英短", value="bsho"),
        app_commands.Choice(name="美短", value="asho"),
        app_commands.Choice(name="布偶", value="ragd"),
    ])
    async def cat_command(self, context: Context, breed: app_commands.Choice[str]) -> None:
        breed_value = breed.value
        if breed_value == "random":
            url = "https://api.thecatapi.com/v1/images/search"
        else:
            url = f"https://api.thecatapi.com/v1/images/search?breed_ids={breed_value}"

        await context.defer()

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    image_url = data[0]["url"]
                    async with session.get(image_url) as image_response:
                        if image_response.status == 200:
                            image_data = await image_response.read()
                            file_buffer = io.BytesIO(image_data)
                            file = discord.File(fp=file_buffer, filename="cat.jpg")
                            await context.interaction.followup.send(
                                content='咪....................咪',
                                file=file)
                else:
                    await context.interaction.followup.send("API 發生問題，請稍後再試")

    @commands.hybrid_command(name='星座運勢', description="看看你今日的星座運勢吧!")
    @app_commands.describe(zodiac_sign="選擇你的星座", type="選擇查詢類型")
    @app_commands.choices(zodiac_sign=[
        app_commands.Choice(name="牡羊座", value="aries"),
        app_commands.Choice(name="金牛座", value="taurus"),
        app_commands.Choice(name="雙子座", value="gemini"),
        app_commands.Choice(name="巨蟹座", value="cancer"),
        app_commands.Choice(name="獅子座", value="leo"),
        app_commands.Choice(name="處女座", value="virgo"),
        app_commands.Choice(name="天秤座", value="libra"),
        app_commands.Choice(name="天蠍座", value="scorpio"),
        app_commands.Choice(name="射手座", value="sagittarius"),
        app_commands.Choice(name="摩羯座", value="capricorn"),
        app_commands.Choice(name="水瓶座", value="aquarius"),
        app_commands.Choice(name="雙魚座", value="pisces"),
    ],
                          type=[
        app_commands.Choice(name="今日運勢", value="today"),
        app_commands.Choice(name="本週運勢", value="week"),
        app_commands.Choice(name="本月運勢", value="month"),
    ])
    async def zodiac_command(self, context: Context, zodiac_sign: str, type: str) -> None:
        await context.send(f"這是 {zodiac_sign} 的星座運勢！")


async def setup(bot) -> None:
    await bot.add_cog(Fun(bot))
