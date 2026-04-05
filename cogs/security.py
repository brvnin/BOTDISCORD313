import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÃO ---
# Lista de termos monitorados
BANNED_WORDS = [
    "virus", "vírus", "malware", "trojan", "rat", "keylogger", "worm", 
    "ransomware", "stealer", "binder", "crypter", "exploit", "rootkit", 
    "spyware", "infostealer", "grabber", "token grabber", "logger", 
    "backdoor", "rce", "ddos", "dos attack", "botnet"
]

# Puxa os IDs das variáveis de ambiente
LOG_ID = int(os.getenv('LOG_CHANNEL_ID', 1490220486808834118))
TICKET_CATEGORY_ID = int(os.getenv('TICKET_CATEGORY_ID', 1490175576491823164))

class SecurityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # 1. Ignora se for o próprio bot ou se não for em um servidor
        if message.author.bot or not message.guild:
            return

        # 2. EXCEÇÃO: Ignora a censura se a mensagem for dentro da categoria de TICKETS
        if message.channel.category_id == TICKET_CATEGORY_ID:
            return

        # 3. Ignora se for Administrador (Dono do projeto)
        if message.author.guild_permissions.administrator:
            return

        # 4. Processa o conteúdo da mensagem
        content = message.content.lower()
        
        if any(word in content for word in BANNED_WORDS):
            try:
                # Apaga a mensagem
                await message.delete()

                # Aviso temporário (5 seg)
                embed = discord.Embed(
                    title="313 // SECURITY_FILTER",
                    description=f"{message.author.mention}, your message contained restricted terminology and was redacted.",
                    color=0xFF0000 
                )
                await message.channel.send(embed=embed, delete_after=5)

                # Log de Auditoria
                log_channel = self.bot.get_channel(LOG_ID)
                if log_channel:
                    log_embed = discord.Embed(
                        title="313 // PROTOCOL_VIOLATION",
                        description=(
                            f"**User:** {message.author.mention} (`{message.author.id}`)\n"
                            f"**Channel:** {message.channel.mention}\n"
                            f"**Content:** `{message.content}`\n"
                            f"**Action:** Message Redacted"
                        ),
                        color=0x000000
                    )
                    await log_channel.send(embed=log_embed)

            except Exception as e:
                print(f"ERR_SECURITY: {e}")

async def setup(bot):
    await bot.add_cog(SecurityCog(bot))
