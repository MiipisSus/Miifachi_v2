"""
Discord Views 和 UI 元件 (py-cord 版本)
"""

import discord
import random


class ConfirmView(discord.ui.View):
    """確認/取消的按鈕 View"""
    
    def __init__(self):
        super().__init__(timeout=60)
        self.value = None

    @discord.ui.button(label='確認', style=discord.ButtonStyle.green)
    async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = True
        self.stop()

    @discord.ui.button(label='取消', style=discord.ButtonStyle.red)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = False
        self.stop()


class CoinFlipView(discord.ui.View):
    """硬幣正反面選擇 View"""
    
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="正面", style=discord.ButtonStyle.blurple)
    async def heads(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = "heads"
        self.stop()

    @discord.ui.button(label="反面", style=discord.ButtonStyle.blurple)
    async def tails(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = "tails"
        self.stop()


class RockPaperScissorsSelect(discord.ui.Select):
    """剪刀石頭布選擇器"""
    
    def __init__(self):
        options = [
            discord.SelectOption(
                label="剪刀", description="你選擇剪刀", emoji="✂"
            ),
            discord.SelectOption(
                label="石頭", description="你選擇石頭", emoji="🪨"
            ),
            discord.SelectOption(
                label="布", description="你選擇布", emoji="🧻"
            ),
        ]
        super().__init__(
            placeholder="選擇你的手勢...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        choices = {
            "石頭": 0,
            "布": 1,
            "剪刀": 2,
        }
        user_choice = self.values[0]
        user_choice_index = choices[user_choice]

        bot_choice = random.choice(list(choices.keys()))
        bot_choice_index = choices[bot_choice]

        result_embed = discord.Embed(color=0xBEBEFE)
        result_embed.set_author(
            name=interaction.user.name, 
            icon_url=interaction.user.display_avatar.url
        )

        winner = (3 + user_choice_index - bot_choice_index) % 3
        if winner == 0:
            result_embed.description = f"**平手！**\n你選擇了{user_choice}，我選擇了{bot_choice}。"
            result_embed.colour = 0xF59E42
        elif winner == 1:
            result_embed.description = f"**你贏了！**\n你選擇了{user_choice}，我選擇了{bot_choice}。"
            result_embed.colour = 0x57F287
        else:
            result_embed.description = f"**你輸了！**\n你選擇了{user_choice}，我選擇了{bot_choice}。"
            result_embed.colour = 0xE02B2B

        await interaction.response.edit_message(
            embed=result_embed, content=None, view=None
        )


class RockPaperScissorsView(discord.ui.View):
    """剪刀石頭布遊戲 View"""
    
    def __init__(self):
        super().__init__()
        self.add_item(RockPaperScissorsSelect())
