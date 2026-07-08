import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Токен бота и ссылка на тест берутся из переменных окружения (настраиваются на хостинге,
# токен никогда не хранится прямо в коде — это безопаснее)
BOT_TOKEN = os.environ["BOT_TOKEN"]
TEST_LINK = os.environ.get("TEST_LINK", "https://ixtosha-cmd.github.io/Averna_test/")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Привет! 👋\n\nПройдите тест на определение уровня английского по ссылке:\n{TEST_LINK}"
    )


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
