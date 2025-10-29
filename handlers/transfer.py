from aiogram import types
from dispatcher import bot, dp
import sqlite3

@dp.message_handler(commands=['transfer'])
async def process_giveeclairs_command(message: types.Message):
    rs = False
    try:
        num = int(message.text.split(' ')[2])
    except:
        await message.answer('/transfer ID Число')
        rs = True
    if rs == False:
        try:
            ui = int(message.text.split(' ')[1])
        except:
            await message.answer('/give ID Число')
            rs = True
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    if rs == False:
        try:
            c.execute(f"SELECT user_id, user_nick, user_eclairs FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                uiseller = [el[0], el[1], el[2]]
            
            c.execute(f"SELECT user_id, user_nick, user_eclairs FROM user_data WHERE user_id = {ui}")
            items = c.fetchall()
            for el in items:
                uibuyer = [el[0], el[1], el[2]]
            uibuyer
        except:
            await message.answer('Ошибка, проверьте ID получателя или попробуйте перезапустить бота: /start')
            rs = True
    if rs == False:
        if uiseller[0] == uibuyer[0]:
            await message.answer("Ты по-моему перепутал")
        elif uiseller[2] >= num:
            if num > 0:
                price_eclairs_b = uibuyer[2] + num
                price_eclairs_s = uiseller[2] - num
                
                await message.answer(f"""<b>Пользователь <a href='tg://user?id={uiseller[0]}'>{uiseller[1]}</a></b> перевел <b>{num} эклеров</b> на счет <b><a href='tg://user?id={uibuyer[0]}'>{uibuyer[1]}</a></b>""", parse_mode="HTML")
                await bot.send_message(ui, f"""<b>Пользователь <a href='tg://user?id={uiseller[0]}'>{uiseller[1]}</a></b> перевел <b>{num} эклеров</b> на счет <b><a href='tg://user?id={uibuyer[0]}'>{uibuyer[1]}</a></b>""", parse_mode="HTML")
                c.execute(f"UPDATE user_data SET user_eclairs = {price_eclairs_s} WHERE user_id = {uiseller[0]}")
                c.execute(f"UPDATE user_data SET user_eclairs = {price_eclairs_b} WHERE user_id = {uibuyer[0]}")
            else:
                await message.answer("Минимальная сумма перевода 1 эклер")
        else:
            await message.answer("Недостаточно средств, операция отменена!")
    c.execute(f"SELECT * FROM user_data WHERE user_id = {message.from_user.id}")
    db.commit()
    db.close()