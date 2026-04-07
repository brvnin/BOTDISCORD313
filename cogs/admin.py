import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÃO DE ACESSO ---
ADMIN_IDS_RAW = os.getenv('ADMIN_IDS', '1490172068573216831,1490209943826075770,1488612428689182882')
ADMIN_IDS = [int(i.strip()) for i in ADMIN_IDS_RAW.split(',')]

# Assets Visuais
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"
EXFIL_IMAGE = "https://cdn.discordapp.com/attachments/1485768180663320597/1491065478062276903/image.png?ex=69d65670&is=69d504f0&hm=8876a69ff9d932752fb88f0bdc095711f5ecbd390c7f4fb629b164dbb5d639af&"

# Canais de Referência
TICKET_REDIRECT = "<#1490175695089959053>"
PRICES_CHANNEL = "<#1490175213646905554>"

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # --- COMANDO !PRICE ---
    @commands.command(name="price")
    async def price(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        embed = discord.Embed(
            title="313 // Pricing",
            description=f"Payments are exclusively via **Cryptocurrency**.\n\nInterested in an acquisition? Open a ticket at: {TICKET_REDIRECT}",
            color=0xFFFFFF
        )
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    # --- COMANDO !PLANS ---
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

    # --- COMANDO !DEPLOY ---
    @commands.command(name="deploy")
    @commands.has_permissions(administrator=True)
    async def deploy(self, ctx):
        from cogs.ticket import SupportView
        embed = discord.Embed(
            title="313 // Support Gateway",
            description="Initialize a secure session for support or licensing inquiries.",
            color=0xFFFFFF
        )
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(embed=embed, view=SupportView())
        await ctx.message.delete()

    # --- COMANDO !UPDATE ---
    @commands.command(name="update")
    async def update_announcement(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        embed = discord.Embed(
            title="💀 313 // PRICE_ADJUSTMENT",
            description=(
                "Effective immediately, our acquisition costs have been re-evaluated "
                "to optimize deployment accessibility.\n\n"
                "**[+] ACQUISITION_COST_REDUCTION**\n"
                "All license tiers have been adjusted for optimized deployment.\n\n"
                "**[+] UPDATED_TERMINAL**\n"
                f"Review the new pricing structure in {PRICES_CHANNEL}.\n\n"
                "*Infrastructure optimized. Operation efficiency increased.*"
            ),
            color=0x000000 
        )
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // NOIR INDUSTRIAL // PRICE_UPDATE")
        await ctx.send(content="@everyone", embed=embed)
        await ctx.message.delete()

    # --- COMANDO !EXFIL (VERSÃO CLEAN) ---
    @commands.command(name="exfil")
    async def exfiltration_status(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return

        embed = discord.Embed(
            title="💀 313 // EXFILTRATION_PROTOCOL",
            description=(
                "All modules are fully operational. Our core engine has successfully "
                "bypassed current mitigations. Operation stable.\n\n"
                "Zero detections recorded. Build stability is verified across all targets.\n\n"
                "*Infrastructure is ready. Initialize your deployment now.*"
            ),
            color=0x000000 
        )
        
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_image(url=EXFIL_IMAGE)
        embed.set_footer(text="313 SYSTEM // NOIR INDUSTRIAL // SYSTEM_STABLE")

        await ctx.send(content="@everyone", embed=embed)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(AdminCog(bot))
