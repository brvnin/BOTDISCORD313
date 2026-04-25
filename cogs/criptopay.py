import discord
from discord.ext import commands
import aiohttp
import os

# --- CONFIGURAÇÃO ---
# Pegue o token no @CryptoBot > Crypto Pay > My Apps
CRYPTO_TOKEN = os.getenv('CRYPTO_PAY_TOKEN')
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"

class CryptoPayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def create_invoice(self, amount):
        """Cria uma fatura via API do CryptoBot"""
        url = "https://pay.crypt.bot/api/createInvoice"
        headers = {"Crypto-Pay-API-Token": CRYPTO_TOKEN}
        payload = {
            "asset": "USDT",
            "amount": str(amount),
            "description": "313 // PREMIUN_INFRASTRUCTURE_ACCESS",
            "allow_comments": False
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data['result']['pay_url']
                return None

    @commands.command(name="buy")
    async def buy(self, ctx, plan: str = None):
        """Gera o link de pagamento. Uso: !buy monthly | !buy lifetime"""
        if not plan or plan.lower() not in ["monthly", "lifetime"]:
            return await ctx.send("```fix\n[ ERROR ] : Use !buy monthly or !buy lifetime\n```")

        # Define o valor baseado no plano
        amount = 60 if plan.lower() == "monthly" else 550
        
        await ctx.send("```fix\n[ SYSTEM ] : Initializing encrypted payment gateway...\n```")

        # Chama a API
        pay_url = await self.create_invoice(amount)

        if pay_url:
            embed = discord.Embed(
                title="💀 313 // SECURE_INVOICE",
                description=(
                    f"A private payment terminal for **{plan.upper()}** has been generated.\n\n"
                    f"🔗 **[PROCEED TO TERMINAL]({pay_url})**\n\n"
                    "*Transaction is verified instantly via Telegram CryptoBot.*"
                ),
                color=0x000000
            )
            embed.set_thumbnail(url=LOGO_URL)
            embed.set_footer(text="313 SYSTEM // CRYPTO_PAY_PROTOCOL")
            
            # Envia o link no privado para segurança do cliente
            await ctx.author.send(embed=embed)
            await ctx.send(f"✅ {ctx.author.mention}, invoice delivered to your DMs.")
        else:
            await ctx.send("❌ `API_ERROR`: Could not establish connection with CryptoBot.")

async def setup(bot):
    await bot.add_cog(CryptoPayCog(bot))
