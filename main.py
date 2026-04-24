from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = '8553205225:AAHION1wwLt6-_XrGOT4--ZuYxSDyvPuFCM'

BAD_WORDS = [
    'غحبه', 'امك', 'كلب', 'اسود', 'زنجي', 'عبد', 'كسمك', 'كس', 'دادي', 
    'زربة', 'زمال', 'تاكله', 'تلكلونه', 'هي', 'قندره', 'تبن', 'مطي', 
    'حمار', 'غبي', 'قرد', 'نعال', 'زبالة', 'نغل'
]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    for word in BAD_WORDS:
        if word in text:
            await update.message.delete()
            break

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.run_polling()
    
