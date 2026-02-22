import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("💰 Баланс"),
        KeyboardButton("🎮 Грати")
    )
    markup.add(
        KeyboardButton("💳 Поповнити"),
        KeyboardButton("📊 Статистика")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Ласкаво просимо до First Bitcoin Game!",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda message: message.text == "💰 Баланс")
def balance(message):
    bot.send_message(message.chat.id, "Ваш баланс: 0 BTC")

@bot.message_handler(func=lambda message: message.text == "🎮 Грати")
def play(message):
    bot.send_message(message.chat.id, "🎰 Гра скоро буде доступна!")

@bot.message_handler(func=lambda message: message.text == "💳 Поповнити")
def deposit(message):
    bot.send_message(message.chat.id, "💳 Надішліть BTC на адресу:\nYOUR_BTC_ADDRESS")

@bot.message_handler(func=lambda message: message.text == "📊 Статистика")
def stats(message):
    bot.send_message(message.chat.id, "📊 Статистика поки порожня.")

bot.infinity_polling()
