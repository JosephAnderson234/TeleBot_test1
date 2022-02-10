import os

from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyMarkup


def start(update, context):
    
    boton = InlineKeyboardButton(text="autor", url="https://portafolio2-jacr.web.app")
    
    update.message.reply_text(text="Hello, I'm a bot that can help you to find the best place to eat in your city.\n", reply_markup=InlineKeyboardMarkup([[boton]]))

if __name__ == '__main__':

    updater = Updater(token=os.environ['TOKEN'], use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()

    print('Bot is polling')

    updater.idle()
