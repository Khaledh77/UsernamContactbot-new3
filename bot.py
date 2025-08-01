import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

logging.basicConfig(level=logging.INFO)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Assalomu alaykum! Tilni tanlang:\n🇺🇿 /uz\n🇷🇺 /ru\n🇬🇧 /en")

def forward_message(update: Update, context: CallbackContext):
    user = update.message.from_user
    msg = f"📩 Yangi xabar:\n👤 Foydalanuvchi: @{user.username or user.first_name}\n🆔 ID: {user.id}\n\n💬 Xabar: {update.message.text}"
    context.bot.send_message(chat_id=ADMIN_ID, text=msg)
    update.message.reply_text("✅ Xabaringiz yuborилди!")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
