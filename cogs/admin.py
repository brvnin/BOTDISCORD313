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

    # --- COMANDO !PRICE ---
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
            description="Initialize a secure session for support or licensing.",
            color=0xFFFFFF
        )
        embed.set_thumbnail(url=LOGO_URL)
        await ctx.send(embed=embed, view=SupportView())
        await ctx.message.delete()

    # --- NOVO COMANDO !UPDATE (COLEI AQUI EMBAIXO) ---
    @commands.command(name="update")
    async def update_announcement(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return

        # Canal de preços mencionado pelo ID
        prices_channel = "<#1490175213646905554>"

        embed = discord.Embed(
            title="💀 313 // PRICE_ADJUSTMENT",
            description=(
                "We have re-evaluated our infrastructure costs. Effective immediately, "
                "the barrier to entry for **313 EXFILTRATOR** has been reduced.\n\n"
                "**[+] ACQUISITION_COST_REDUCTION**\n"
                "All license tiers have been adjusted for optimized deployment.\n\n"
                "**[+] UPDATED_TERMINAL**\n"
                f"Review the new pricing structure in {prices_channel}.\n\n"
                "**[+] SYSTEM_EFFICIENCY**\n"
                "Higher accessibility. Same elite performance.\n\n"
                "*Infrastructure optimized. Operation efficiency increased.*"
            ),
            color=0x000000 
        )
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // NOIR INDUSTRIAL // PRICE_UPDATE")

        # Enviamos o @everyone fora da embed para o ping funcionar
        await ctx.send(content="@everyone", embed=embed)
        
        try:
            await ctx.message.delete()
        except:
            pass

#!exfil
@commands.command(name="exfil")
    async def exfiltration_status(self, ctx):
        # Verificação de segurança (Apenas Admins)
        if ctx.author.id not in ADMIN_IDS:
            return

        # URL da imagem=
        EXFIL_IMAGE = "https://cdn.discordapp.com/attachments/1485768180663320597/1491065478062276903/image.png?ex=69d65670&is=69d504f0&hm=8876a69ff9d932752fb88f0bdc095711f5ecbd390c7f4fb629b164dbb5d639af&"

        embed = discord.Embed(
            title="💀 313 // EXFILTRATION_PROTOCOL",
            description=(
                "All systems are fully operational. Our core engine has successfully "
                "bypassed current mitigations. Data exfiltration and bypass protocols "
                "are stable and verified.\n\n"
                "**[+] ENGINE_STATUS:** 100% OPERATIONAL\n"
                "**[+] BYPASS_STABILITY:** VERIFIED (V137+)\n"
                "**[+] DATA_ROUTING:** ACTIVE\n\n"
                "Our deployment team has confirmed that all exfiltration modules "
                "are firing correctly. Zero detections recorded in current builds.\n\n"
                "*Infrastructure is ready. Initialize your deployment now.*"
            ),
            color=0x000000 
        )
        
        # Logo pequena no canto
        embed.set_thumbnail(url=LOGO_URL)
        
        # print
        embed.set_image(url=EXFIL_IMAGE)
        
        embed.set_footer(text="313 SYSTEM // NOIR INDUSTRIAL // SYSTEM_STABLE")

        # Ping everyone fora da embed para notificar
        await ctx.send(content="@everyone", embed=embed)
        
        try:
            await ctx.message.delete()
        except:
            pass
# --- FIM DA CLASSE (NÃO MEXA AQUI) ---
async def setup(bot):
    await bot.add_cog(AdminCog(bot))


