import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Обработчик /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🛒 Оформить заказ", url="https://t.me/DVA_Izhevsk?text=Здравствуйте! Хочу оформить заказ на квадроцикл Senki 200"),
            InlineKeyboardButton("💬 Получить консультацию", url="https://t.me/DVA_Izhevsk?text=Здравствуйте! Хочу получить консультацию по квадроциклу Senki 200")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open("senki.jpg", "rb"),
        caption=(
            "🚀 *Квадроцикл Senki 200*

"
            "✅ 200 куб. см
"
            "✅ Гарантия 3 года
"
            "✅ Доставка по Ижевску и области
"
            "🎁 Шлем в подарок
"
            "💰 *Цена со скидкой — уточняйте в сообщении!*

"
            "👇 Выберите действие:"
        ),
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    TOKEN = os.getenv("TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
