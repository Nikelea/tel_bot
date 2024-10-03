from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import logging
from fetchURL import fetch_currency 


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = '7224445218:AAEynHDYMSoEzl5KBfK5b2bngZuxHS4Qdro'

class BotState:
    def __init__(self):
        self.last_message = ""

    async def start(self, update: Update, context):
        await update.message.reply_text('Добрый день! Как вас зовут?')

    async def build_message(self, update: Update, context):
        self.user_name = update.message.text
        get_exchange_rate = await fetch_currency()
        exchange_rate = get_exchange_rate.get('USDRUB')
        try:
            if '.' in exchange_rate:
                number = float(exchange_rate) 
            else:
                number = int(exchange_rate)
        except ValueError:
            message = 'Не удалось получить свежий курс доллара. Попробуйте позже.'
        message = f'Рад знакомству, {self.user_name}! Курс доллара сегодня:  {number:.2f}'
        await update.message.reply_text(message)

def main():
    bot_state = BotState()
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', bot_state.start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot_state.build_message))
    application.run_polling()


if __name__ == '__main__':
    main()

