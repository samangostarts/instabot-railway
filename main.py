import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("7245345277:AAG6u2O8KRWa_mc2nUBD1vzAgMUirEm0Fz4")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ ربات فعال شد. خوش‌اومدی!")

def main():
    if not TOKEN:
        print("❌ خطا: متغیر محیطی TELEGRAM_BOT_TOKEN پیدا نشد.")
        return

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🚀 ربات در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()
