import telebot
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
    "🎮 Ласкаво просимо до First Bitcoin Game!\n\n"
    "💰 Вхід: 10 USDT\n"
    "🏆 Грай та вигравай Bitcoin!\n\n"
    "▶️ Напиши /play щоб почати")

@bot.message_handler(commands=['play'])
def play(message):
    bot.send_message(message.chat.id,
    "🎰 Гра почалась!\n\n"
    "🍀 Удачі!")

bot.polling()
