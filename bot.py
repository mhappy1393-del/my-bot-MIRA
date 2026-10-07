import threading
from flask import Flask
from rubika import Robot

TOKEN = "CGBJCA0RDCHIMVGATJJMLDRWNTVYFHNOKJUIRHJRDBNQZJCCHWKESMVQRKBLSCUK"

# راه‌اندازی ربات
bot = Robot(
    token=TOKEN,
    enable_offset=True
)

@bot.on_message()
async def handler(bot, message):
    text = message.text
    chat_id = message.chat_id

    print("پیام:", text)

    if text == "/start":
        await bot.send_message(
            chat_id,
            "می‌خوای با من حرف بزنی؟\n\n"
            "برای فعالیت‌های جدید بنویس: فعالیت های جدید\n"
            "برای پشتیبانی مستقیم بنویس: پشتیبانی مستقیم"
        )

    elif text == "فعالیت های جدید":
        await bot.send_message(
            chat_id,
            "Mira تقدیم می‌کند\n\n"
            "ما در چنل آپارات در حال ساخت ویدیو هستیم و در کانال در حال پست گذاشتن.\n\n"
            "سؤال دیگری دارید؟ بنویسید پشتیبانی مستقیم"
        )

    elif text == "پشتیبانی مستقیم":
        await bot.send_message(
            chat_id,
            "🛠️ پشتیبانی مستقیم:\n@mohmmahre"
        )


# ساخت یک وب‌سرور کوچک برای جلوگیری از خاموش شدن ربات در Render
app = Flask(name)

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run_web():
    # Render به طور خودکار به پورت اختصاصی نیاز دارد، فلاسْک روی پورت ۸۰۸۰ اجرا می‌شود
    app.run(host="0.0.0.0", port=8080)


if name == "main":
    # اجرای وب‌سرور در یک بخش پس‌زمینه (Thread)
    t = threading.Thread(target=run_web)
    t.start()
    
    print("ربات و وب‌سرور روشن شدند ✅")
    bot.run()