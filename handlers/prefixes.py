from aiogram import types
from dispatcher import dp
import sqlite3

@dp.message_handler(commands=['prefixes', 'pref'])
async def process_balance_command(message: types.Message):
    await message.answer("""<b>Префиксы:</b>

1. <code>Новичок</code> - 10 000 эклеров
2. <code>Бревно</code> - 25 000 эклеров
3. <code>Фермер</code> - 50 000 эклеров
4. <code>Кликер</code> - 100 000 эклеров
5. <code>Олдик</code> - 500 000 эклеров
6. <code>Бронза</code> - 750 000 эклеров
7. <code>Серебряный</code> - 1 500 000 эклеров
8. <code>Голд</code> - 1 750 000
9. <code>Платина</code> - 3 000 000 эклеров
10. <code>Бриллиант</code> - 5 000 000 эклеров
11. <code>Помощник</code> - 10 000 000 эклеров
12. <code>Кодер</code> - 5 000 фрибасов
13. <code>Овнер</code> - 10 000 фрибасов
14. <code>Сударь</code> - 1 000 чапчей
15. <code>Донатер</code> - 100 000 чапчей

/buyprefix Префикс - купить префикс""", parse_mode="HTML")

#qsbuyprefix
@dp.message_handler(commands=['buyprefix'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        pr = message.text[11:]
        c.execute(f"SELECT user_prefix, user_job FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for p in items:
            up = p[0]
            work = el[1]
        if up == 'НоуНейм':
            pn = 0
        elif up == 'Новичок':
            pn = 1
        elif up == 'Бревно':
            pn = 2
        elif up == 'Фермер':
            pn = 3
        elif up == 'Кликер':
            pn = 4
        elif up == 'Олдик':
            pn = 5
        elif up == 'Бронза':
            pn = 6
        elif up == 'Серебряный':
            pn = 7
        elif up == 'Голд':
            pn = 8
        elif up == 'Платина':
            pn = 9
        elif up == 'Бриллиант':
            pn = 10
        elif up == 'Помощник':
            pn = 11
        elif up == 'Кодер':
            pn = 12
        elif up == 'Овнер':
            pn = 13
        elif up == 'Сударь':
            pn = 14
        elif up == 'Донатер':
            pn = 15
        else:
            pn = 16
        
        if pr == 'НоуНейм':
            prn = 0
        elif pr == 'Новичок':
            prn = 1
        elif pr == 'Бревно':
            prn = 2
        elif pr == 'Фермер':
            prn = 3
        elif pr == 'Кликер':
            prn = 4
        elif pr == 'Олдик':
            prn = 5
        elif pr == 'Бронза':
            prn = 6
        elif pr == 'Серебряный':
            prn = 7
        elif pr == 'Голд':
            prn = 8
        elif pr == 'Платина':
            prn = 9
        elif pr == 'Бриллиант':
            prn = 10
        elif pr == 'Помощник':
            prn = 11
        elif pr == 'Кодер':
            prn = 12
        elif pr == 'Овнер':
            prn = 13
        elif pr == 'Сударь':
            prn = 14
        elif pr == 'Донатер':
            prn = 15
        elif pr == '' or pr == ' ':
            print(forerrorprint)
        else:
            prn = 16
        if work.lower() == 'архитектор':
            work1 = 'architector'
        elif work.lower() == 'блогер':
            work1 = 'bloger'
        elif work.lower() == 'строитель':
            work1 = 'builder'
        elif work.lower() == 'шахтер':
            work1 = 'caver'
        elif work.lower() == 'разработчик':
            work1 = 'developer'
        elif work.lower() == 'киберспортсмен':
            work1 = 'esportsman'
        elif work.lower() == 'фермер':
            work1 = 'farmer'
        elif work.lower() == 'киллер':
            work1 = 'killer'
        elif work.lower() == 'программист':
            work1 = 'programmer'
        elif work.lower() == 'учитель':
            work1 = 'teacher'
        else:
            work1 = 'Нету'
        c.execute(f"SELECT user_eclairs, user_chapchas, user_freebases FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for i in items:
            uec = i[0]
            uch = i[1]
            ufr = i[2]
        if prn == pn:
            await message.answer("У Вас уже установлен такой префикс")
        elif prn > pn:
            if prn == 1:
                if uec >= 10000:
                    price_eclairs = uec - 10000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 2:
                if uec >= 25000:
                    price_eclairs = uec - 25000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 3:
                if uec >= 50000:
                    price_eclairs = uec - 50000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 4:
                if uec >= 100000:
                    price_eclairs = uec - 100000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 5:
                if uec >= 500000:
                    price_eclairs = uec - 500000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 6:
                if uec >= 750000:
                    price_eclairs = uec - 750000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 7:
                if uec >= 1500000:
                    price_eclairs = uec - 1500000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 8:
                if uec >= 1750000:
                    price_eclairs = uec - 1750000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 9:
                if uec >= 2500000:
                    price_eclairs = uec - 2500000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 10:
                if uec >= 5000000:
                    price_eclairs = uec - 5000000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 11:
                if uec >= 10000000:
                    price_eclairs = uec - 10000000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 12:
                if ufr >= 5000:
                    price_eclairs = ufr - 5000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 13:
                if ufr >= 10000:
                    price_eclairs = ufr - 10000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 14:
                if uch >= 1000:
                    price_eclairs = uch - 1000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            elif prn == 15:
                if uch >= 100000:
                    price_eclairs = uch - 100000
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_prefix = '{pr}' WHERE worker_id = {message.from_user.id}")
                    c.execute(f"UPDATE user_data SET user_prefix = '{pr}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    await message.answer("Префикс установлен!")
                else:
                    await message.answer("Недостаточно средств")
            else:
                await message.answer("Префикс не найден")
        else:
            await message.answer("Ваш префикс выше")
    except:
        await message.answer("/buyprefix Префикс")
    db.commit()
    db.close()

#qsmyprefix
@dp.message_handler(commands=['myprefix', 'mypref'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_nick, user_prefix FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            up = el[1]
        await message.answer(f"<b><i>[{up}]</i> <a href='tg://user?id={message.from_user.id}'>{un}</a></b>", parse_mode="HTML")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()