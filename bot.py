import os
import telebot
import random
from datetime import datetime
from threading import Thread
from flask import Flask

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN non impostato")

bot = telebot.TeleBot(TOKEN)

# Questa parte mantiene il bot "vivo" per Render
app = Flask('')

@app.route('/')
def home():
    return "Bot attivo"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, f"Ciao {m.from_user.first_name}!")

@bot.message_handler(commands=['help'])
def help_cmd(m):
    bot.reply_to(m, "Comandi: /start, /help, /time, /random")

@bot.message_handler(commands=['time'])
def time_cmd(m):
    bot.reply_to(m, datetime.now().strftime("%H:%M:%S"))

@bot.message_handler(commands=['random'])
def random_cmd(m):
    bot.reply_to(m, f"🎲 {random.randint(1,100)}")

print("Bot avviato!")
bot.infinity_polling()
