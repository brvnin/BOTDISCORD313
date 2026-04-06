import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÃO ---
LOG_ID = int(os.getenv('LOG_CHANNEL_ID', 1490220486808834118))
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"

class AuditCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Monitora a entrada de novos usuários no servidor"""
        
        log_channel = self.bot.get_channel(LOG_ID)
        if not log_channel:
            return

        # Cálculo da idade da conta (Útil para auditoria de segurança)
        created_at = discord.utils.format_dt(member.created_at, style='R') # Ex: "há 2 anos"
        
        embed = discord.Embed(
            title="313 // INBOUND_CONNECTION",
            description=f"New identity detected in the infrastructure.",
            color=0x000000 # Preto total
        )
        
        embed.set_thumbnail(url=LOGO_URL)
        
        embed.add_field(name="USER", value=f"{member.mention}", inline=True)
        embed.add_field(name="ID", value=f"`{member.id}`", inline=True)
        embed.add_field(name="ACCOUNT_AGE", value=created_at, inline=False)
        
        # Rodapé com o total de membros atualizado
        embed.set_footer(text=f"Total Personnel: {member.guild.member_count} // AUDIT_INTERFACE")

        try:
            await log_channel.send(embed=embed)
        except Exception as e:
            print(f"ERR_LOG_JOIN: {e}")

async def setup(bot):
    await bot.add_cog(AuditCog(bot))
