import telebot
import sqlite3
from telebot import types

bot=telebot.TeleBot("8136847790:AAFGRmlafZFqx19YMlZCm9XD7ZJomIjl1YY")
name=None

@bot.message_handler(commands=['journal'])
def help_operation(message):
    markup=types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть журнал',url='https://journal.top-academy.ru/ru/auth/login/index?returnUrl=%2Fru%2Fmain%2Fhomework%2Fpage%2Findex'))

    bot.reply_to(message,'Журнал  будет открыт в вашем браузере',reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_operation(message):
    markup=types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton('Как удалить домашку если уже ее прикрепили',callback_data='homework')
    btn2=types.InlineKeyboardButton('Хочу узнать свои данные от журнала',callback_data='log_in')
    markup.row(btn1,btn2)
    bot.send_message(message.chat.id,'Популярные запросы: ',reply_markup=markup)

@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data=='homework':
        file=open('./homeworkdelete.png','rb')
        bot.send_photo(callback.message.chat.id,file)
        bot.send_message(callback.message.chat.id ,'Вам нужно нажать правой кнопкой мыши и внизу окна найти "Удалить работу".Теперь вы можете заново загрузить домашку если время не прошло')





with sqlite3.connect('./database.db') as db:
    cursor=db.cursor()
    query1="""INSERT INTO expenses (id,name) VALUES (1,'Коммуналка')"""
    query2 = """INSERT INTO expenses (name,id) VALUES ('Бензин',2)"""
    query3 = """INSERT INTO expenses  VALUES (3,'Интернет')"""
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    db.commit()












bot.polling(non_stop=True)