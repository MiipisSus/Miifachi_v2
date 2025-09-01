"""
Discord Modals (彈出式表單) - py-cord 版本
"""

import discord


class FeedbackModal(discord.ui.Modal):
    """意見回饋表單"""
    
    def __init__(self):
        super().__init__(title='意見回饋')
        
        self.add_item(discord.ui.InputText(
            label='名稱',
            placeholder='請輸入你的名稱...',
            required=False,
            max_length=50,
        ))
        
        self.add_item(discord.ui.InputText(
            label='意見回饋',
            style=discord.InputTextStyle.long,
            placeholder='請輸入你的意見...',
            required=True,
            max_length=1000,
        ))

    async def callback(self, interaction: discord.Interaction):
        name = self.children[0].value or "匿名使用者"
        await interaction.response.send_message(
            f'感謝你的回饋，{name}！', 
            ephemeral=True
        )


class SayModal(discord.ui.Modal):
    """讓機器人說話的表單"""
    
    def __init__(self):
        super().__init__(title='讓機器人說話')
        
        self.add_item(discord.ui.InputText(
            label='訊息內容',
            style=discord.InputTextStyle.long,
            placeholder='請輸入要讓機器人說的話...',
            required=True,
            max_length=2000,
        ))

    async def callback(self, interaction: discord.Interaction):
        message = self.children[0].value
        await interaction.response.send_message(message)


class ReportModal(discord.ui.Modal):
    """檢舉使用者表單"""
    
    def __init__(self):
        super().__init__(title='檢舉使用者')
        
        self.add_item(discord.ui.InputText(
            label='檢舉原因',
            style=discord.InputTextStyle.long,
            placeholder='請詳細說明檢舉原因...',
            required=True,
            max_length=1000,
        ))
        
        self.add_item(discord.ui.InputText(
            label='證據 (可選)',
            style=discord.InputTextStyle.long,
            placeholder='提供相關證據或連結...',
            required=False,
            max_length=500,
        ))

    async def callback(self, interaction: discord.Interaction):
        # 這裡可以加入檢舉處理邏輯
        await interaction.response.send_message(
            '已收到你的檢舉，管理員會盡快處理。', 
            ephemeral=True
        )
