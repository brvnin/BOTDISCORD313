import discord
from discord.ext import commands
import os

ADMIN_IDS_RAW = os.getenv('ADMIN_IDS', '1490172068573216831,1490209943826075770,1488612428689182882')
ADMIN_IDS = [int(i.strip()) for i in ADMIN_IDS_RAW.split(',')]
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"

class PremiumCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="premium")
    async def premium_pricing(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return

        ghost_emoji = "<:313ghost:1490216288524566608>"
        ticket_channel = "<#1490175695089959053>"

        embed = discord.Embed(
            title=f"{ghost_emoji} 313 // CLOUD_PREMIUM",
            description=(
                "Provisioning high-tier infrastructure for advanced auditing operations.\n\n"
                "**[+] MONTHLY_ACCESS**\n"
                "> Price: **$60.00 / Month**\n\n"
                "**[+] LIFETIME_PROVISIONING**\n"
                "> Price: **$550.00**\n\n"
                "**[+] CONTINUOUS_EVOLUTION**\n"
                "Our core engine receives **frequent agile updates** to maintain "
                "100% stability against security mitigations (V137+).\n\n"
                f"**[!] Initialize session at:** {ticket_channel}"
            ),
            color=0x000000 
        )
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // CLOUD_PREMIUM")

        await ctx.send(content="@everyone", embed=embed)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(PremiumCog(bot))
