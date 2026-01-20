import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@balanova1"  # ← ЗАМЕНИ

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id

    try:
        member = bot.get_chat_member(CHANNEL, user_id)

        if member.status in ["member", "administrator", "creator"]:
           with open("guide1.pptx.pdf", "rb") as file:
                bot.send_document(
                message.chat.id,
                file,
            caption="Спасибо за подписку! Вот твой файл❤️"
            )
        else:
            bot.send_message(
                message.chat.id,
                "❌ Подпишись на канал тут https://t.me/balanova1 и нажми /start"
            )

    except:
        bot.send_message(
            message.chat.id,
            "⚠️ Не могу проверить подписку"
        )

bot.polling()
