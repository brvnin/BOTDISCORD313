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

# Seu domínio customizado do Selly
STORE_DOMAIN = "brvnin.selly.store"

class BillingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def create_selly_invoice(self, product_id, customer_email):
        url = "https://selly.io/api/v2/pay"
        
        # PROTOCOLO DE LIMPEZA: Remove espaços e pontos finais acidentais no e-mail
        email = customer_email.strip().rstrip('.')
        
        payload = {
            "product_id": product_id,
            "email": email
        }
        
        auth = aiohttp.BasicAuth(SELLY_EMAIL, SELLY_API_KEY)
        headers = {"User-Agent": "313-Exfiltrator-Bot/2.0", "Content-Type": "application/json"}
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json=payload, auth=auth, headers=headers) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return data.get('url'), "API_SUCCESS"
                    else:
                        # FALLBACK PARA SEU DOMÍNIO REAL
                        fallback_url = f"https://{STORE_DOMAIN}/product/{product_id}?email={email}"
                        return fallback_url, f"API_REJECTED_{resp.status}_FALLBACK_ACTIVE"
            except Exception:
                fallback_url = f"https://{STORE_DOMAIN}/product/{product_id}?email={email}"
                return fallback_url, "CONNECTION_ERROR_FALLBACK"

    @commands.command(name="invoice")
    async def generate_invoice(self, ctx, plan: str = None, email: str = None):
        if ctx.channel.category_id != TICKET_CATEGORY_ID:
            return

        if not plan or not email or plan.lower() not in ["monthly", "lifetime"]:
            return await ctx.send("```fix\n[ USAGE ] : !invoice <monthly/lifetime> <email>\n```")

        await ctx.message.delete()
        status_msg = await ctx.send(f"```ansi\n{GHOST} Initializing 313 // ACQUISITION_PROTOCOL...```")

        # IDs verificados por você
        prod_id = "77e40edf" if plan.lower() == "monthly" else "bda7f845"

        url, log_status = await self.create_selly_invoice(prod_id, email)
        await status_msg.delete()
        
        # Embed com o link sanitizado
        embed = discord.Embed(
            title=f"{GHOST} 313 // ACQUISITION_TERMINAL",
            description=(
                f"Infrastructure: **313 // {plan.upper()}**\n"
                f"Client Identity: `{email.strip().rstrip('.')}`\n"
                f"Status: `STABLE`\n\n"
                "**AVAILABLE_GATEWAYS:**\n"
                "> 💳 **Stripe** | ₿ **Bitcoin** | ♦️ **Ethereum** | Ł **Litecoin**\n\n"
                "Click the terminal link below to finalize deployment.\n\n"
                f"🔗 **[PROCEED TO CHECKOUT]({url})**"
            ),
            color=0x000000
        )
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text=f"TRX_ID: {log_status} // brvnin.selly.store")
        
        await ctx.send(content=ctx.author.mention, embed=embed)

async def setup(bot):
    await bot.add_cog(BillingCog(bot))
