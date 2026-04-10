import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÃO DE ACESSO ---
ADMIN_IDS_RAW = os.getenv('ADMIN_IDS', '1490172068573216831,1490209943826075770,1488612428689182882')
ADMIN_IDS = [int(i.strip()) for i in ADMIN_IDS_RAW.split(',')]

# Assets Visuais
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"
EXFIL_IMAGE = "https://cdn.discordapp.com/attachments/1485768180663320597/1491065478062276903/image.png?ex=69d65670&is=69d504f0&hm=8876a69ff9d932752fb88f0bdc095711f5ecbd390c7f4fb629b164dbb5d639af&"
CLOUD_IMAGE = "https://cdn.discordapp.com/attachments/1490421470914936902/1491971619109998602/0877bf1a-794c-4799-acea-c80777e1fb99.png?ex=69d9a259&is=69d850d9&hm=98dacca578af2c1d4e41cb677ca147f3eae1c7e694183a3e231bb08d3dfce618&"

# Canais de Referência
TICKET_REDIRECT = "<#1490175695089959053>"
PRICES_CHANNEL = "<#1490175213646905554>"
GHOST_EMOJI = "<:313ghost:1490216288524566608>"

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="price")
    async def price(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        embed = discord.Embed(title="313 // Pricing", description=f"Payments are exclusively via **Cryptocurrency**.\n\nInterested? Open a ticket at: {TICKET_REDIRECT}", color=0xFFFFFF)
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name="plans")
    async def plans(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        embed = discord.Embed(title="313 // Pricing Models", description="Access our official terminal for detailed pricing and features:\n\n🔗 **[313 // PRICING TERMINAL](https://three13-exfiltrator.onrender.com/#pricing)**", color=0xFFFFFF)
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name="deploy")
    @commands.has_permissions(administrator=True)
    async def deploy(self, ctx):
        from cogs.ticket import SupportView
        embed = discord.Embed(title="313 // Support Gateway", description="Initialize a secure session for support or licensing inquiries.", color=0xFFFFFF)
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(embed=embed, view=SupportView())
        await ctx.message.delete()

    @commands.command(name="update")
    async def update_announcement(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        embed = discord.Embed(title="💀 313 // PRICE_ADJUSTMENT", description=f"Effective immediately, our acquisition costs have been re-evaluated.\n\n**[+] ACQUISITION_COST_REDUCTION**\nAll license tiers adjusted.\n\n**[+] UPDATED_TERMINAL**\nReview the new structure in {PRICES_CHANNEL}.", color=0x000000)
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // PRICE_UPDATE")
        await ctx.send(content="@everyone", embed=embed)
        await ctx.message.delete()

    @commands.command(name="exfil")
    async def exfiltration_status(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        embed = discord.Embed(title="💀 313 // EXFILTRATION_PROTOCOL", description="All modules are fully operational. Core engine bypassed current mitigations.\n\nZero detections recorded. Build stability verified.\n\n*Infrastructure is ready. Initialize your deployment now.*", color=0x000000)
        embed.set_thumbnail(url=LOGO_URL)
        embed.
