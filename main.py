import os
import time
import telebot
from dotenv import load_dotenv
from commands import register_commands

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

AUFGABEN = {
    1: "💧 Trinke ein Glas Wasser!",
    2: "🏋️ Mache 10 Kniebeugen!",
    3: "😂 Erzähle einen Witz!",
    4: "👉 Bestimme jemanden, der als Nächstes würfeln muss!",
    5: "🎲 Du darfst noch einmal würfeln!",
    6: "🃏 Joker! Du darfst eine Aufgabe ablehnen!"
}

try:
    bot = telebot.TeleBot(TOKEN)
    register_commands(bot)

    @bot.message_handler(commands=["start"])
    def start(message):
        bot.reply_to(
            message,
            "🎲 Willkommen beim Würfelspiel!\n\n"
            "Schreibe /wuerfeln und ich würfle für dich.\n\n"
            "1️⃣ 💧 Trinke ein Glas Wasser\n"
            "2️⃣ 🏋️ Mache 10 Kniebeugen\n"
            "3️⃣ 😂 Erzähle einen Witz\n"
            "4️⃣ 👉 Bestimme jemanden, der als Nächstes würfelt\n"
            "5️⃣ 🎲 Du darfst noch einmal würfeln\n"
            "6️⃣ 🃏 Joker – du darfst eine Aufgabe ablehnen"
        )

    @bot.message_handler(commands=["wuerfeln"])
    def wuerfeln(message):

        # Echten animierten Telegram-Würfel senden
        dice_message = bot.send_dice(
            message.chat.id,
            emoji="🎲"
        )

        # Telegram bestimmt die gewürfelte Zahl
        zahl = dice_message.dice.value

        # Warten, bis die Würfelanimation fertig ist
        time.sleep(4)

        # Passende Aufgabe anzeigen
        bot.send_message(
            message.chat.id,
            f"🎲 Du hast eine {zahl} gewürfelt!\n\n"
            f"{AUFGABEN[zahl]}"
        )

    # Webhook entfernen und Bot starten
    bot.delete_webhook(drop_pending_updates=True)
    bot.infinity_polling()

except Exception as e:
    print(f"FEHLER: {e}")
    while True:
        time.sleep(3600)
