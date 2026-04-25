import discord
from discord.ext import commands
import os
import aiohttp

# --- CONFIGURAÇÃO ---
# Certifique-se de que estas chaves estão no seu painel do Discloud
SELLY_API_KEY = os.getenv('SELLY_API_KEY')
SELLY_EMAIL = os.getenv('SELLY_EMAIL')
TICKET_CATEGORY_ID = int(os.getenv('TICKET_CATEGORY_ID', 1490175576491823164))
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"
GHOST = "<:313ghost:1490216288524566608>"

class BillingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def create_direct_invoice(self, product_id, customer_email):
        """Gera uma fatura (Invoice) via API V2"""
        url = "https://selly.io/api/v2/pay"
        
        # Sanitização rigorosa do e-mail
        clean_email = customer_email.strip().lower().rstrip('.')
        
        payload = {
            "product_id": product_id,
            "email": clean_email,
            "gateway": None # Permite que o cliente escolha no checkout
        }
        
        # Autenticação padrão Selly (Basic Auth)
        auth = aiohttp.BasicAuth(SELLY_EMAIL, SELLY_API_KEY)
        
        headers = {
            "User-Agent": "313-Exfiltrator-Bot/2.0",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json=payload, auth=auth, headers=headers) as resp:
                    data = await resp.json()
                    if resp.status == 200 and 'url' in data:
                        # Retorna o link da Fatura (ex: selly.io/i/abc123)
                        return data['url'], "SUCCESS"
                    else:
                        error_msg = data.get('error', f"HTTP_{resp.status}")
                        return None, error_msg
            except Exception as e:
                return None, str(e)

    @commands.command(name="invoice")
    async def generate_invoice(self, ctx, plan: str = None, email: str = None):
        # 1. Trava de Segurança (Só funciona em Tickets)
        if ctx.channel.category_id != TICKET_CATEGORY_ID:
            return

        # 2. Validação
        if not plan or not email or plan.lower() not in ["monthly", "lifetime"]:
            return await ctx.send("```fix\n[ USAGE ] : !invoice <monthly/lifetime> <email>\n```")

        await ctx.message.delete()
        status_msg = await ctx.send(f"```ansi\n{GHOST} [ SYSTEM ] : Provisioning unique payment session...```")

        # 3. IDs do Selly
        prod_id = "77e40edf" if plan.lower() == "monthly" else "bda7f845"

        # 4. Geração do Link de Checkout Direto
        invoice_url, log_status = await self.create_direct_invoice(prod_id, email)

        await status_msg.delete()

        if invoice_url:
            # Embed de Elite - Focada no Checkout
            embed = discord.Embed(
                title=f"{GHOST} 313 // SECURE_CHECKOUT",
                description=(
                    f"A private payment session has been initialized for your inquiry.\n\n"
                    f"**SPECIFICATIONS:**\n"
                    f"> **Project:** 313 EXFILTRATOR\n"
                    f"> **Plan:** {plan.upper()}\n"
                    f"> **User:** `{email.lower()}`\n\n"
                    "**INSTRUCTIONS:**\n"
                    "1. Click the button below.\n"
                    "2. Select your preferred Gateway (Stripe/Crypto).\n"
                    "3. Complete the transaction.\n\n"
                    f"🔗 **[OPEN PAYMENT TERMINAL]({invoice_url})**"
                ),
                color=0x000000
            )
            embed.set_thumbnail(url=LOGO_URL)
            embed.set_footer(text="313 SYSTEM // ENCRYPTED_PAYMENT_GATEWAY")
            
            await ctx.send(content=f"{ctx.author.mention} | **Action Required**", embed=embed)
        else:
            # Caso a API falhe, o bot avisa o Admin silenciosamente
            await ctx.send(f"```diff\n- API_CONNECTION_ERROR\n- REASON: {log_status}\n```", delete_after=10)
            print(f"DEBUG: Selly Error: {log_status}")

async def setup(bot):
    await bot.add_cog(BillingCog(bot))
