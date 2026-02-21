import telebot
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🎮 Ласкаво просимо до First Bitcoin Game!\n\nНатисни /play щоб почати")

@bot.message_handler(commands=['play'])
def play(message):
    bot.send_message(message.chat.id, "🎰 Ти знайшов 0.00001 BTC!")

@bot.message_handler(commands=['balance'])
def balance(message):
    bot.send_message(message.chat.id, "💰 Твій баланс: 0.00001 BTC")

bot.polling()
