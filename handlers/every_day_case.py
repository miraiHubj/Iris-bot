from aiogram import types
from dispatcher import bot, dp
from random import randint
import asyncio
import sqlite3
import datetime

@dp.message_handler(text=['Открыть ежедневный кейс', 'Ежедневный кейс', 'Ек', '!Ежедневка', 'Чапча ежедневка', 'открыть ежедневный кейс', 'ежедневный кейс', 'ек', '!ежедневка', 'чапча ежедневка'])
async def process_auction_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT up_pr, every_day_case FROM game_case WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            pr = el[0]
            evc = el[1]
        c.execute(f"SELECT user_nick, user_coins FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            up = el[1]
        evc = datetime.datetime.strptime(str(evc), '%Y-%m-%d %H:%M:%S')
        date_now = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        date_now = datetime.datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S')
        if date_now >= evc:
            its = []
            for i in range(5):
                its.append("00")
            for i in range(10):
                its.append(randint(10, 99))
            farm = its[-1]
            for i in range(10):
                its.append(randint(10, 99))
            msg = await message.answer(f"""<b>Ежедневный кейс</b>
| 00 | 00 |   00   | 00 | 00 |
                      ⚜️
Открытие через: 3""", parse_mode='HTML')
            for i in range(2):
                await asyncio.sleep(1)
                await msg.edit_text(f"""<b>Ежедневный кейс</b>
| 00 | 00 |   00   | 00 | 00 |
                      ⚜️
Открытие через: {-i+2}""")
            await asyncio.sleep(1)
            for i in range(13):
                if i < 7:
                    await asyncio.sleep(0.1)
                else:
                    await asyncio.sleep(i/13)
                await msg.edit_text(f"""<b>Ежедневный кейс</b>
| {its[i]} | {its[i+1]} |   {its[i+2]}   | {its[i+3]} | {its[i+4]} |
                      ⚜️""")
            price_coins = up + farm
            date_change = datetime.timedelta(days=1)
            date_new = date_now + date_change
            await asyncio.sleep(1)
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {message.from_user.id}")
            c.execute(f"UPDATE game_case SET every_day_case = '{date_new}' WHERE user_id = {message.from_user.id}")
            await msg.edit_text(f"""<b>Ежедневный кейс</b>
| {its[12]} | {its[13]} |   {its[14]}   | {its[15]} | {its[16]} |
                      ⚜️

<a href='tg://user?id={message.from_user.id}'>{un}</a> получил <b>{farm} монет</b> из ежедневного кейса!""", parse_mode="HTML")
        else:
            date2 = str(datetime.datetime.strptime(str(evc), '%Y-%m-%d %H:%M:%S')-datetime.datetime.now())
            secs = date2.split(':')[2].split('.')[0] + ' секунд'
            mins = date2.split(':')[1] + ' минут '
            hours = date2.split(':')[0].split(' ')[-1] + ' часов '
            if hours.find('0') == 0:
                hours = hours[1:]
            if mins.find('0') == 0:
                mins = mins[1:]
            if secs.find('0') == 0:
                secs = secs[1:]
            date1 = ''
            if hours.split(' ')[0] != '0' and hours.split(' ')[0] != '':
                date1 += hours
            if mins.split(' ')[0] != '0' and mins.split(' ')[0] != '':
                date1 += mins
            if secs.split(' ')[0] != '0' and secs.split(' ')[0] != '':
                date1 += secs
            await message.answer(f"Ежедневный кейс появится через {date1}!")
        db.commit()
        db.close()
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")