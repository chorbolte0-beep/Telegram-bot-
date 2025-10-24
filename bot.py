from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Apna BotFather ka token daalo
TOKEN = "YAHAN_APNA_TOKEN_DAALO"

# Apne video links (Telegram file links) yahan daalo
VIDEOS = {
    "video1": "https://t.me/yourchannel/video1link",
    "video2": "https://t.me/yourchannel/video2link"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("👋 Type /start video1 ya /start video2 to get a video.")
        return
    
    key = args[0]
    if key in VIDEOS:
        await update.message.reply_text(f"🎬 Here's your video:\n{VIDEOS[key]}")
    else:
        await update.message.reply_text("❌ Video not found.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🤖 Bot running...")
app.run_polling()
