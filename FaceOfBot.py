import telebot
import conf

bot=telebot.TeleBot(conf.TOKEN)

@bot.message_handler(content_types=['text'])

def main_page(message):

    non = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_write = telebot.types.KeyboardButton("Generate qweschons")
    buttons.add(button_write)

    if conf.mode==0:
        if message.text=='Generate qweschons':
            bot.send_message(message.chat.id,"Write number of qweschon:",reply_markup=non)
            bot.send_message(message.chat.id,"In this version placed qweschons number: 6,8,9 and 10")
            conf.mode=1
        else:
            bot.send_message(message.chat.id,'This is system of generation qweschons.\nVersion: Alfa:0.1',reply_markup=buttons)
    elif conf.mode==1:
        if str.isdigit(message.text):
            if int(message.text)==6 or int(message.text)==8 or int(message.text)==9 or int(message.text)==10:
                conf.var=int(message.text)
                conf.mode=2
                bot.send_message(message.chat.id,"Write quantity of qweschon",reply_markup=non)
            else:
                bot.send_message(message.chat.id,'Error: Invalid question number.',reply_markup=buttons)
                conf.mode=0
        else:
            bot.send_message(message.chat.id,'Error: Not digit.',reply_markup=buttons)
            conf.mode=0
    elif conf.mode==2:
        if str.isdigit(message.text):
            conf.namber=int(message.text)
            conf.mode=0
            conf.qweschons=conf.generation(conf.var,conf.namber)
            for i in conf.qweschons:
                bot.send_message(message.chat.id,i,reply_markup=buttons)
        else:
            bot.send_message(message.chat.id,'Error: Not digit.',reply_markup=buttons)
            conf.mode=0

bot.polling(none_stop=True)