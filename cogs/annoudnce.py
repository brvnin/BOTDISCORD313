import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÃO DE ACESSO ---
# Puxa os IDs do seu .env (Garante que você e seus sócios tenham acesso)
ADMIN_IDS_RAW = os.getenv('ADMIN_IDS', '1490172068573216831,1490209943826075770,1488612428689182882')
ADMIN_IDS = [int(i.strip()) for i in ADMIN_IDS_RAW.split(',')]

# Assets Visuais
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"
GHOST = "<:313ghost:1490216288524566608>"

# Canais de Referência
PANEL_REF = "<#1490177743990685908>"
TICKET_REF = "<#1490175695089959053>"

class AnnounceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # --- COMANDO 1: ATUALIZAÇÃO GLOBAL V2 (HÍBRIDO C++/PYTHON) ---
    @commands.command(name="global_news")
    async def global_news(self, ctx):
        if ctx.author.id not in ADMIN_IDS:
            return

        msg_content = f"""
**[  🇺🇸  ENGLISH_TERMINAL ]**
The most respected auditing tool has been refined. 
Engineered with a **High-Performance C++ Core** and an **Agile Python Framework**, 313 is now stealthier and faster.

**⚡ TECH_SPECS & UPDATES:**
> **C++ & Python Hybrid:** Maximum execution speed with zero-footprint delivery.
> **Session Cloning:** Instant access to Telegram, Discord, Steam (Bypass Guard), and more.
> **Zero CMD Stealth:** Operates entirely in the shadows with no visual trace.
> **Anti-Analysis:** 8 layers of protection + Human movement detection.

**⚠️ CHROME_STATUS:** 90% Success rate. Daily C++ engine patches to maintain stability.
*"If it passed through hardware, it now belongs to you."*

---

**[  🇧🇷  TERMINAL_PORTUGUÊS ]**
A ferramenta de auditoria mais respeitada foi refinada. 
Desenvolvida com um **Motor C++ de Alta Performance** e **Framework Python Ágil**, o 313 está mais silencioso e veloz.

**⚡ ESPECIFICAÇÕES & NOVIDADES:**
> **Híbrido C++/Python:** Velocidade máxima de execução com rastro zero no sistema.
> **Clonagem de Sessão:** Acesso instantâneo a Telegram, Discord, Steam e outros.
> **Silêncio Absoluto:** Operação total nas sombras, sem janelas ou rastros visuais.
> **Anti-Análise:** 8 camadas de proteção + Detecção de movimento humano.

**⚠️ STATUS_CHROME:** 90% de sucesso. Manutenção diária no motor C++ para estabilidade.

**🌐 WEB_PANEL:** {PANEL_REF} | **📩 SUPPORT:** {TICKET_REF}
"""

        embed = discord.Embed(
            title=f"{GHOST} 313 // GLOBAL_INFRASTRUCTURE_V2",
            description=msg_content,
            color=0x000000
        )
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // C++ ENGINE // PYTHON FRAMEWORK")

        await ctx.send(content="@everyone", embed=embed)
        try: await ctx.message.delete()
        except: pass

    # --- COMANDO 2: PROTOCOLO DE LIQUIDAÇÃO (VENDA DO PROJETO TRILÍNGUE) ---
    @commands.command(name="liquidation")
    async def project_sale(self, ctx):
        if ctx.author.id not in ADMIN_IDS:
            return

        msg_content = f"""
**[  🇺🇸  FULL PROJECT ACQUISITION ]**
The complete **313 EXFILTRATOR** infrastructure is available for acquisition. A turnkey operation with verified revenue and high-frequency traffic.

**📊 STATS:** +50 Logs every 12h cycle.
**📦 INCLUDES:** C++ Source (Engine + Key System), Web UI Source, Auto-2FA Modules, Active DB, and this configured Discord Bot.

---

**[  🇧🇷  AQUISIÇÃO TOTAL DO PROJETO ]**
Toda a infraestrutura do **313 EXFILTRATOR** está à venda. Operação completa e lucrativa, pronta para uso imediato.

**📊 STATS:** +50 Logs a cada ciclo de 12h.
**📦 INCLUI:** Source C++ (Motor + Sistema de Keys), Source Web UI, Módulos Auto-2FA, Database Ativa e este Bot de Discord.

---

**[  🇷🇺  ПОЛНАЯ ПРОДАЖА ПРОЕКТА ]**
Вся инфраструктура **313 EXFILTRATOR** доступна для покупки. Готовый бизнес с проверенным трафиком и стабильным доходом.

**📊 ПОКАЗАТЕЛИ:** +50 логов каждые 12 часов.
**📦 В КОМПЛЕКТЕ:** Исходный код C++ (Движок + Система ключей), Исходный код Web UI, Модули Auto-2FA, Активная БД и этот Discord бот.

**📩 NEGOTIATION:** Open a ticket at {TICKET_REF}. Serious inquiries only.
"""

        embed = discord.Embed(
            title=f"{GHOST} 313 // PROJECT_LIQUIDATION_PROTOCOL",
            description=msg_content,
            color=0x000000
        )
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // INTERNATIONAL_ASSET_TRANSFER")

        await ctx.send(content="@everyone", embed=embed)
        try: await ctx.message.delete()
        except: pass

# --- INICIALIZAÇÃO DA COG ---
# Esta função setup deve estar fora da classe e sem espaços no início
async def setup(bot):
    await bot.add_cog(AnnounceCog(bot))
