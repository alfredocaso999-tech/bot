import os
import telebot
import random
from datetime import datetime
from flask import Flask
from threading import Thread

# ---------------------------
#  QUESTO È UN TEST. TI MANDA SUBITO UN MESSAGGIO
# ---------------------------
TOKEN = os.environ.get("BOT_TOKEN")

print(f"🔍 [DEBUG] Il token ricevuto da Render è: {TOKEN}")
print(f"🔍 [DEBUG] Il token inizia con: {str(TOKEN)[:15]}...")

if not TOKEN:
    print("❌ [DEBUG] TOKEN MANCANTE! Render non lo sta passando.")
    raise RuntimeError("BOT_TOKEN non impostato su Render!")

# ---------------------------
#  BOT
# ---------------------------
bot = telebot.TeleBot(TOKEN)

# ---------------------------
#  FLASK (per Render)
# ---------------------------
app = Flask('')

@app.route('/')
def home():
    return "✅ Bot attivo"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

Thread(target=run).start()
# ---------------------------

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

print("🚀 Bot avviato!")
bot.infinity_polling()
