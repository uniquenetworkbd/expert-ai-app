import telebot
import os
import requests
from github import Github

# কনফিগারেশন
TOKEN = os.getenv('BOT_TOKEN') # Render থেকে নেবে
GITHUB_TOKEN = "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"
REPO_NAME = "uniquenetworkbd/expert-ai-app" # আপনার রিপোজিটরি নাম
ADMIN_ID = 5519303439

bot = telebot.TeleBot(TOKEN)
g = Github(GITHUB_TOKEN)

@bot.message_handler(commands=['update_main'])
def update_github_code(message):
    if message.from_user.id == ADMIN_ID:
        try:
            new_code = message.text.replace('/update_main ', '')
            repo = g.get_repo(REPO_NAME)
            contents = repo.get_contents("main.py")
            repo.update_file(contents.path, "Update via Telegram", new_code, contents.sha)
            bot.reply_to(message, "✅ GitHub-এ কোড সফলভাবে আপডেট হয়েছে! এবার সার্ভার রিস্টার্ট হতে ১-২ মিনিট লাগবে।")
        except Exception as e:
            bot.reply_to(message, f"❌ এরর: {str(e)}")
    else:
        bot.reply_to(message, "🚫 আপনার এই কমান্ড দেওয়ার অনুমতি নেই।")

@bot.message_handler(commands=['check_repo'])
def check_repo(message):
    if message.from_user.id == ADMIN_ID:
        repo = g.get_repo(REPO_NAME)
        files = [f.name for f in repo.get_contents("")]
        bot.reply_to(message, f"📂 গিটহাবে বর্তমানে এই ফাইলগুলো আছে:\n\n" + "\n".join(files))

bot.polling(none_stop=True)
