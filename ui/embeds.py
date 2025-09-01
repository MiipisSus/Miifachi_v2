"""
Discord Embed 元件
"""
from datetime import datetime

import discord

from core.types.embed import EmbedType


class DefaultEmbed(discord.Embed):
    """預設的 Embed 類別"""
    default_embed_color = 0x51b0e7
    default_description = '米花機 MiiFaChi'
    def __init__(self, embed_type: EmbedType):
        super().__init__(
            title="",
            description=self.default_description,
            color=self.default_embed_color,
            timestamp=datetime.today()
            )
        
        self._init_embed(embed_type)

    def _init_embed(self, embed_type: EmbedType):
        if embed_type == EmbedType.GENERAL_FAILED:
            self.title = "指令暫時失敗了！請稍後再試"
            self.color = 0xde5959
            

class ZodiacEmbed(discord.Embed):
    color_code = [0xff0000, 0x228c22, 0xfff222, 0xdadbdd, 0xd4ad2c, 0x6d712e, 
                  0xf8c8dc, 0x000000, 0x4d0f28, 0x888b8d, 0x183efa, 0x9fe2bf]
    zodiac_list = ["牡羊座 ♈ ","金牛座 ♉️ ","雙子座 ♊️ ","巨蟹座 ♋️ ","獅子座 ♌️ ","處女座 ♍️ ",
                   "天秤座 ♎️ ","天蠍座 ♏️ ","射手座 ♐️ ","摩羯座 ♑️ ","水瓶座 ♒️ ","雙魚座 ♓️ "]
    request_list = ["本日運勢", "本週運勢", "本月運勢"]
    def __init__(self, *args):
        zodiac_type = args[0]
        request_type = args[1]
        super(ZodiacEmbed, self).__init__(title=f"{self.zodiac_list[zodiac_type]}{self.request_list[request_type]}", 
                                          color=self.color_code[zodiac_type], timestamp=datetime.today())
        self.set_thumbnail(url='https://i.imgur.com/JDoObmi.png')
        if request_type == 0:
            self.add_field(name=f"整體指數 {args[2] * '💚'}{((5 - args[2]) * '🤍')}",
                           value=f"```{args[3]}```", inline=False)
            self.add_field(name=f"愛情指數 {args[4] * '❤️'}{((5 - args[4]) * '🤍')}",
                           value=f"```{args[5]}```", inline=False)
            self.add_field(name=f"事業指數 {args[6] * '🩵'}{((5 - args[6]) * '🤍')}",
                           value=f"```{args[7]}```", inline=False)
            self.add_field(name=f"財運指數 {args[8] * '💛'}{((5 - args[8]) * '🤍')}",
                           value=f"```{args[9]}```", inline=False)
        elif request_type == 1:
            self.add_field(name=f"整體指數 {args[2] * '💚'}{((5 - args[2]) * '🤍')}",
                           value=f"```{args[3]}```", inline=False)
            self.add_field(name=f"愛情指數 {args[4] * '❤️'}{((5 - args[4]) * '🤍')}",
                           value=f"```{args[5]}```\n \
                                   ```{args[7]}```", inline=False)
            self.add_field(name=f"事業指數 {args[8] * '🩵'}{((5 - args[8]) * '🤍')}",
                           value=f"```{args[9]}```", inline=False)
            self.add_field(name=f"財運指數 {args[10] * '💛'}{((5 - args[10]) * '🤍')}",
                           value=f"```{args[11]}```", inline=False)
        else:
            self.add_field(name=f"整體指數 {args[2] * '💚'}{((5 - args[2]) * '🤍')}",
                           value=f"```{args[3]}```", inline=False)
            self.add_field(name=f"愛情指數 {args[4] * '❤️'}{((5 - args[4]) * '🤍')}",
                           value=f"```{args[6]}```\n \
                                   ```{args[7]}```", inline=False)
            self.add_field(name=f"事業指數 {args[8] * '🩵'}{((5 - args[8]) * '🤍')}",
                           value=f"```{args[10]}```\n \
                                   ```{args[11]}```", inline=False)
            self.add_field(name=f"財運指數 {args[12] * '💛'}{((5 - args[12]) * '🤍')}",
                           value=f"```{args[13]}```", inline=False)
