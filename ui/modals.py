"""
Discord Modals (彈出式表單)
"""

import discord


class FeedbackModal(discord.ui.Modal, title='意見回饋'):
    """意見回饋表單"""
    
    name = discord.ui.TextInput(
        label='名稱',
        placeholder='請輸入你的名稱...',
        required=False,
        max_length=50,
    )
    
    feedback = discord.ui.TextInput(
        label='意見回饋',
        style=discord.TextStyle.long,
        placeholder='請輸入你的意見...',
        required=True,
        max_length=1000,
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f'感謝你的回饋，{self.name.value or "匿名使用者"}！', 
            ephemeral=True
        )


class SayModal(discord.ui.Modal, title='讓機器人說話'):
    """讓機器人說話的表單"""
    
    message = discord.ui.TextInput(
        label='訊息內容',
        style=discord.TextStyle.long,
        placeholder='請輸入要讓機器人說的話...',
        required=True,
        max_length=2000,
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(self.message.value)


class ReportModal(discord.ui.Modal, title='檢舉使用者'):
    """檢舉使用者表單"""
    
    reason = discord.ui.TextInput(
        label='檢舉原因',
        style=discord.TextStyle.long,
        placeholder='請詳細說明檢舉原因...',
        required=True,
        max_length=1000,
    )
    
    evidence = discord.ui.TextInput(
        label='證據 (可選)',
        style=discord.TextStyle.long,
        placeholder='提供相關證據或連結...',
        required=False,
        max_length=500,
    )

    async def on_submit(self, interaction: discord.Interaction):
        # 這裡可以加入檢舉處理邏輯
        await interaction.response.send_message(
            '已收到你的檢舉，管理員會盡快處理。', 
            ephemeral=True
        )
