import os
from dotenv import load_dotenv
import keep_alive
from gemini_bot import DISCORD_BOT_TOKEN, bot
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if __name__ == '__main__':
    keep_alive.keep_alive()  # Corrected function call
    bot.run(DISCORD_BOT_TOKEN)
  
