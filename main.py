import telebot
from telebot import types
from for_db import BotDB


BOT_TOKEN = ' '
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет, я бот, который сохранит твоё ментальное здоровье! ✨"
                                           "Здесь ты найдёшь: аффирмации, дыхательную гимнастику, "
                                           "звуки природы и музыку для медитации."
                                           "")
    db_cr = BotDB()
    user_id = message.from_user.id
    if not db_cr.check(user_id):
        db_cr.add_us(user_id)
        bot.send_message(message.from_user.id, "регистрация выполнена")
    else:
        bot.send_message(message.from_user.id, "вход выполнен")


@bot.message_handler(commands=['what_is'])
def what(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    medit = types.KeyboardButton('Что такое медитация')
    affirm = types.KeyboardButton('Что такое аффирмация')
    markup.add(medit, affirm)
    bot.send_message(message.from_user.id, "вот ответ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Что такое медитация':
        bot.send_message(message.from_user.id, text='медитация это')
    else:
        bot.send_message(message.from_user.id, text='аффирма это')


bot.polling(none_stop=True, interval=0)
