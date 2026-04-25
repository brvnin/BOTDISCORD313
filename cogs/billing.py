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
        # Endpoint oficial V2
        url = "https://selly.io/api/v2/pay"
        
        payload = {
            "product_id": product_id,
            "email": customer_email,
            "gateway": "cryptocurrency"
        }
        
        # Selly exige Basic Auth: E-mail como usuário e API Key como senha
        auth = aiohttp.BasicAuth(SELLY_EMAIL, SELLY_API_KEY)
        
        headers = {
            "User-Agent": "313-Exfiltrator-Bot/2.0",
            "Content-Type": "application/json"
        }
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, json=payload, auth=auth, headers=headers) as resp:
                    response_text = await resp.text()
                    
                    if resp.status == 200:
                        data = await resp.json()
                        return data.get('url'), None
                    else:
                        # Retorna o código do erro para diagnóstico
                        return None, f"HTTP_{resp.status}: {response_text[:100]}"
            except Exception as e:
                return None, str(e)

    @commands.command(name="invoice")
    async def generate_invoice(self, ctx, plan: str = None, email: str = None):
        if ctx.channel.category_id != TICKET_CATEGORY_ID:
            return

        if not plan or not email or plan.lower() not in ["monthly", "lifetime"]:
            return await ctx.send("```fix\n[ USAGE ] : !invoice <monthly/lifetime> <email>\n```")

        await ctx.message.delete()
        status_msg = await ctx.send(f"```ansi\n{GHOST} Negotiating with Selly.io Terminal...```")

        # Puxa IDs do .env
        prod_id = os.getenv('PRODUCT_ID_MONTHLY') if plan.lower() == "monthly" else os.getenv('PRODUCT_ID_LIFETIME')

        url, error_log = await self.create_selly_invoice(prod_id, email)

        if url:
            await status_msg.delete()
            embed = discord.Embed(
                title=f"{GHOST} 313 // PAYMENT_TERMINAL",
                description=(
                    f"Plan: **313 // {plan.upper()}**\n"
                    f"Destination: `{email}`\n\n"
                    "Secure link generated. Click below to complete the acquisition via Cryptocurrency.\n\n"
                    f"🔗 **[PROCEED TO CHECKOUT]({url})**"
                ),
                color=0x000000
            )
            embed.set_thumbnail(url=LOGO_URL)
            await ctx.send(content=ctx.author.mention, embed=embed)
        else:
            # Mostra o erro técnico para você saber o que está errado
            await status_msg.edit(content=f"```diff\n- SELLY_API_FAILURE\n- REASON: {error_log}\n```")

async def setup(bot):
    await bot.add_cog(BillingCog(bot))
