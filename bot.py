import logging
from telegram.ext import Application, CommandHandler
import os

# توکن ربات شما
TOKEN = os.environ.get("TELEGRAM_TOKEN", "8225568589:AAEpqqIkWIdjduKb4Nete6gRav2A84Vohvc")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update, context):
    """تابع پاسخ‌دهی به دستور /start"""
    user_first_name = update.effective_user.first_name
    welcome_message = f"سلام {user_first_name}، خوش اومدی به ربات تحلیل تکنیکال آریان ترید! ✨"
    await update.message.reply_text(welcome_message)
    await update.message.reply_text("برای شروع تحلیل، نام ارز مورد نظر را به انگلیسی (مثلاً **BTCUSDT**) ارسال کنید.")

def main():
    """تابع اصلی برای اجرای ربات."""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling() 

if __name__ == '__main__':
    main()
