@commands.command(name="premium")
    async def premium_pricing(self, ctx):
        if ctx.author.id not in ADMIN_IDS: return

        # Configurações do Comando
        ghost_emoji = "<:313ghost:1490216288524566608>"
        ticket_channel_mention = "<#1490175695089959053>"

        embed = discord.Embed(
            title=f"{ghost_emoji} 313 // CLOUD_PREMIUM",
            description=(
                "Provisioning high-tier infrastructure for advanced auditing operations. "
                "The 313 engine is engineered for maximum stealth and bypass efficiency.\n\n"
                "**[+] MONTHLY_ACCESS**\n"
                "> Price: **$60.00 / Month**\n"
                "> *Standard deployment & bypass cycles.*\n\n"
                "**[+] LIFETIME_PROVISIONING**\n"
                "> Price: **$550.00**\n"
                "> *Permanent infrastructure & priority engine access.*\n\n"
                "**[+] CONTINUOUS_EVOLUTION**\n"
                "Our core engine receives **frequent agile updates**. The deployment team "
                "issues real-time patches to maintain 100% stability against the latest "
                "security mitigations and browser updates (V137+).\n\n"
                "**[!] ACQUISITION_PROTOCOL**\n"
                "Payments exclusively via encrypted Crypto channels. "
                f"Initialize your session at: {ticket_channel_mention}"
            ),
            color=0x000000 
        )
        
        embed.set_thumbnail(url=LOGO_URL)
        embed.set_footer(text="313 SYSTEM // CONTINUOUS_DEPLOYMENT // v2.0")

        # Envia com o ping global
        await ctx.send(content="@everyone", embed=embed)
        
        try:
            await ctx.message.delete()
        except:
            pass
