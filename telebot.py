import feedparser
import time
import telegram

import os
TOKEN = os.getenv("TOKEN")
CHAT_ID = "@DailyNews20perMinutes"
RSS_URL = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"

bot = telegram.Bot(token=TOKEN)

def fetch_and_send_news():
    feed = feedparser.parse(RSS_URL)
    for entry in feed.entries[:3]:
        title = entry.title
        link = entry.link
        message = f"📰 {title}\n🔗 {link}"
        bot.send_message(chat_id=CHAT_ID, text=message)
        time.sleep(2)

if __name__ == "__main__":
    while True:
        try:
            fetch_and_send_news()
            print("✅ News Sent. Waiting 20 min...")
        except Exception as e:
            print(f"❌ Error: {e}")
        time.sleep(1200)
