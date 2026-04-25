import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

class ExfiltratorBot(commands.Bot):
    def __init__(self):
        # Configuração de Intenções (Permissões totais para o bot)
        intents = discord.Intents.default()
        intents.message_content = True  # Para ler comandos e palavras banidas
        intents.members = True          # Para logs de entrada e permissões de ticket
        intents.guilds = True           # Para gerenciar canais
        
        super().__init__(
            command_prefix=["!", "$"], 
            intents=intents, 
            help_command=None
        )

    async def setup_hook(self):
        """
        Este método roda uma única vez quando o bot liga.
        Ele carrega os módulos e registra os botões para serem permanentes.
        """
        print("--- STARTING_MODULE_LOAD_SEQUENCE ---")
        
        # 1. Carrega automaticamente todos os arquivos da pasta 'cogs'
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f"[ SUCCESS ] : Module '{filename}' loaded.")
                except Exception as e:
                    print(f"[ ERROR ] : Failed to load module '{filename}'. | {e}")

        # 2. Registro de Views Persistentes (Botões que nunca param de funcionar)
        # Importamos aqui dentro para evitar erros de importação cíclica
        try:
            from cogs.ticket import SupportView
            from cogs.billing import PaymentView
            
            self.add_view(SupportView())
            self.add_view(PaymentView())
            print("[ SUCCESS ] : Persistent Views registered.")
        except Exception as e:
            print(f"[ WARNING ] : Could not register views. (Ignore if modules are missing) | {e}")

    async def on_ready(self):
        """Disparado quando o bot está online e conectado"""
        print("------------------------------------------")
        print(f"313 // TERMINAL_ONLINE: {self.user}")
        print(f"ID: {self.user.id}")
        print(f"DISCLOUD_STATUS: OPERATIONAL")
        print("------------------------------------------")
        
        # Define o status do bot no Discord
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, 
                name="313 // AUDIT_SESSIONS"
            )
        )

# --- INICIALIZAÇÃO ---
bot = ExfiltratorBot()

if __name__ == "__main__":
    TOKEN = os.getenv('DISCORD_TOKEN')
    
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("CRITICAL_ERROR: DISCORD_TOKEN not found in environment variables.")
