import telebot
import os

# আপনার সঠিক টোকেন
TOKEN = '7992279050:AAHTmfD_0sqgERo4FNZJYmfIz5fgVxrmJSI'
bot = telebot.TeleBot(TOKEN)

# অ্যাডমিন আইডি (এখানে আপনার টেলিগ্রাম আইডি বসান, যা @userinfobot থেকে পাবেন)
ADMIN_ID = 123456789 

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 ExpertBrain AI এখন সরাসরি ক্লাউড থেকে সচল!")

# --- অ্যাডমিন কমান্ড (ডেভলপমেন্টের জন্য) ---
@bot.message_handler(commands=['dev_update'])
def update_system(message):
    if message.from_user.id == ADMIN_ID:
        bot.reply_to(message, "⚙️ সিস্টেম আপডেট করা হচ্ছে... নতুন ফিচার লোড হচ্ছে।")
    else:
        bot.reply_to(message, "❌ আপনি এই কমান্ড ব্যবহারের অনুমতি নেই।")

bot.polling(none_stop=True)
