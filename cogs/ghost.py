import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÃO ---
LOG_ID = int(os.getenv('LOG_CHANNEL_ID', 1490220486808834118))

class GhostCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # --- MONITORAMENTO DE MENSAGENS APAGADAS ---
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        # Ignora se for bot ou se não tiver conteúdo (ex: apenas imagem)
        if message.author.bot or not message.content:
            return

        log_channel = self.bot.get_channel(LOG_ID)
        if not log_channel:
            return

        embed = discord.Embed(
            title="313 // DATA_REDACTED",
            description=f"Information removed from the terminal.",
            color=0x000000
        )
        
        embed.add_field(name="USER", value=f"{message.author.mention}", inline=True)
        embed.add_field(name="CHANNEL", value=f"{message.channel.mention}", inline=True)
        embed.add_field(name="CONTENT", value=f"```\n{message.content}\n```", inline=False)
        embed.set_footer(text="GHOST_AUDIT_MODULE // 313 EXFILTRATOR")

        await log_channel.send(embed=embed)

    # --- MONITORAMENTO DE MENSAGENS EDITADAS ---
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        # Ignora se for bot ou se o conteúdo for igual (ex: apenas fixou mensagem)
        if before.author.bot or before.content == after.content:
            return

        log_channel = self.bot.get_channel(LOG_ID)
        if not log_channel:
            return

        embed = discord.Embed(
            title="313 // DATA_MODIFIED",
            description=f"Information altered in the infrastructure.",
            color=0x000000
        )
        
        embed.add_field(name="USER", value=f"{before.author.mention}", inline=True)
        embed.add_field(name="CHANNEL", value=f"{before.channel.mention}", inline=True)
        embed.add_field(name="BEFORE", value=f"```\n{before.content}\n```", inline=False)
        embed.add_field(name="AFTER", value=f"```\n{after.content}\n```", inline=False)
        embed.set_footer(text="GHOST_AUDIT_MODULE // 313 EXFILTRATOR")

        await log_channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GhostCog(bot))
