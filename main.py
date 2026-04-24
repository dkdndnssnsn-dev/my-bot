from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = '8400477283:AAHp2XgnTIOPmsGlTuStTSA8S2X5ie1PncQ'

BAD_WORDS = [
    'غحبه', 'امك', 'كلب', 'اسود', 'زنجي', 'عبد', 'كسمك', 'كس', 'دادي', 
    'زربة', 'زمال', 'تاكله', 'تلكلونه', 'هي', 'قندره', 'تبن', 'مطي', 
    'حمار', 'غبي', 'قرد', 'نعال', 'زبالة', 'نغل'
]

async def delete_bad_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.lower()
        for word in BAD_WORDS:
            if word in text:
                try:
                    await update.message.delete()
                    break
                except:
                    pass

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), delete_bad_words))
    app.run_polling()
    
