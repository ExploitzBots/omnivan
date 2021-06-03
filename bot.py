import os
import telebot
import time

bot_token =  "1800288176:AAG7Kwoe_htZKlhwXp2GOI42n3tAqdWRDlw"

telebot.Telebot(token=bot_token)

@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Hello, welcome to Telegram Bot!")

bot.polling()
