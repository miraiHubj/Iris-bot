from aiogram import types
from dispatcher import dp, bot
from random import randint
import sqlite3

@dp.message_handler(commands=['jobs', 'j', 'работы', 'ворки'], commands_prefix="/!.")
async def games(message: types.Message):
    await message.answer("""<b>Профессии:</b>

<code>Архитектор</code>
<code>Блогер</code>
<code>Строитель</code>
<code>Шахтер</code>
<code>Разработчик</code>
<code>Киберспортсмен</code>
<code>Фермер</code>
<code>Киллер</code>
<code>Программист</code>
<code>Учитель</code>

<code>+работа</code> Профессия - устроиться на работу""", parse_mode="HTML")

@dp.message_handler(commands=['работа', 'профессия', 'ворк'], commands_prefix='+')
async def games(message: types.Message):
    if message.text.lower().find('работа') != -1:
        work = message.text[8:]
    elif message.text.lower().find('профессия') != -1:
        work = message.text[11:]
    else:
        work = message.text[6:]
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
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
    if work1 == 'Нету':
        await message.answer("Такой профессии нету")
    else:
        try:
            c.execute(f"SELECT user_prefix, user_nick, user_job FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                up = el[0]
                un = el[1]
                uj = el[2]
            if uj == 'Безработный':
                c.execute(f"INSERT INTO job_{work1} VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                          (message.from_user.id, up, un, 1, 1000, 0, 365, 10000))
                c.execute(f"UPDATE user_data SET user_job = '{work.capitalize()}' WHERE user_id = {message.from_user.id}")
                await message.answer("Вы устроились на работу!")
            else:
                await message.answer("Вы уже устроены на работу!")
        except:
            await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.message_handler(text=['-работа', '-профессия', '-ворк'])
async def games(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_job FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            work = el[0]
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
        if work1 == 'Нету':
            await message.answer("Вы безработный(ая)")
        else:
            c.execute(f"DELETE FROM job_{work1} WHERE worker_id = {message.from_user.id}")
            c.execute(f"UPDATE user_data SET user_job = 'Безработный' WHERE user_id = {message.from_user.id}")
            await message.answer("Вы уволились с работы!")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.message_handler(commands=['работа', 'профессия', 'ворк'], commands_prefix='/!.')
async def games(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_job FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            work = el[0]
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
        if work1 == 'Нету':
            await message.answer("Вы безработный(ая)")
        else:
            c.execute(f"SELECT * FROM job_{work1} WHERE worker_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                wi = el[0]
                wp = el[1]
                wn = el[2]
                wl = el[3]
                ws = el[4]
                ww = el[5]
                ns = el[6]
                nu = el[7]
            if wl != 5:
                await message.answer(f"""Профессия <b><i>[{wp}]</i> <a href='tg://user?id={message.from_user.id}'>{wn}</a></b>: <b>{work}</b>
Ранг: <b>{wl}</b>
Зарплата: <b>{ws} монет</b>
Отработано: <b>{ww} дней</b>
До зарплаты: <b>{ns} дней работы</b>
До повышения: <b>{nu} дней работы</b>""", parse_mode="HTML")
            else:
                await message.answer(f"""Профессия <b><i>[{wp}]</i> <a href='tg://user?id={message.from_user.id}'>{wn}</a></b>: <b>{work}</b>
Ранг: <b>{wl}</b>
Зарплата: <b>{ws} монет</b>
Отработано: <b>{ww} дней</b>
До зарплаты: <b>{ns} дней работы</b>""", parse_mode="HTML")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.message_handler(commands=['работать', 'воркинг', 'праця'], commands_prefix='/!.')
async def games(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_job FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            work = el[0]
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
        if work1 == 'Нету':
            await message.answer("Вы безработный(ая)")
        else:
            c.execute(f"SELECT * FROM job_{work1} WHERE worker_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                wi = el[0]
                wp = el[1]
                wn = el[2]
                wl = el[3]
                ws = el[4]
                ww = el[5]
                ns = el[6]
                nu = el[7]
            c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {wi}")
            items = c.fetchall()
            for el in items:
                uc = el[0]
            price_ns = ns - 1
            if wl == 5:
                price_nu = 999999
            else:
                price_nu = nu - 1
            if price_ns == 0:
                c.execute(f"UPDATE user_data SET user_coins = {uc+ws} WHERE user_id = {wi}")
                c.execute(f"UPDATE job_{work1} SET working = {ww+1}, to_salary_left = 365, to_up_left = {price_nu} WHERE worker_id = {wi}")
                if price_nu == 0 and wl != 5:
                    c.execute(f"UPDATE job_{work1} SET work_lvl = {wl+1}, salary = {ws+1000}, to_up_left = {10000*(2**(wl))} WHERE worker_id = {wi}")
                    if wl + 1 == 5:
                        c.execute(f"UPDATE job_{work1} SET work_lvl = {wl+1}, salary = {ws+1000}, to_up_left = 999999 WHERE worker_id = {wi}")
                        await message.answer(f"<b><i>[{wp}]</i> <a href='tg://user?id={message.from_user.id}'>{wn}</a></b> Вы отработали 8 часов!\nВы получили зарплату: <b>{ws} монет</b>!\n<b>Вас повысили до максимального ранга!</b>", parse_mode="HTML")
                    else:
                        await message.answer(f"<b><i>[{wp}]</i> <a href='tg://user?id={message.from_user.id}'>{wn}</a></b> Вы отработали 8 часов!\nВы получили зарплату: <b>{ws} монет</b>!\n<b>Вас повысили!</b>", parse_mode="HTML")
                else:
                    await message.answer(f"<b><i>[{wp}]</i> <a href='tg://user?id={message.from_user.id}'>{wn}</a></b> Вы отработали 8 часов!\nВы получили зарплату: <b>{ws} монет</b>!")
            else:
                if wl == 5:
                    c.execute(f"UPDATE job_{work1} SET working = {ww+1}, to_salary_left = {price_ns}, to_up_left = 999999 WHERE worker_id = {wi}")
                    await message.answer(f"<b><i>[{wp}]</i> <a href='tg://user?id={message.from_user.id}'>{wn}</a></b> Вы отработали 8 часов!\nДо зарплаты осталось <b>{price_ns} дней работы</b>", parse_mode="HTML")
                else:
                    c.execute(f"UPDATE job_{work1} SET working = {ww+1}, to_salary_left = {price_ns}, to_up_left = {price_nu} WHERE worker_id = {wi}")
                    await message.answer(f"<b><i>[{wp}]</i> <a href='tg://user?id={message.from_user.id}'>{wn}</a></b> Вы отработали 8 часов!\nДо зарплаты осталось <b>{price_ns} дней работы</b>\nДо повышения осталось <b>{price_nu} дней работы</b>", parse_mode="HTML")
            c.execute(f"SELECT up_kv, key_regular, key_rare, key_epic, key_legendary, key_mifik FROM game_case WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                kv = el[0]
                rk = el[1]
                rak = el[2]
                ek = el[3]
                lk = el[4]
                mk = el[5]
            fk1 = randint(0,100)
            fk2 = randint(0, 999)
            fk = float(str(fk1)+'.'+str(fk2))
            if fk < mk-49:
                mk += 1
                await message.answer("🔑 Вы нашли ключ от мифического кейса!")
            elif fk < mk-36:
                lk += 1
                await message.answer("🔑 Вы нашли ключ от легендарного кейса!")
            elif fk < mk-24:
                ek += 1
                await message.answer("🔑 Вы нашли ключ от эпического кейса!")
            elif fk < mk-12:
                rak += 1
                await message.answer("🔑 Вы нашли ключ от редкого кейса!")
            elif fk < mk:
                rk += 1
                await message.answer("🔑 Вы нашли ключ от обычного кейса!")
            c.execute(f"UPDATE game_case SET key_regular = {rk}, key_rare = {rak}, key_epic = {ek}, key_legendary = {lk}, key_mifik = {mk} WHERE user_id = {message.from_user.id}")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()