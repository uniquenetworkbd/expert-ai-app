/update_main import telebot
import os
import google.generativeai as genai
from github import Github

# কনফিগারেশন
TOKEN = os.getenv('BOT_TOKEN')
GEMINI_KEY = "AIzaSyBweVJAfOeGZNLcW_gCQOS48sPpP9zM6fM" # আপনার এপিআই কি সেট করে দিলাম
GITHUB_TOKEN = "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"
REPO_NAME = "uniquenetworkbd/expert-ai-app"
ADMIN_ID = 5519303439

# এআই ও বট সেটআপ
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(TOKEN)
g = Github(GITHUB_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 আমি এখন সম্পূর্ণ বুদ্ধিসম্পন্ন এআই! আমাকে যেকোনো প্রশ্ন করুন।")

@bot.message_handler(commands=['check_repo'])
def check_repo(message):
    if message.from_user.id == ADMIN_ID:
        repo = g.get_repo(REPO_NAME)
        files = [f.name for f in repo.get_contents("")]
        bot.reply_to(message, f"📂 বর্তমান ফাইলসমূহ:\n" + "\n".join(files))

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        sent_msg = bot.reply_to(message, "🧠 ভাবছি...")
        response = model.generate_content(message.text)
        bot.edit_message_text(response.text, chat_id=message.chat.id, message_id=sent_msg.message_id)
    except Exception as e:
        bot.edit_message_text("❌ এআই এই মুহূর্তে উত্তর দিতে পারছে না।", chat_id=message.chat.id, message_id=sent_msg.message_id)

bot.polling(none_stop=True)
