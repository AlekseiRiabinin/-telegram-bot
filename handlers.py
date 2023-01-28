from loader import dp, bot
from aiogram import types

total = 150

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Hi, {message.from_user.first_name}! '
                         f'Have not seen you for a while')  

@dp.message_handler(commands=['OOP'])
async def mes_start(message: types.Message):
    await message.answer(f'Oh, it is really cool') 

@dp.message_handler(commands=['toxic'])
async def mes_toxic(message: types.Message):
    await bot.delete.message(message.from_user.id, message.message_id)
    await message.answer(f'This is a toxic word')

@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total

    count = message.text.split()[1]
    total = int(count)
    await message.answer(f'Set {total} candies')                

@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    
    if message.text.isdigit():
        total -= int(message.text)
        await bot.send_message(message.from_user.id, f'{total} candies are left on the table')
    else:
        await bot.send_message(message.from_user.id, f'Enter a number')
    
    # await message.answer(f'Look, what I have caught - {message.text}')    