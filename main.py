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
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('Что такое медитация?', url="https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B4%D0%B8%D1%82%D0%B0%D1%86%D0%B8%D1%8F")
    btn2 = types.InlineKeyboardButton('Что такое аффирмация?', url="https://ru.wikipedia.org/wiki/%D0%90%D1%84%D1%84%D0%B8%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F_(%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F)")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, 'Здесь вы узнаете 👇', reply_markup=markup)


@bot.message_handler(commands=['menu'])
def what(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_cont = types.KeyboardButton('Контакты')
    btn_med = types.KeyboardButton('Медитация')
    btn_aff = types.KeyboardButton('Аффирмации')
    markup.add(btn_aff, btn_med, btn_cont)
    bot.send_message(message.from_user.id, "вот ответ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Что такое медитация':
        bot.send_message(message.from_user.id, text='медитация это')
    else:
        bot.send_message(message.from_user.id, text='аффирма это')


bot.polling(none_stop=True, interval=0)
