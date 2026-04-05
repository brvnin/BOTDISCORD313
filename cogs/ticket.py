import discord
from discord.ext import commands

LOGO_URL = "https://cdn.discordapp.com/emojis/1490216288524566608.webp?size=96"
CATEGORY_ID = 1490175576491823164
STAFF_ID = 1490209943826075770

class SupportView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Initialize Session", style=discord.ButtonStyle.gray, custom_id="313:ticket", emoji="🔒")
    async def init_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        guild = interaction.guild
        
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True, attach_files=True, read_message_history=True),
            guild.get_role(STAFF_ID): discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
        }

        channel = await guild.create_text_channel(
            name=f"313-{interaction.user.name}",
            category=guild.get_channel(CATEGORY_ID),
            overwrites=overwrites
        )

        embed = discord.Embed(
            title="313 // Session Initialized",
            description=f"Welcome {interaction.user.mention}. State your inquiry below.",
            color=0xFFFFFF
        )
        embed.set_thumbnail(url=LOGO_URL)
        
        await channel.send(content=f"{interaction.user.mention} | <@&{STAFF_ID}>", embed=embed)
        await interaction.followup.send(f"✅ Ticket created: {channel.mention}", ephemeral=True)

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(TicketCog(bot))