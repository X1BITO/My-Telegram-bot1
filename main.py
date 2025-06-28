from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "7866908309:AAG3t8jkQeX_aO6EG3A-M7AOJX12zYlJgZM"
GAME_LINK = "https://www.tirangagames.top/#/register?invitationCode=5714811441601"
CHANNEL_LINK = "https://t.me/+fZ6TAOGhrUVlZGM1"
EARNING_IMAGE = "https://i.imgur.com/NNfBHDl.jpg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 About", callback_data="about")],
        [InlineKeyboardButton("💸 Earn", url=GAME_LINK)]
    ]
    await update.message.reply_text(
        "🎮 *Welcome to the Tiranga God Prediction*\n"
        "👉 [Click here to play](" + GAME_LINK + ")\n\n"
        "*Steps to Earn Money 💰 :*\n"
        "1️⃣ Login in game\n"
        "2️⃣ Add cash 💰\n\n"
        "Enjoy and Win Money! 🏆",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await context.bot.send_photo(
        chat_id=query.message.chat.id,
        photo=EARNING_IMAGE,
        caption=(
            "📈 *How to Play:*\n"
            "1️⃣ Add ₹300–₹500\n"
            "2️⃣ Check daily updates on our Telegram channel\n\n"
            f"🔗 [Join Channel]({CHANNEL_LINK})\n\n"
            "🤑 Follow steps and start earning!"
        ),
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(about))

if __name__ == "__main__":
    print("✅ Bot is running...")
    app.run_polling()
