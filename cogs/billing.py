import discord
from discord.ext import commands
import os
import aiohttp
import asyncio

# --- CONFIGURAÇÃO ---
SELLY_API_KEY = os.getenv('SELLY_API_KEY')
SELLY_EMAIL = os.getenv('SELLY_EMAIL')
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"
GHOST = "<:313ghost:1490216288524566608>"
TICKET_CATEGORY_ID = int(os.getenv('TICKET_CATEGORY_ID', 1490175576491823164))

class BillingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def create_selly_invoice(self, product_id, customer_email):
        """Comunica com a API v2 do Selly para gerar o link de pagamento"""
        url = "https://selly.io/api/v2/pay"
        payload = {
            "product_id": product_id,
            "email": customer_email,
            "gateway": "cryptocurrency" # O Selly abrirá as opções de Crypto
        }
        
        auth = aiohttp.BasicAuth(SELLY_EMAIL, SELLY_API_KEY)
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json=payload, auth=auth) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return data.get('url')
                    else:
                        print(f"SELLY_ERROR: {resp.status}")
                        return None
            except Exception as e:
                print(f"API_EXCEPTION: {e}")
                return None

    @commands.command(name="invoice")
    async def generate_invoice(self, ctx, plan: str = None, email: str = None):
        """Uso: !invoice monthly cliente@email.com"""
        
        # 1. Verificação de Canal (Apenas dentro da categoria de Tickets)
        if ctx.channel.category_id != TICKET_CATEGORY_ID:
            return await ctx.send("```diff\n- ERROR: This command can only be used inside a ticket.\n```", delete_after=5)

        # 2. Validação de Argumentos
        if not plan or not email or plan.lower() not in ["monthly", "lifetime"]:
            return await ctx.send("```fix\n[ USAGE ] : !invoice <monthly/lifetime> <customer_email>\n```")

        await ctx.message.delete()
        status_msg = await ctx.send(f"```ansi\n{GHOST} Initializing secure billing protocol...```")

        # 3. Mapeamento de IDs do Selly
        prod_id = os.getenv('PRODUCT_ID_MONTHLY') if plan.lower() == "monthly" else os.getenv('PRODUCT_ID_LIFETIME')

        # 4. Geração da Fatura
        url = await self.create_selly_invoice(prod_id, email)

        if url:
            await status_msg.delete()
            embed = discord.Embed(
                title=f"{GHOST} 313 // PAYMENT_TERMINAL",
                description=(
                    f"Order initialized for: **313 // {plan.upper()}**\n"
                    f"Customer: `{email}`\n\n"
                    "Please proceed to the secure checkout via the link below. "
                    "Cryptocurrency confirmation is required.\n\n"
                    f"🔗 **[PROCEED TO PAYMENT]({url})**"
                ),
                color=0x000000
            )
            embed.set_thumbnail(url=LOGO_URL)
            embed.set_footer(text="313 SYSTEM // ENCRYPTED_CHECKOUT_V2")
            
            await ctx.send(content=ctx.author.mention, embed=embed)
        else:
            await status_msg.edit(content="```diff\n- CRITICAL_ERROR: Failed to connect to Selly.io API.\n```")

async def setup(bot):
    await bot.add_cog(BillingCog(bot))
