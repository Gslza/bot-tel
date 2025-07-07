from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv(7848401336:AAFydhkyUvPLuDd5tkDX_vVTk8jtnQ37exs)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! Ketik /github untuk lihat GitHub saya."
    )

async def github(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "GitHub saya: https://github.com/Gslza"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("github", github))
    app.run_polling()

if __name__ == "__main__":
    main()
