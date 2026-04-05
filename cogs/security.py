import discord
from discord.ext import commands
import asyncio
import os

# --- CONFIGURAÇÃO DE SEGURANÇA ---
# Lista de termos monitorados (Focada em evitar flags e manter o profissionalismo)
BANNED_WORDS = [
    "virus", "vírus", "malware", "trojan", "rat", "keylogger", "worm", 
    "ransomware", "stealer", "binder", "crypter", "exploit", "rootkit", 
    "spyware", "infostealer", "grabber", "token grabber", "logger", 
    "backdoor", "rce", "ddos", "dos attack", "botnet"
]

LOG_ID = 1490220486808834118  # Seu canal de logs

class SecurityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # 1. Ignora se for o próprio bot ou se não for em um servidor
        if message.author.bot or not message.guild:
            return

        # 2. Ignora se for Admin (opcional, mas recomendado para vocês testarem)
        # Se quiser que censure até os ADMs, apague as duas linhas abaixo
        if message.author.guild_permissions.administrator:
            return

        # 3. Processa o conteúdo da mensagem
        content = message.content.lower()
        
        # Verifica se alguma palavra banida está na mensagem
        if any(word in content for word in BANNED_WORDS):
            try:
                # Apaga a mensagem proibida
                await message.delete()

                # Aviso rápido no chat (Auto-deleta em 5 segundos para manter o chat clean)
                embed = discord.Embed(
                    title="313 // SECURITY_FILTER",
                    description=f"{message.author.mention}, your message contained restricted terminology and was redacted.",
                    color=0xFF0000 # Vermelho para alerta
                )
                await message.channel.send(embed=embed, delete_after=5)

                # Log de Auditoria
                log_channel = self.bot.get_channel(LOG_ID)
                if log_channel:
                    log_embed = discord.Embed(
                        title="313 // PROTOCOL_VIOLATION",
                        description=(
                            f"**User:** {message.author.mention} (`{message.author.id}`)\n"
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
