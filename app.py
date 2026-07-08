import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.environ["BOT_TOKEN"]
TEST_LINK = os.environ.get("TEST_LINK", "https://ixtosha-cmd.github.io/Averna_test/")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(chat_id, text):
    requests.post(f"{TELEGRAM_API}/sendMessage", json={"chat_id": chat_id, "text": text})


@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json(force=True)
    message = update.get("message")
    if message and "text" in message:
        chat_id = message["chat"]["id"]
        text = message["text"]
        if text.startswith("/start"):
            send_message(
                chat_id,
                f"Привет! 👋\n\nПройдите тест на определение уровня английского по ссылке:\n{TEST_LINK}",
            )
    return "ok"


@app.route("/", methods=["GET"])
def health():
    return "Bot is running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
