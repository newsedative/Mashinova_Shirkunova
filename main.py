import telebot
from for_db import BotDB


BOT_TOKEN = ' '
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def forward_message(message):
    bot.send_message(message.from_user.id, "Привет, я бот,"
                                           "ТЕКСТ ПРИВЕТСТВИЯ")
    print(message.from_user.id)
    db_cr = BotDB()


bot.polling(none_stop=True, interval=0)
