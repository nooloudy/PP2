import telebot
from telebot import types


TOKEN = '6097379695:AAH0pi3cO6dQcMS3-Mevud1l2y6u4nmuPHI' #bot token from @BotFather

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    mess_start = f'Welcomeee, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess_start , parse_mode = 'html')

bot.polling(none_stop = True)

