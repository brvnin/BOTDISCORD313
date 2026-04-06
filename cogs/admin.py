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

@commands.command(name="update")
    async def update_announcement(self, ctx):
        # Verificação de segurança (Apenas Admins)
        if ctx.author.id not in ADMIN_IDS:
            return

        embed = discord.Embed(
            title="💀 313 // UPDATE_V1.0.4",
            description=(
                "The 313 core engine has been refined. This update prioritizes "
                "stealth, customization, and deployment precision.\n\n"
                "**[+] CUSTOM ICON INJECTION**\n"
                "Direct .ico patching into binary. Full compatibility with Bypass V137+.\n\n"
                "**[+] WEBHOOK PING**\n"
                "Immediate signal upon build completion. Confirmation delivered to your endpoint.\n\n"
                "**[+] EXPANDED COMPATIBILITY**\n"
                "Enhanced URL validation for discordapp.com domains & automatic sanitization.\n\n"
                "**[+] NOIR CLEAN INTERFACE**\n"
                "Brutalist UI overhaul. Streamlined support access and navigation.\n\n"
                "**[+] BUILD FEEDBACK**\n"
                "Visual 'Generating Binary' indicators for real-time process monitoring.\n\n"
                "*System updated silently. Reload your dashboard to initialize build.*"
            ),
            color=0x000000 # Preto absoluto (Noir)
        )
        
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // NOIR INDUSTRIAL // NEXT GEN AUDITING")

        # Envia no canal onde o comando foi digitado (ou você pode fixar o ID do canal de anúncios)
        await ctx.send(embed=embed)
        
        try:
            await ctx.message.delete() # Apaga o comando !update para manter o log limpo
        except:
            pass
