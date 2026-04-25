import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÃO ---
ADMIN_IDS_RAW = os.getenv('ADMIN_IDS', '1490172068573216831,1490209943826075770,1488612428689182882')
ADMIN_IDS = [int(i.strip()) for i in ADMIN_IDS_RAW.split(',')]
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"

class FaqCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="faq_crypto")
    async def crypto_tutorial(self, ctx):
        if ctx.author.id not in ADMIN_IDS:
            return

        msg_content = f"""
**[  🇺🇸  HOW TO ACQUIRE CRYPTO ]**
To access 313 infrastructure, you need **USDT (Network: TRC20)**. Follow these steps for a fast acquisition:

**1. FASTEST METHOD (MoonPay / Transak):**
> Use [MoonPay.com](https://www.moonpay.com/) or [Transak.com](https://transak.com/).
> You can buy using Credit/Debit Card or Apple/Google Pay.
> Select **USDT (TRON Network)** and send it directly to the wallet provided in your ticket.

**2. EXCHANGE METHOD (Binance / Kraken):**
> Create an account on [Binance.com](https://www.binance.com/).
> Purchase USDT via P2P or Credit Card.
> Withdraw the funds using the **TRC20 (TRON)** network to our address.

**⚠️ WARNING:** Always double-check the network (**TRC20**). Funds sent to the wrong network will be permanently lost.

---

**[  🇧🇷  COMO COMPRAR CRYPTO ]**
Para adquirir o 313, você precisa de **USDT (Rede: TRC20)**. Siga os passos abaixo:

**1. MÉTODO RÁPIDO (MoonPay - Aceita PIX):**
> Acesse [MoonPay.com](https://www.moonpay.com/).
> Selecione **USDT (Rede TRON)**.
> Insira o valor do plano e pague via **PIX**.
> Cole a carteira fornecida pelo bot no seu ticket como destino.

**2. MÉTODO TRADICIONAL (Binance):**
> Compre USDT na Binance via PIX.
> Vá em 'Sacar', escolha **USDT** e obrigatoriamente a rede **TRON (TRC20)**.
> Insira o endereço da nossa carteira.

**⚠️ AVISO:** Use apenas a rede **TRC20**. Transferências via redes erradas não podem ser estornadas.
"""

        embed = discord.Embed(
            title="💀 313 // CRYPTO_ACQUISITION_PROTOCOL",
            description=msg_content,
            color=0x000000
        )
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // FINANCIAL_EDUCATION // NOIR")

        await ctx.send(embed=embed)
        try:
            await ctx.message.delete()
        except:
            pass
@commands.command(name="faq_qr")
    async def qr_tutorial(self, ctx):
        if ctx.author.id not in ADMIN_IDS:
            return

        msg_content = f"""
**[  🇺🇸  QR_CODE SCAN PROTOCOL ]**
Follow these steps to complete your acquisition using the terminal's QR Code:

**1. OPEN YOUR WALLET:**
> Use your mobile crypto app (Binance, Trust Wallet, Exodus, or Kraken).
**2. SCAN:**
> Tap the **'Scan'** icon and aim your camera at the QR Code displayed in your ticket.
**3. VERIFY SPECS:**
> Asset: **USDT** | Network: **TRC20 (Tron)**.
> Ensure the amount matches the selected plan.
**4. CONFIRM & SUBMIT:**
> After sending, copy the **Transaction ID (Hash/TXID)**.
> Click the **'Submit Hash'** button below the invoice and paste it.

---

**[  🇧🇷  PROTOCOLO DE ESCANEAMENTO ]**
Siga os passos abaixo para pagar usando o QR Code do terminal:

**1. ABRA SUA CARTEIRA:**
> Use o app da sua exchange ou carteira no celular (Binance, Trust, Exodus, etc).
**2. ESCANEAR:**
> Toque no ícone de **'Escanear/Scan'** e aponte a câmera para o QR Code no seu ticket.
**3. VERIFIQUE OS DADOS:**
> Moeda: **USDT** | Rede: **TRC20 (Tron)**.
> Certifique-se de que o valor está correto.
**4. CONFIRME E ENVIE:**
> Após o envio, copie o **ID da Transação (Hash/TXID)**.
> Clique no botão **'Submit Hash'** abaixo da fatura e cole o código.
"""

        embed = discord.Embed(
            title="💀 313 // SCAN_PAYMENT_TUTORIAL",
            description=msg_content,
            color=0x000000
        )
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // LOGISTICS_SUPPORT // NOIR")

        await ctx.send(embed=embed)
        try:
            await ctx.message.delete()
        except:
            pass

async def setup(bot):
    await bot.add_cog(FaqCog(bot))
