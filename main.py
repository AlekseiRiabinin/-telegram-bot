from handlers import dp
from aiogram import executor

async def on_start(_):
    print('Bot is running')
    # await dp.bot.send_message(message.from_user.id, f'Chat is joined by {message.from_user.full_name}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)