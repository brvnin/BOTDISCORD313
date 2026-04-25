import discord
from discord.ext import commands
import os
import aiohttp

# --- CONFIGURAÇÃO ---
SELLY_API_KEY = os.getenv('SELLY_API_KEY')
SELLY_EMAIL = os.getenv('SELLY_EMAIL')
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"

class BillingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def create_selly_order(self, product_id, email):
        """Comunica com a API do Selly para gerar uma fatura"""
        url = "https://selly.io/api/v2/pay"
        payload = {
            "product_id": product_id,
            "email": email,
            "gateway": "bitcoin" # Você pode deixar vazio para o cliente escolher ou fixar um
        }
        headers = {
            "Authorization": f"Basic {SELLY_API_KEY}", # Nota: Selly pode exigir Auth customizada
            "Content-Type": "application/json"
        }
        
        # Como o Selly exige autenticação específica, usaremos o formato de API Key simples
        auth = aiohttp.BasicAuth(SELLY_EMAIL, SELLY_API_KEY)

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, auth=auth) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('url') # Link da fatura
                return None

    @commands.command(name="buy")
    async def buy_product(self, ctx, plan: str = None):
        """Uso: !buy monthly ou !buy lifetime"""
        if not plan or plan.lower() not in ["monthly", "lifetime"]:
            return await ctx.send("```fix\n[ ERROR ] : Usage: !buy monthly | !buy lifetime\n```")

        # IDs dos produtos
        prod_id = os.getenv('PRODUCT_ID_MONTHLY') if plan.lower() == "monthly" else os.getenv('PRODUCT_ID_LIFETIME')

        await ctx.send(f"```ansi\n[1;37m313 // BILLING_PROTOCOL{0}\nInitializing secure invoice for {plan}...```")

        # Criar a ordem (Usando o e-mail do cliente ou um placeholder)
        # O Selly exige um e-mail para enviar o produto após a compra
        invoice_url = await self.create_selly_order(prod_id, "customer@313exfiltrator.com")

        if invoice_url:
            embed = discord.Embed(
                title="💀 313 // INVOICE_GENERATED",
                description=(
                    f"Your private payment terminal for **{plan.upper()}** is ready.\n\n"
                    f"🔗 **[PROCEED TO CHECKOUT]({invoice_url})**\n\n"
                    "*All transactions are processed through encrypted channels.*"
                ),
                color=0x000000
            )
            embed.set_thumbnail(url=LOGO_URL)
            embed.set_footer(text="313 SYSTEM // SELLY_INTEGRATION")
            await ctx.author.send(embed=embed) # Envia no privado para discrição
            await ctx.send(f"✅ {ctx.author.mention}, your secure invoice was sent to your DMs.")
        else:
            await ctx.send("❌ Failed to generate invoice. Please open a ticket.")

async def setup(bot):
    await bot.add_cog(BillingCog(bot))
