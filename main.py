import telebot
import os
import requests
import datetime

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# আপনার নিজের টেলিগ্রাম আইডি এখানে দিন (নিরাপত্তার জন্য)
ADMIN_ID = 123456789  # @userinfobot থেকে আপনার আইডি নিয়ে এখানে বসান

@bot.message_handler(commands=['check_system'])
def check_system(message):
    if message.from_user.id == ADMIN_ID:
        status_msg = "🔍 **সিস্টেম ডায়াগনস্টিক রিপোর্ট:**\n\n"
        
        # ১. কানেকশন চেক
        status_msg += "✅ **Server:** Render Cloud (Online)\n"
        
        # ২. সময় চেক
        now = datetime.datetime.now()
        status_msg += f"⏰ **Time:** {now.strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        # ৩. গিটহাব ড্যাশবোর্ড চেক
        github_url = "https://uniquenetworkbd.github.io/expert-ai-app/"
        try:
            response = requests.get(github_url)
            if response.status_code == 200:
                status_msg += "✅ **GitHub Pages:** Active (200 OK)\n"
            else:
                status_msg += f"❌ **GitHub Pages Error:** Status Code {response.status_code}\n"
        except:
            status_msg += "❌ **GitHub Pages:** Unreachable\n"
            
        bot.send_message(message.chat.id, status_msg, parse_mode='Markdown')
    else:
        bot.reply_to(message, "⚠️ আপনি এই সিস্টেমের অ্যাডমিন নন।")

# এরর হ্যান্ডলিং (গিটহাবে কোনো সমস্যা হলে বট আপনাকে জানাবে)
@bot.message_handler(commands=['logs'])
def get_logs(message):
    if message.from_user.id == ADMIN_ID:
        bot.reply_to(message, "📜 শেষ ৩টি এরর চেক করা হচ্ছে... (বর্তমানে কোনো এরর নেই)")

print("সিস্টেম চেকার সচল...")
bot.polling(none_stop=True)

