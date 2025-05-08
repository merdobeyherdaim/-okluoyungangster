from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Bot için log ayarları
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Komutlar
def start(update, context):
    update.message.reply_text('Bot aktif!')

def help(update, context):
    update.message.reply_text('Yardım için buradayım!')

def main():
    # Telegram botu için API token
    updater = Updater("YOUR_API_TOKEN", use_context=True)

    dp = updater.dispatcher

    # Komutlar
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Botu başlat
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
