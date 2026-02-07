import telebot
from telebot import types
import os

# Render Environment Variable থেকে টোকেন নেবে
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# আপনার GitHub ড্যাশবোর্ড লিঙ্ক
WEB_APP_URL = "https://uniquenetworkbd.github.io/expert-ai-app/"

# --- কমান্ডগুলো সেট করা ---
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # বাটন ১: ড্যাশবোর্ড
    web_app = types.WebAppInfo(WEB_APP_URL)
    btn1 = types.InlineKeyboardButton("🚀 ওপেন ড্যাশবোর্ড", web_app=web_app)
    
    # বাটন ২: সাহায্য
    btn2 = types.InlineKeyboardButton("🆘 হেল্প", callback_data="help")
    
    # বাটন ৩: সাবস্ক্রিপশন
    btn3 = types.InlineKeyboardButton("💳 প্রিমিয়াম", callback_data="premium")
    
    markup.add(btn1)
    markup.add(btn2, btn3)

    welcome_msg = (
        f"👋 স্বাগতম, {message.from_user.first_name}!\n\n"
        "ExpertBrain AI এখন পুরোপুরি প্রস্তুত। নিচের মেনু থেকে আপনার কাঙ্ক্ষিত সেবাটি বেছে নিন।"
    )
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup)

@bot.message_handler(commands=['id'])
def show_id(message):
    bot.reply_to(message, f"🆔 আপনার ইউজার আইডি: `{message.from_user.id}`", parse_mode='Markdown')

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "💡 **কিভাবে ব্যবহার করবেন?**\n\n"
        "১. /start - বট চালু করতে।\n"
        "২. /id - আপনার আইডি দেখতে।\n"
        "৩. /ask - এআই কে প্রশ্ন করতে।\n"
        "৪. /dashboard - সরাসরি অ্যাপ ওপেন করতে।"
    )
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')

# বাটন ক্লিক হ্যান্ডলার
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "help":
        bot.answer_callback_query(call.id, "হেল্প মেনু ওপেন হচ্ছে...")
        help_command(call.message)
    elif call.data == "premium":
        bot.send_message(call.message.chat.id, "👑 প্রিমিয়াম ফিচারগুলো বর্তমানে ডেভেলপ করা হচ্ছে। শীঘ্রই আসছে!")

print("✅ বটের সব মেনু এখন সচল!")
bot.polling(none_stop=True)
