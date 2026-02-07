import telebot
import os
import requests

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# আপনার আইডি জানার জন্য /id কমান্ড দিন, তারপর সেই নম্বরটি এখানে বসান
ADMIN_ID = 123456789 

@bot.message_handler(commands=['check'])
def check_github(message):
    if message.from_user.id == ADMIN_ID:
        url = "https://uniquenetworkbd.github.io/expert-ai-app/"
        try:
            r = requests.get(url)
            if r.status_code == 200:
                bot.reply_to(message, "✅ GitHub Pages একদম ঠিক আছে! (Status: 200)")
            else:
                bot.reply_to(message, f"❌ GitHub Pages-এ সমস্যা! Error Code: {r.status_code}")
        except:
            bot.reply_to(message, "❌ গিটহাব সার্ভারে পৌঁছানো যাচ্ছে না।")
    else:
        bot.reply_to(message, "⛔ শুধু অ্যাডমিন এই কমান্ড দিতে পারবে।")

@bot.message_handler(commands=['id'])
def get_id(message):
    bot.reply_to(message, f"আপনার আইডি: {message.from_user.id}")

bot.polling(none_stop=True)
