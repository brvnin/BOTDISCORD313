import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÃO ---
# Endereço da sua carteira (Recomendo USDT - Rede TRC20/Tron)
MY_WALLET = "573079:AAoKFXmc3kJKeT5zFpZzTdyfbwES2K9STvg"
LOG_ID = 1490220486808834118 
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"

class PaymentModal(discord.ui.Modal, title='313 // VERIFY_TRANSACTION'):
    txid = discord.ui.TextInput(
        label='Transaction Hash (TXID)',
        placeholder='Paste the transaction hash here...',
        min_length=10,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        # Envia o log para você verificar
        log_channel = interaction.guild.get_channel(LOG_ID)
        if log_channel:
            embed_log = discord.Embed(
                title="💀 313 // PAYMENT_PENDING_VERIFICATION",
                description=f"A user has submitted a payment for verification.",
                color=0xFFFF00 # Amarelo (Pendente)
            )
            embed_log.add_field(name="USER", value=f"{interaction.user.mention} (`{interaction.user.id}`)", inline=True)
            embed_log.add_field(name="TXID / HASH", value=f"```\n{self.txid.value}\n```", inline=False)
            await log_channel.send(embed=embed_log)

        await interaction.response.send_message(
            "```fix\n[ SYSTEM ] : Hash submitted successfully.\n[ STATUS ] : Waiting for manual verification by the deployment team.\n```", 
            ephemeral=True
        )

class PaymentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Confirm Payment", style=discord.ButtonStyle.green, custom_id="313:confirm_pay", emoji="✔️")
    async def confirm_pay(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(PaymentModal())

class PaymentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="buy")
    async def buy(self, ctx, plan: str = None):
        """Uso: !buy monthly | !buy lifetime"""
        if not plan or plan.lower() not in ["monthly", "lifetime"]:
            return await ctx.send("```fix\n[ ERROR ] : Use !buy monthly or !buy lifetime\n```")

        price = "60.00 USDT" if plan.lower() == "monthly" else "550.00 USDT"
        
        embed = discord.Embed(
            title="💀 313 // PAYMENT_TERMINAL",
            description=(
                f"You are acquiring **{plan.upper()}** access.\n\n"
                f"**AMOUNT:** `{price}`\n"
                f"**NETWORK:** `TRC20 (Tron)`\n"
                f"**ADDRESS:** `{MY_WALLET}`\n\n"
                "*Transfer the exact amount to the address above. After sending, click the button below to submit your transaction hash for verification.*"
            ),
            color=0x000000
        )
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // ENCRYPTED_PAYMENT_v2")

        await ctx.author.send(embed=embed, view=PaymentView())
        await ctx.send(f"✅ {ctx.author.mention}, the payment instructions were sent to your DMs.")

async def setup(bot):
    await bot.add_cog(PaymentCog(bot))
