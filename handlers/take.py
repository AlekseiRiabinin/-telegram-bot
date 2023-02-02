from loader import dp
from aiogram.types import Message
import game
import random

@dp.message_handler()
async def mes_help(message: Message):
    for duel in game.total:

        if message.from_user.id == duel[0]:

            count = message.text
            if count.isdigit() and 0 < int(count) < 29:
                duel[2] -= int(count)
                
                if await check_win(message, message.from_user.first_name, duel):
                    return True
                
                await message.answer(f'{duel[1]} takes {count} candies, so {duel[2]} candies are on the table\n'
                                     f"Now, bot's turn")
                bot_take = random.randint(1, 28) if duel[2] > 28 else duel[2]
                duel[2] -= bot_take
                
                if await check_win(message, 'Bot', duel):
                    return True
                
                await message.answer(f'Bot takes {bot_take} candies, '
                                     f'so {duel[2]} candies are on the table\n'
                                     f'Now, your turn')
            else:
                await message.answer(f'Enter a number between 1 and 28')

async def check_win(message: Message, win: str, duel: list):
    if duel[2] <= 0:
        await message.answer(f'{win} wins! Congrats!')
        game.total.remove(duel)
        return True
    
    return False
