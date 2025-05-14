from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Bot berhasil dijalankan!')

def main():
    updater = Updater(token=7203731424:AAHXnB7tI9f_yVJlSpdHYTdpfe6r_AUZ3q8, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
