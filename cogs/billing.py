import discord
from discord.ext import commands
import os
import aiohttp

# --- CONFIGURAÇÃO ---
SELLY_API_KEY = os.getenv('SELLY_API_KEY')
SELLY_EMAIL = os.getenv('SELLY_EMAIL')
TICKET_CATEGORY_ID = int(os.getenv('TICKET_CATEGORY_ID', 1490175576491823164))
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"
GHOST = "<:313ghost:1490216288524566608>"

class BillingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def create_selly_invoice(self, product_id, customer_email):
        url = "https://selly.io/api/v2/pay"
        payload = {
            "product_id": product_id,
            "email": customer_email
            # Gateway deixado em branco para o cliente escolher entre Stripe/Crypto no site
        }
        
        auth = aiohttp.BasicAuth(SELLY_EMAIL, SELLY_API_KEY)
        headers = {"User-Agent": "313-Exfiltrator-Bot/2.0"}
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json=payload, auth=auth, headers=headers) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return data.get('url'), "API_STABLE"
                    else:
                        # Fallback se a API falhar
                        fallback_url = f"https://selly.io/p/{product_id}?email={customer_email}"
                        return fallback_url, f"API_REJECTED_HTTP_{resp.status}_FALLBACK_ACTIVE"
            except Exception:
                fallback_url = f"https://selly.io/p/{product_id}?email={customer_email}"
                return fallback_url, "NETWORK_ERROR_FALLBACK_ACTIVE"

    @commands.command(name="invoice")
    async def generate_invoice(self, ctx, plan: str = None, email: str = None):
        """Gera a fatura dentro do ticket do cliente"""
        
        # 1. Trava de segurança por categoria
        if ctx.channel.category_id != TICKET_CATEGORY_ID:
            return

        # 2. Validação de entrada
        if not plan or not email or plan.lower() not in ["monthly", "lifetime"]:
            return await ctx.send("```fix\n[ USAGE ] : !invoice <monthly/lifetime> <email>\n```")

        await ctx.message.delete()
        status_msg = await ctx.send(f"```ansi\n{GHOST} Connecting to 313 // Billing Infrastructure...```")

        # 3. Mapeamento de IDs do Selly no .env
        prod_id = os.getenv('PRODUCT_ID_MONTHLY') if plan.lower() == "monthly" else os.getenv('PRODUCT_ID_LIFETIME')

        # 4. Processamento da Fatura
        url, log_status = await self.create_selly_invoice(prod_id, email)

        await status_msg.delete()
        
        # 5. Embed Profissional Noir
        embed = discord.Embed(
            title=f"{GHOST} 313 // ACQUISITION_TERMINAL",
            description=(
                f"Infrastructure: **313 // {plan.upper()}**\n"
                f"Client Identity: `{email}`\n"
                f"Network Status: `ENCRYPTED`\n\n"
                "**AVAILABLE_GATEWAYS:**\n"
                "> 💳 **Stripe** (Credit/Debit Card)\n"
                "> ₿ **Bitcoin / Bitcoin Cash**\n"
                "> ♦️ **Ethereum**\n"
                "> Ł **Litecoin**\n\n"
                "Use the terminal below to proceed with the transaction. Access is granted immediately after confirmation.\n\n"
                f"🔗 **[PROCEED TO CHECKOUT]({url})**"
            ),
            color=0x000000
        )
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text=f"TRANSACTION_ID: {log_status} // v2.0")
        
        await ctx.send(content=ctx.author.mention, embed=embed)

async def setup(bot):
    # Correção do carregamento para setup(bot)
    await bot.add_cog(BillingCog(bot))
