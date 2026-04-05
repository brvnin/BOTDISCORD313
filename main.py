import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

class ExfiltratorBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.guilds = True
        super().__init__(command_prefix=["!", "$"], intents=intents, help_command=None)

    async def setup_hook(self):
        # Carrega os comandos da pasta cogs
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
        
        # Registra o botão para ele ser eterno
        from cogs.ticket import SupportView
        self.add_view(SupportView())

    async def on_ready(self):
        print(f"313 // DISCLOUD_OPERATIONAL: {self.user}")

bot = ExfiltratorBot()

if __name__ == "__main__":
    bot.run(os.getenv('DISCORD_TOKEN'))