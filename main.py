import telebot
import os
import requests
from telebot import types

# সিকিউর টোকেন (Render এনভায়রনমেন্ট থেকে নেবে)
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# আপনার পার্সোনাল আইডি (অ্যাডমিন কন্ট্রোল)
ADMIN_ID = 5519303439

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("🚀 ওপেন এআই ড্যাশবোর্ড", web_app=types.WebAppInfo("https://uniquenetworkbd.github.io/expert-ai-app/"))
    markup.add(btn)
    
    welcome_text = (
        f"🌟 **ExpertBrain Pro AI-তে স্বাগতম!**\n\n"
        "আমি সরাসরি ক্লাউড থেকে ২৪/৭ সচল। আপনার যেকোনো প্রশ্ন আমাকে করতে পারেন।"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

# --- সুপার অ্যাডমিন কন্ট্রোল (শুধুমাত্র আপনার জন্য) ---
@bot.message_handler(commands=['check'])
def check_github(message):
    if message.from_user.id == ADMIN_ID:
        url = "https://uniquenetworkbd.github.io/expert-ai-app/"
        try:
            r = requests.get(url)
            if r.status_code == 200:
                bot.reply_to(message, "✅ **GitHub Status:** সবকিছু ঠিক আছে! (Status 200)")
            else:
                bot.reply_to(message, f"❌ **GitHub Status:** এরর পাওয়া গেছে! (Code: {r.status_code})")
        except:
            bot.reply_to(message, "❌ **Critical Error:** গিটহাব সাইটে পৌঁছানো যাচ্ছে না।")
    else:
        bot.reply_to(message, "⛔ আপনি এই সিস্টেমের অ্যাডমিন নন।")

@bot.message_handler(commands=['broadcast'])
def broadcast(message):
    if message.from_user.id == ADMIN_ID:
        bot.reply_to(message, "📢 সবাইকে মেসেজ পাঠানোর সিস্টেম লোড হচ্ছে...")
    else:
        bot.reply_to(message, "❌ অ্যাক্সেস ডিনাইড!")

# এআই রেসপন্স হ্যান্ডলার
@bot.message_handler(func=lambda message: True)
def ai_reply(message):
    # আপাতত সিম্পল রেসপন্স, পরে আমরা এখানে Gemini API যুক্ত করব
    bot.reply_to(message, "🤖 আপনার মেসেজটি পেয়েছি। আমি এআই দিয়ে এর উত্তর প্রসেস করছি...")

print("🔥 আপনার সুপার বট এখন চূড়ান্তভাবে সচল!")
bot.polling(none_stop=True)
