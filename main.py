from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes

# التوكن الخاص ببوتك
TOKEN = "8400477283:AAFCGqltH8kyTl46814rhTWZMysw2Tcy7c"

async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # التأكد من أن الرسالة تحتوي على نص
    if not update.message or not update.message.text:
        return
        
    text = update.message.text
    
    # قائمة الكلمات المحظورة (أضف هنا أي كلمات عربية تريد منعها)
    bad_words = ["كلمة1", "كلمة2", "كلمة3"]
    
    for word in bad_words:
        if word in text:
            # حذف الرسالة
            await update.message.delete()
            # إرسال تحذير
            await update.message.reply_text(f"عذراً {update.message.from_user.first_name}، هذا اللفظ ممنوع في المجموعة!")
            break

if __name__ == '__main__':
    # إعداد البوت وتشغيله
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), check_message))
    app.run_polling()
  
