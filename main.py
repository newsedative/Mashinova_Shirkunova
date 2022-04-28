import telebot
from telebot import types
from for_db import BotDB


BOT_TOKEN = ' '
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "<b>Привет, я бот, который сохранит твоё ментальное здоровье! ✨</b>\n"
                                           "\n"
                                           "Здесь ты найдёшь: аффирмации, дыхательную гимнастику,"
                                           "звуки природы и музыку для медитации.\n"
                                           "\n"
                                           "Чтобы узнать, что бот умеет напиши слеш /\n"
                                           "Чтобы перейти к возможностям бота \n"
                                           "/commands\n"
                                           "Если есть вопросы пиши /help", parse_mode='html')
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


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, 'Я умею петь')


@bot.message_handler(commands=['commands'])
def what(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_cont = types.KeyboardButton('Контакты ☎️')
    btn_med = types.KeyboardButton('Выбрать часть суток')
    markup.add(btn_med, btn_cont)
    bot.send_message(message.from_user.id, "вот ответ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Контакты ☎️':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Вконтакте', url='https://vk.com/feed')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'здесь можно связаться с нами', reply_markup=markup)
    elif message.text == 'Выбрать часть суток' or message.text == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('утро/день')
        btn2 = types.KeyboardButton('вечер/ночь')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'выбирайте', reply_markup=markup)
    elif message.text == 'утро/день':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('аффирмация на день')
        btn2 = types.KeyboardButton('дыхательная практика')
        btn3 = types.KeyboardButton('назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'предлагаем вам взбодрится', reply_markup=markup)
    elif message.text == 'вечер/ночь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('медитация')
        btn2 = types.KeyboardButton('дыхательная практика')
        btn3 = types.KeyboardButton('назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'предлагаем вам расслабиться', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'idk')


bot.polling(none_stop=True, interval=0)
