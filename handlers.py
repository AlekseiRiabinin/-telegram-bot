from loader import dp, bot
from aiogram import types
from random import randint

total = 150
turn = ''

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    global human
    global robot

    await message.answer(f'Hi, {message.from_user.first_name}! '
                         f'Have not seen you for a while')                        

@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total

    count = message.text.split()[1]
    total = int(count)
    await message.answer(f'Put {total} candies on the table') 

@dp.message_handler(commands=['human'])
async def mes_human(message: types.Message):
    global total
    global turn
    await bot.send_message(message.from_user.id, f"Human's turn")
    
    count = message.text.split()[1]
    candies = int(count)

    if candies < 28:
        total -= candies
        turn = 'Robot'
        await bot.send_message(message.from_user.id, f'{total} candies are left on the table')
        if total < 29:
            await bot.send_message(message.from_user.id, f'{turn} wins!')    
    else:
        await bot.send_message(message.from_user.id, f'Enter a number less than 28')
               
@dp.message_handler(commands=['robot'])
async def mes_robot(message: types.Message):
    global total
    global turn

    turn = 'Human'
    await bot.send_message(message.from_user.id, f"Robot's turn")

    if total > 57:
        candies = randint(1, 29)
        total -= candies
    
    elif 28 < total < 57:    
        candies = 1
        total -= candies
    
    else:    
        candies = total
        total -= candies
        
    if total < 29:
        await bot.send_message(message.from_user.id, f'{turn} wins!')
    
    await bot.send_message(message.from_user.id, f'{total} candies are left on the table')
                    