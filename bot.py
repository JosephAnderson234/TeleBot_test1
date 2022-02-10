import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatAction

INPUT = 0

def start(update, context):
    
    boton = InlineKeyboardButton(text="autor", url="https://portafolio2-jacr.web.app")
    
    update.message.reply_text(text="Hello, I'm a bot that can help you to find the best place to eat in your city.\n", reply_markup=InlineKeyboardMarkup([[boton]]))


"""QR main"""
def generate_qr(text):
    filename = text + ".jpg"
    qrcode.make(text).save(filename)
    
    return filename

def send_qr(filename, chat):
    chat.send_action(action=ChatAction.UPLOAD_PHOTO, timeout=None)
    chat.send_photo(
        photo=open(filename, 'rb')
    )
    os.unlink(filename)

"""Mensajes main"""
def qr_genrator(update, context):
    update.message.reply_text(text="Envia el texto para generar el qr")
    return INPUT

def input_text(update, context):
    text = update.message.text
    chat = update.message.chat
    filename = generate_qr(text)
    send_qr(filename, chat)
    
    return ConversationHandler.END
    
    
if __name__ == '__main__':

    updater = Updater(token=os.environ['TOKEN'], use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('qr', qr_genrator)
        ],
        
        states={
            INPUT: [MessageHandler(Filters.text, input_text)]
        },
        
        fallbacks={}
    ))
    
    updater.start_polling()

    updater.idle()
