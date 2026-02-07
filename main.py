
import telebot
import os

# Render Environment Variable থেকে টোকেন নেবে
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 ExpertBrain AI এখন Render ক্লাউড থেকে পুরোপুরি সচল!\n\nআপনার আইডি জানতে লিখুন: /id")

@bot.message_handler(commands=['id'])
def get_id(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"আপনার টেলিগ্রাম আইডি: {user_id}")

@bot.message_handler(commands=['ask'])
def ask(message):
    bot.reply_to(message, "🤖 আপনার প্রশ্নটি লিখুন, আমি উত্তর দিচ্ছি...")

# এটি বটকে সচল রাখবে
print("বটটি এখন লাইভ...")
bot.polling(none_stop=True)
