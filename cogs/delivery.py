import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÃO ---
ADMIN_IDS = [int(i.strip()) for i in os.getenv('ADMIN_IDS', '1490172068573216831,1490209943826075770,1488612428689182882').split(',')]
LOG_ID = int(os.getenv('LOG_CHANNEL_ID', 1490220486808834118))
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"

class DeliveryCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sendkey")
    async def send_key(self, ctx, user_id: int, *, key: str):
        """Uso: !sendkey 1234567890 SUAKEY-123-ABC"""
        
        # 1. Verificação de Segurança (Apenas Admins)
        if ctx.author.id not in ADMIN_IDS:
            return

        try:
            # 2. Busca o usuário pelo ID
            user = await self.bot.fetch_user(user_id)
            if not user:
                return await ctx.send("❌ Error: Identity not found in Discord database.", delete_after=5)

            # 3. Embed de Entrega (Privado do Cliente)
            user_embed = discord.Embed(
                title="313 // LICENSE_DELIVERY",
                description="Your secure access key has been successfully generated.",
                color=0xFFFFFF
            )
            user_embed.add_field(name="ACCESS_KEY", value=f"```\n{key}\n```", inline=False)
            user_embed.set_thumbnail(url=LOGO_URL)
            user_embed.set_footer(text="313 EXFILTRATOR // SECURE_DISTRIBUTION")

            # Envia para a DM do cliente
            await user.send(embed=user_embed)

            # 4. Confirmação para o Admin
            await ctx.send(f"✅ Key successfully delivered to **{user.name}**.", delete_after=5)
            await ctx.message.delete()

            # 5. Log de Auditoria (Para você saber o que foi enviado e para quem)
            log_channel = self.bot.get_channel(LOG_ID)
            if log_channel:
                log_embed = discord.Embed(
                    title="313 // ASSET_DISTRIBUTION",
                    description=f"License delivered via encrypted channel.",
                    color=0x000000
                )
                log_embed.add_field(name="OPERATOR", value=f"{ctx.author.mention}", inline=True)
                log_embed.add_field(name="CLIENT", value=f"{user.mention} (`{user.id}`)", inline=True)
                log_embed.add_field(name="KEY_SENT", value=f"||{key}||", inline=False) # Spoiler para proteger a key no log
                await log_channel.send(embed=log_embed)

        except discord.Forbidden:
            # Se a DM do cliente estiver fechada
            await ctx.send(f"❌ Failed: **{user.name}** has their DMs closed.", delete_after=10)
        except Exception as e:
            await ctx.send(f"❌ Error: {e}", delete_after=10)

async def setup(bot):
    await bot.add_cog(DeliveryCog(bot))
