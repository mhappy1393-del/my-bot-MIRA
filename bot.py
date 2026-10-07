from rubka import Robot

TOKEN = "CGBJCA0RDCHIMVGATJJMLDRWNTVYFHNOKJUIRHJRDBNQZJCCHWKESMVQRKBLSCUK"

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

print("ربات روشن شد ✅")
bot.run()
