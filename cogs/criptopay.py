import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÃO ---
ADMIN_IDS = [int(i.strip()) for i in os.getenv('ADMIN_IDS', '1490172068573216831,1490209943826075770,1488612428689182882').split(',')]
MY_WALLET = "SEU_ENDERECO_DE_CARTEIRA_AQUI" # Substitua pela sua carteira
LOG_ID = 1490220486808834118 
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"
STAFF_ID = 1490209943826075770

class PaymentModal(discord.ui.Modal, title='313 // SUBMIT_TRANSACTION'):
    txid = discord.ui.TextInput(
        label='Transaction Hash (TXID)',
        placeholder='Paste the blockchain hash here...',
        min_length=10,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        # 1. Alerta no Canal de Logs
        log_channel = interaction.guild.get_channel(LOG_ID)
        if log_channel:
            embed_log = discord.Embed(
                title="💀 313 // PAYMENT_SUBMITTED",
                description=f"Transaction received for verification in channel {interaction.channel.mention}.",
                color=0xFFFF00
            )
            embed_log.add_field(name="USER", value=f"{interaction.user.mention}", inline=True)
            embed_log.add_field(name="TXID", value=f"```\n{self.txid.value}\n```", inline=False)
            await log_channel.send(embed=embed_log)

        # 2. Resposta no Ticket
        response_ansi = (
            "```fix\n"
            "[ SYSTEM ] : Transaction Hash received.\n"
            "[ STATUS ] : Awaiting manual confirmation by the Deployment Team.\n"
            "```"
        )
        # Menciona a staff no ticket para avisar que o cara pagou
        await interaction.response.send_message(content=f"<@&{STAFF_ID}>", embed=discord.Embed(description=response_ansi, color=0xFFFFFF))

class PaymentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Submit Hash", style=discord.ButtonStyle.gray, custom_id="313:submit_hash", emoji="🔒")
    async def confirm_pay(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(PaymentModal())

class BillingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bill")
    async def bill(self, ctx, plan: str = None):
        """Uso: !bill monthly | !bill lifetime (Apenas no canal de ticket)"""
        # Verificação de Admin
        if ctx.author.id not in ADMIN_IDS:
            return

        if not plan or plan.lower() not in ["monthly", "lifetime"]:
            return await ctx.send("```fix\n[ ERROR ] : Usage: !bill monthly | !bill lifetime\n```", delete_after=5)

        price = "60.00 USDT" if plan.lower() == "monthly" else "550.00 USDT"
        
        embed = discord.Embed(
            title="💀 313 // SECURE_INVOICE",
            description=(
                f"**PLAN:** `{plan.upper()}`\n"
                f"**AMOUNT:** `{price}`\n"
                f"**NETWORK:** `TRC20 (Tron)`\n"
                f"**ADDRESS:** `{MY_WALLET}`\n\n"
                "Transfer the exact amount to the address above.\n"
                "After the transaction, click the button below to submit your hash."
            ),
            color=0x000000
        )
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // ACQUISITION_INTERFACE")

        await ctx.send(embed=embed, view=PaymentView())
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(BillingCog(bot))
