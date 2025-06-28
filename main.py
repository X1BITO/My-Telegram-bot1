from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7866908309:AAG3t8jkQeX_aO6EG3A-M7AOJX12zYlJgZM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Hello! I'm alive and running 24/7!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    print("✅ Bot is running...")
    app.run_polling()
