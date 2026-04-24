import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# إعداد السجلات لمتابعة الأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = '8553205225:AAHION1wwLt6-_XrGOT4--ZuYxSDyvPuFCM'

BAD_WORDS = [
    'غحبه', 'امك', 'كلب', 'اسود', 'زنجي', 'عبد', 'كسمك', 'كس', 'دادي', 
    'زربة', 'زمال', 'تاكله', 'تلكلونه', 'هي', 'قندره', 'تبن', 'مطي', 
    'حمار', 'غبي', 'قرد', 'نعال', 'زبالة', 'نغل'
]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.lower()
        for word in BAD_WORDS:
            if word in text:
                try:
                    await update.message.delete()
                    break
                except Exception as e:
                    print(f"Error deleting message: {e}")

if __name__ == '__main__':
    try:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
        print("Bot is starting...")
        app.run_polling()
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        
