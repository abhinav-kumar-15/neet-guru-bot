import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! This bot is running 24/7 on Railway.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message.text)

bot.infinity_polling()
