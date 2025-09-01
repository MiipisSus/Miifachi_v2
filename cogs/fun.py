"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.3.0 (py-cord)
"""

import random
import io

import aiohttp
import discord
from discord.ext import commands


class Fun(commands.Cog, name="fun"):
    
    def __init__(self, bot) -> None:
        self.bot = bot

    @discord.slash_command(name="狗勾", description="給我一隻狗勾")
    @discord.option(name="品種", description="選擇你想要的狗狗品種", choices=[
        "隨機狗勾", "伯恩山犬", "邊牧", "柯基", "柴柴", "吉娃娃", "薩摩耶", "哈士奇", "博美"
    ])
    async def dog_command(self, ctx: discord.ApplicationContext, 品種: str) -> None:
        """
        獲取指定品種的狗勾圖片
        
        :param ctx: 指令內容
        :param 品種: 選擇的狗勾品種
        """
        breed = 品種
        # 品種對應表
        breed_mapping = {
            "隨機狗勾": "random",
            "伯恩山犬": "bernese",
            "邊牧": "collie/border",
            "柯基": "corgi",
            "柴柴": "shiba",
            "吉娃娃": "chihuahua",
            "薩摩耶": "samoyed",
            "哈士奇": "husky",
            "博美": "pomeranian"
        }
        
        breed_value = breed_mapping.get(breed, "random")
        
        # 根據選擇建立 API URL
        if breed_value == "random":
            url = "https://dog.ceo/api/breeds/image/random"
        else:
            url = f"https://dog.ceo/api/breed/{breed_value}/images/random"
        
        await ctx.defer()
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data["status"] == "success":
                        image_url = data["message"]
                        async with session.get(image_url) as image_response:
                            if image_response.status == 200:
                                image_data = await image_response.read()
                                file_buffer = io.BytesIO(image_data)
                                file = discord.File(fp=file_buffer, filename="dog.jpg")
                                await ctx.followup.send(file=file)
                            else:
                                await ctx.followup.send("無法下載圖片")
                    else:
                        await ctx.followup.send("找不到該品種的狗勾圖片")
                else:
                    error = await response.json()
                    print(error)
                    await ctx.followup.send("API 發生問題，請稍後再試")

    @discord.slash_command(name="貓貓", description="給我一隻貓貓")
    @discord.option(name="breed", description="選擇你想要的貓貓品種", choices=[
        "隨機貓貓", "英短", "美短", "布偶"
    ])
    async def cat_command(self, ctx: discord.ApplicationContext, breed: str) -> None:
        """
        獲取指定品種的貓貓圖片
        
        :param ctx: 指令內容
        :param breed: 選擇的貓貓品種
        """
        # 品種對應表
        breed_mapping = {
            "隨機貓貓": "random",
            "英短": "bsho",
            "美短": "asho",
            "布偶": "ragd"
        }
        
        breed_value = breed_mapping.get(breed, "random")
        
        # 根據選擇建立 API URL
        if breed_value == "random":
            url = "https://api.thecatapi.com/v1/images/search"
        else:
            url = f"https://api.thecatapi.com/v1/images/search?breed_ids={breed_value}"

        await ctx.defer()

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
                            await ctx.followup.send(
                                content='咪....................咪',
                                file=file)
                else:
                    await ctx.followup.send("API 發生問題，請稍後再試")
                    
    @discord.slash_command(name='test', description="測試指令")
    async def test_command(self, ctx: discord.ApplicationContext) -> None:
        await ctx.respond("這是一個測試指令！")


def setup(bot):
    bot.add_cog(Fun(bot))
