import os
import telebot
import random
from datetime import datetime
from flask import Flask
from threading import Thread

# ==========================================
# TOKEN SCRITTO DIRETTAMENTE (SOLUZIONE TEST)
# ==========================================
TOKEN = "8262179130:AAExljxX08oGFz2cYuQE6C4FMqNr3cgmiA"

print(f"✅ TOKEN: {TOKEN[:15]}... (prime 15 lettere)")
print(f"✅ Lunghezza token: {len(TOKEN)} caratteri")

bot = telebot.TeleBot(TOKEN)

# Flask per Render
app = Flask('')
@app.route('/')
def home():
    return "Bot attivo"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

Thread(target=run).start()

# Comandi del bot
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
