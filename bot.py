import logging
import time
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from commands.kick import kick
from commands.unban import unban
from commands.help_cmd import help_command
from commands.info import info
from commands.ttp import ttp
from commands.lirik import lirik
from commands.ass import ass
from commands.boobs import boobs
from commands.hboobs import hboobs
from commands.ipinfo import ipinfo
from commands.darkgen import darkgen
from commands.darkweather import darkweather
from commands.defdark import defdark
from commands.darkquote import darkquote
from commands.ping import ping
from commands.uptime import uptime
from commands.nsfw import nsfw
from commands.ai_kyo import ai_kyo
from commands.ban import ban     

TOKEN = "8130076025:AAH4L1ozSiEm8mdZE7-36YwQFFUf9L0wQ3k"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔮 Bienvenue dans DarkAI Bot.\nTape /help pour voir les commandes.")

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    app.bot_data["start_time"] = time.time()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(CommandHandler("kick", kick))
    app.add_handler(CommandHandler("unban", unban))
    app.add_handler(CommandHandler("ban", ban))           # ← ajout handler ban

    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("ipinfo", ipinfo))

    app.add_handler(CommandHandler("ttp", ttp))
    app.add_handler(CommandHandler("lirik", lirik))
    app.add_handler(CommandHandler("ass", ass))
    app.add_handler(CommandHandler("boobs", boobs))
    app.add_handler(CommandHandler("hboobs", hboobs))

    app.add_handler(CommandHandler("darkgen", darkgen))
    app.add_handler(CommandHandler("darkweather", darkweather))
    app.add_handler(CommandHandler("defdark", defdark))
    app.add_handler(CommandHandler("darkquote", darkquote))

    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("uptime", uptime))
    app.add_handler(CommandHandler("nsfw", nsfw))
    app.add_handler(CommandHandler(["ai", "kyo"], ai_kyo))

    logging.info("✅ Bot lancé et prêt à répondre ✨")
    app.run_polling()

if __name__ == "__main__":
    main()
