import discord
from discord.ext import commands
from cogs.ticket import SupportView

LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"
ADMIN_IDS = [1490172068573216831, 1490209943826075770]

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="price")
    async def price(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        
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
        await ctx.message.delete()

    @commands.command(name="deploy")
    @commands.has_permissions(administrator=True)
    async def deploy(self, ctx):
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