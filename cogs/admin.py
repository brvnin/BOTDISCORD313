import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÃO DE ACESSO ---
ADMIN_IDS_RAW = os.getenv('ADMIN_IDS', '1490172068573216831,1490209943826075770,1488612428689182882')
ADMIN_IDS = [int(i.strip()) for i in ADMIN_IDS_RAW.split(',')]

# Assets Visuais
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"
EXFIL_IMG = "https://cdn.discordapp.com/attachments/1485768180663320597/1491065478062276903/image.png?ex=69d65670&is=69d504f0&hm=8876a69ff9d932752fb88f0bdc095711f5ecbd390c7f4fb629b164dbb5d639af&"
CLOUD_IMG = "https://cdn.discordapp.com/attachments/1490421470914936902/1491971619109998602/0877bf1a-794c-4799-acea-c80777e1fb99.png?ex=69d9a259&is=69d850d9&hm=98dacca578af2c1d4e41cb677ca147f3eae1c7e694183a3e231bb08d3dfce618&"

# Canais e Emojis
TICKET_REF = "<#1490175695089959053>"
PRICE_CH = "<#1490175213646905554>"
GHOST = "<:313ghost:1490216288524566608>"

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="price")
    async def price(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        msg = f"Payments are exclusively via **Cryptocurrency**.\n\nInterested? Open a ticket at: {TICKET_REF}"
        embed = discord.Embed(title="313 // Pricing", description=msg, color=0xFFFFFF)
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name="plans")
    async def plans(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        msg = "Access our official terminal for detailed pricing:\n\n🔗 **[313 // PRICING TERMINAL](https://three13-exfiltrator.onrender.com/#pricing)**"
        embed = discord.Embed(title="313 // Pricing Models", description=msg, color=0xFFFFFF)
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name="deploy")
    @commands.has_permissions(administrator=True)
    async def deploy(self, ctx):
        from cogs.ticket import SupportView
        embed = discord.Embed(title="313 // Support Gateway", description="Initialize a secure session for support inquiries.", color=0xFFFFFF)
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(embed=embed, view=SupportView())
        await ctx.message.delete()

    @commands.command(name="update")
    async def update(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        msg = f"""Effective immediately, acquisition costs have been re-evaluated.

**[+] COST_REDUCTION**
All license tiers adjusted for optimized deployment.

**[+] UPDATED_TERMINAL**
Review the new structure in {PRICE_CH}."""
        embed = discord.Embed(title="💀 313 // PRICE_ADJUSTMENT", description=msg, color=0x000000)
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(content="@everyone", embed=embed)
        await ctx.message.delete()

    @commands.command(name="exfil")
    async def exfil(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        msg = f"""All modules are fully operational. Core engine stable.

Zero detections recorded. Build stability verified.

*Infrastructure is ready. Initialize your deployment now.*"""
        embed = discord.Embed(title="💀 313 // EXFILTRATION_PROTOCOL", description=msg, color=0x000000)
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_image(url=EXFIL_IMG)
        await ctx.send(content="@everyone", embed=embed)
        await ctx.message.delete()

    @commands.command(name="premium")
    async def premium(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        msg = f"""Advanced infrastructure provisioning. Under constant evolution.

**[+] MONTHLY_ACCESS**
> Price: **$60.00 / Month**

**[+] LIFETIME_PROVISIONING**
> Price: **$550.00**

**[!] Initialize at:** {TICKET_REF}"""
        embed = discord.Embed(title=f"{GHOST} 313 // CLOUD_PREMIUM", description=msg, color=0x000000)
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(content="@everyone", embed=embed)
        await ctx.message.delete()

    @commands.command(name="cloud")
    async def cloud(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        msg = f"""Our elite cloud-based infrastructure is now open.

**[+] INFRASTRUCTURE_STATUS:** AVAILABLE
**[+] ACCESS_LEVEL:** PREMIUM

Initialize session at: {TICKET_REF}"""
        embed = discord.Embed(title=f"{GHOST} 313 // CLOUD_DEPLOYMENT", description=msg, color=0x000000)
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_image(url=CLOUD_IMG)
        await ctx.send(content="@everyone", embed=embed)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(AdminCog(bot))
