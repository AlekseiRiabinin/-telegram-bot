from loader import dp, bot
from aiogram import types

total = 150
turn = 'Human'

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
        turn = 'Human'
        await bot.send_message(message.from_user.id, f'{total} candies are left on the table')
    else:
        await bot.send_message(message.from_user.id, f'Enter a number less than 28')
               
@dp.message_handler(commands=['robot'])
async def mes_robot(message: types.Message):
    global total
    global turn
    await bot.send_message(message.from_user.id, f"Robot's turn")
    
    count = message.text.split()[1]
    candies = int(count)

    if candies < 28:
        total -= candies
        turn = 'Robot'
        await bot.send_message(message.from_user.id, f'{total} candies are left on the table')
    else:
        await bot.send_message(message.from_user.id, f'Enter a number less than 28')

# @dp.message_handler()
# async def mes_all(message: types.Message):
#     global total
#     global turn
    
#     if message.text.isdigit() and int(message.text) < 28:
#         total -= int(message.text)
#         await bot.send_message(message.from_user.id, f'{total} candies are left on the table')
#     else:
#         await bot.send_message(message.from_user.id, f'Enter a number')        

# @dp.message_handler()
# async def mes_all(message: types.Message):
#     global total
#     global turn
    
#     if message.text.isdigit():
#         total -= int(message.text)
#         await bot.send_message(message.from_user.id, f'{total} candies are left on the table')
#     else:
#         await bot.send_message(message.from_user.id, f'Enter a number')

# @dp.message_handler(commands=['OOP'])
# async def mes_start(message: types.Message):
#     await message.answer(f'Oh, it is really cool') 

# @dp.message_handler(commands=['toxic'])
# async def mes_toxic(message: types.Message):
#     await bot.delete.message(message.from_user.id, message.message_id)
#     await message.answer(f'This is a toxic word')
                    