import discord
from discord.ext import commands
import os

# --- CONFIGURAÇÃO ---
ADMIN_IDS_RAW = os.getenv('ADMIN_IDS', '1490172068573216831,1490209943826075770,1488612428689182882')
ADMIN_IDS = [int(i.strip()) for i in ADMIN_IDS_RAW.split(',')]
LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"

# Canais Oficiais
PANEL_REF = "<#1490177743990685908>"
TICKET_REF = "<#1490175695089959053>"

class AnnounceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="global_news")
    async def global_news(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return
        
        msg = f"""**[  🇺🇸  ]**
The most respected auditing tool has been refined. 
Engineered with a **High-Performance C++ Core** and an **Agile Python Framework**, 313 is now stealthier and faster.

**⚡ TECH_SPECS & UPDATES:**
> **C++ & Python Hybrid:** Maximum execution speed with zero-footprint delivery.
> **Session Cloning:** Instant access to Telegram, Discord, Steam (Bypass Guard), and more.
> **Zero CMD Stealth:** Operates entirely in the shadows with no visual trace.
> **Anti-Analysis:** 8 layers of protection + Human movement detection.
> **Manual Binder:** Now available via support ticket.

**⚠️ CHROME_STATUS:** 90% Success rate. Daily C++ engine patches to maintain stability.
*"If it passed through hardware, it now belongs to you."*

---

**[  🇧🇷  ]**
A ferramenta de auditoria mais respeitada foi refinada. 
Desenvolvida com um **Motor C++ de Alta Performance** e **Framework Python Ágil**, o 313 está mais silencioso e veloz.

**⚡ ESPECIFICAÇÕES & NOVIDADES:**
> **Híbrido C++/Python:** Velocidade máxima de execução com rastro zero no sistema.
> **Clonagem de Sessão:** Acesso instantâneo a Telegram, Discord, Steam e outros.
> **Silêncio Absoluto:** Operação total nas sombras, sem janelas ou rastros visuais.
> **Anti-Análise:** 8 camadas de proteção + Detecção de movimento humano.
> **Serviço de Binder:** Agora disponível via ticket manual.

**⚠️ STATUS_CHROME:** 90% de sucesso. Manutenção diária no motor C++ para estabilidade.
*"Se passou pelo hardware, agora pertence a você."*

**🌐 WEB_PANEL:** {PANEL_REF} | **📩 SUPPORT:** {TICKET_REF}"""

        embed = discord.Embed(
            title="💀 313 // GLOBAL_INFRASTRUCTURE_V2", 
            description=msg, 
            color=0x000000
        )
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // C++ ENGINE // PYTHON FRAMEWORK // NOIR")
        
        await ctx.send(content="@everyone", embed=embed)
        await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(AnnounceCog(bot))
