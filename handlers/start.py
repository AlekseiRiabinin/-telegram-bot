import game
import random
from loader import dp
from aiogram.types import Message

@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer("Let's start the game")
            break
    else:
        # game.new_game = True
        await message.answer(f'Hi, {message.from_user.full_name}! '
                             f'Take candies between 1 and 28')
        my_game = [message.from_user.id, message.from_user.first_name, random.randint(100, 200)]
        game.total.append(my_game)
