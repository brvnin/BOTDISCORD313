import discord
from discord.ext import commands
import os

# Pega os IDs do .env e garante que sejam uma lista de números inteiros
ADMIN_IDS_RAW = os.getenv('ADMIN_IDS', '1490172068573216831,1490209943826075770')
ADMIN_IDS = [int(i.strip()) for i in ADMIN_IDS_RAW.split(',')]

LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="price")
    async def price(self, ctx):
        # 1. Verificação de segurança
        if ctx.author.id not in ADMIN_IDS:
            # Envia uma mensagem temporária para você saber que o bot te viu, mas te barrou
            return await ctx.send(f"❌ Seu ID ({ctx.author.id}) não está na lista de ADMIN_IDS.", delete_after=5)
        
        # 2. Embed limpo
        embed = discord.Embed(
            title="313 // Pricing",
            description=(
                "Payments are exclusively via **Cryptocurrency**.\n\n"
                "Interested in an acquisition? Open a ticket at:\n"
                "<#1490175695089959053>"
            ),
            color=0xFFFFFF
        )
        embed.set_thumbnail(url=LOGO_URL)
        
        await ctx.send(embed=embed)
        try:
            await ctx.message.delete()
        except:
            pass # Ignora se não tiver permissão de apagar mensagens

    @commands.command(name="deploy")
    @commands.has_permissions(administrator=True)
    async def deploy(self, ctx):
        # O deploy usa a view que está no ticket.py
        from cogs.ticket import SupportView
        embed = discord.Embed(
            title="313 // Support Gateway",
            description="Initialize a secure session for support or licensing.",
            color=0xFFFFFF
        )
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(embed=embed, view=SupportView())
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(AdminCog(bot))
