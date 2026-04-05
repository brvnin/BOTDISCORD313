import discord
from discord.ext import commands
import os

# Puxa os IDs do seu .env
ADMIN_IDS_RAW = os.getenv('ADMIN_IDS', '1490172068573216831,1490209943826075770,1488612428689182882')
ADMIN_IDS = [int(i.strip()) for i in ADMIN_IDS_RAW.split(',')]
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # COMANDO !PRICE (Pagamentos Crypto)
    @commands.command(name="price")
    async def price(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        embed = discord.Embed(
            title="313 // Pricing",
            description="Payments are exclusively via **Cryptocurrency**.\n\nInterested? Open a ticket at: <#1490175695089959053>",
            color=0xFFFFFF
        )
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    # NOVO COMANDO !PLANS (Link do Site)
    @commands.command(name="plans")
    async def plans(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        embed = discord.Embed(
            title="313 // Pricing Models",
            description="Access our official terminal for detailed pricing and features:\n\n🔗 **[313 // PRICING TERMINAL](https://three13-exfiltrator.onrender.com/#pricing)**",
            color=0xFFFFFF
        )
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    # COMANDO !DEPLOY (Botão de Ticket)
    @commands.command(name="deploy")
    @commands.has_permissions(administrator=True)
    async def deploy(self, ctx):
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
