import os, time
from instagrapi import Client
from telegram import Bot

TG_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
IG_USER = os.getenv("INSTAGRAM_USERNAME")
IG_PASS = os.getenv("INSTAGRAM_PASSWORD")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")

if not all([TG_TOKEN, IG_USER, IG_PASS, TG_CHAT_ID]):
    print("❌ لطفاً تمام متغیر‌های محیطی را بررسی کن.")
    exit(1)

cl = Client()
cl.login(IG_USER, IG_PASS)
bot = Bot(token=TG_TOKEN)
last_seen = {}

def forwarding_loop():
    threads = cl.direct_threads(amount=5, selected_filter="unread")
    for thread in threads:
        tid = thread.id
        msgs = cl.direct_messages(tid, amount=5)
        for msg in msgs:
            if last_seen.get(tid, 0) < msg.id:
                last_seen[tid] = msg.id
                text = f"📩 از {thread.users[0].username}:\n{msg.text or '<فایل فرستاده شده>'}"
                bot.send_message(chat_id=TG_CHAT_ID, text=text)
                if msg.media:
                    fpath = cl.direct_download(msg.media.pk, folder=".")
                    bot.send_document(chat_id=TG_CHAT_ID, document=open(fpath, 'rb'))

while True:
    forwarding_loop()
    time.sleep(60)
