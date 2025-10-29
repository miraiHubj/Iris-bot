from aiogram import types
from dispatcher import dp
from random import randint

@dp.message_handler(commands=['Выбери', 'Выбирай', 'выбери', 'выбирай'], commands_prefix='/!')
async def process_select_command(message: types.Message):
    com = message.text
    if "!выбери" in com.lower():
        com = com[7:]
    else:
        com = com[8:]
    if com.lower().find("от") != -1:
        if com.lower().find("до") != -1:
            ot = com.lower().find("от") + 2
            sdo = com.lower().find("до") - 1
            edo = com.lower().find("до") + 2
            fcom = com[ot:sdo]
            scom = com[edo:]
            try:
                fcom = int(fcom)
                scom = int(scom)
                answer = randint(fcom, scom)
                await message.answer(f"Я выбираю число {answer}")
            except:
                pass
    elif com.lower().find("или") != -1:
        sor = com.lower().find("или") - 1
        eor = com.lower().find("или") + 4
        fcom = com[1:sor]
        scom = com[eor:]
        answer = randint(1, 2)
        if answer == 1:
            await message.answer(f"Я выбираю {fcom}")
        else:
            await message.answer(f"Я выбираю {scom}")