from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من بات درمانگران هستم 🤖")

if __name__ == '__main__':
    app = ApplicationBuilder().token("8384774071:AAE9l6FUltdLMlRaPLGL4JE-bnUTFjysa3Y").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()