import telebot
from telebot import types
import os

# Render-এর Environment থেকে টোকেন নেবে
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# আপনার মিনি অ্যাপের লিঙ্ক
WEB_APP_URL = "https://uniquenetworkbd.github.io/expert-ai-app/"

@bot.message_handler(commands=['start'])
def start(message):
    # ইনলাইন বাটন (Launch Dashboard)
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo(WEB_APP_URL)
    btn = types.InlineKeyboardButton("🚀 Launch AI Dashboard", web_app=web_app)
    markup.add(btn)
    
    welcome_text = (
        f"🌟 **ExpertBrain Pro AI-তে স্বাগতম!**\n\n"
        "আমি এখন সরাসরি ক্লাউড থেকে ২৪/৭ সচল।\n\n"
        "🔹 আপনার আইডি জানতে লিখুন: /id\n"
        "🔹 এআই প্রশ্ন করতে লিখুন: /ask\n"
        "🔹 ড্যাশবোর্ড ওপেন করতে নিচের বাটনে ক্লিক করুন।"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(commands=['id'])
def get_id(message):
    bot.reply_to(message, f"🆔 আপনার টেলিগ্রাম আইডি: `{message.from_user.id}`", parse_mode='Markdown')

@bot.message_handler(commands=['ask'])
def ask_ai(message):
    bot.reply_to(message, "🧠 আমি আপনার প্রশ্ন শোনার জন্য প্রস্তুত। আপনার প্রশ্নটি টাইপ করুন...")

# অন্য যেকোনো মেসেজ আসলে এআই রেসপন্স (টেস্ট)
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, "🤖 আপনার মেসেজটি পেয়েছি। আমি এটি এআই দিয়ে প্রসেস করছি...")

print("✅ বট এখন চূড়ান্তভাবে সচল!")
bot.polling(none_stop=True)
