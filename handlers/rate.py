from aiogram import types
from dispatcher import dp
import sqlite3

@dp.message_handler(commands=['btop', 'balance_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_chapchas, user_freebases, user_eclairs, user_coins FROM user_data ORDER BY user_chapchas DESC")
    items = c.fetchall()
    cb = []
    for el in items:
        cb.append(el[0])
        cb.append(el[1])
        cb.append(el[2])
        cb.append(el[3])
        cb.append(el[4])
        cb.append(el[5])
        cb.append(el[5])
    c.execute("SELECT user_id FROM user_data ORDER BY user_chapchas DESC")
    utbitems = c.fetchall()
    utbis = []
    for el in utbitems:
        utbis.append(el[0])
    ut = 1
    for t in utbis:
        if t == message.from_user.id:
            break
        else:
            ut += 1
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_chapchas, user_freebases, user_eclairs, user_coins FROM user_data WHERE user_id = {message.from_user.id}")
    uitems = c.fetchall()
    utop = []
    for el in uitems:
        utop.append(el[1])
        utop.append(el[2])
        utop.append(el[3])
        utop.append(el[4])
        utop.append(el[5])
        utop.append(el[6])
    
    await message.answer(f"""Рейтинг: <b>Баланс</b>

1. <b><i>[{cb[1]}]</i></b> <a href='tg://user?id={cb[0]}'>{cb[2]}</a>  |   {cb[3]} чапчей   |   {cb[4]} фрибасов   |   {cb[5]} эклеров   |   {cb[6]} монет
2. <b><i>[{cb[8]}]</i></b> <a href='tg://user?id={cb[7]}'>{cb[9]}</a>  |   {cb[10]} чапчей   |   {cb[11]} фрибасов   |   {cb[12]} эклеров   |   {cb[13]} монет
3. <b><i>[{cb[15]}]</i></b> <a href='tg://user?id={cb[14]}'>{cb[16]}</a>  |   {cb[17]} чапчей   |   {cb[18]} фрибасов   |   {cb[19]} эклеров   |   {cb[20]} монет
4. <b><i>[{cb[22]}]</i></b> <a href='tg://user?id={cb[21]}'>{cb[23]}</a>  |   {cb[24]} чапчей   |   {cb[25]} фрибасов   |   {cb[26]} эклеров   |   {cb[27]} монет
5. <b><i>[{cb[29]}]</i></b> <a href='tg://user?id={cb[28]}'>{cb[30]}</a>  |   {cb[31]} чапчей   |   {cb[32]} фрибасов   |   {cb[33]} эклеров   |   {cb[34]} монет
6. <b><i>[{cb[36]}]</i></b> <a href='tg://user?id={cb[35]}'>{cb[37]}</a>  |   {cb[38]} чапчей   |   {cb[39]} фрибасов   |   {cb[40]} эклеров   |   {cb[41]} монет
7. <b><i>[{cb[43]}]</i></b> <a href='tg://user?id={cb[42]}'>{cb[44]}</a>  |   {cb[45]} чапчей   |   {cb[46]} фрибасов   |   {cb[47]} эклеров   |   {cb[48]} монет
8. <b><i>[{cb[50]}]</i></b> <a href='tg://user?id={cb[49]}'>{cb[51]}</a>  |   {cb[52]} чапчей   |   {cb[53]} фрибасов   |   {cb[54]} эклеров   |   {cb[55]} монет
9. <b><i>[{cb[57]}]</i></b> <a href='tg://user?id={cb[56]}'>{cb[58]}</a>  |   {cb[59]} чапчей   |   {cb[60]} фрибасов   |   {cb[61]} эклеров   |   {cb[62]} монет
10. <b><i>[{cb[64]}]</i></b> <a href='tg://user?id={cb[63]}'>{cb[65]}</a>  |   {cb[66]} чапчей   |   {cb[67]} фрибасов   |   {cb[68]} эклеров   |   {cb[69]} монет

<b>Вы:</b>
{round(ut)}. <b><i>[{utop[0]}]</i></b> <a href='tg://user?id={message.from_user.id}'>{utop[1]}</a>   |   {utop[4]} чапчей   |   {utop[5]} фрибасов   |   {utop[2]} эклеров   |   {utop[3]} монет
""", parse_mode="HTML")
    c.execute(f"SELECT * FROM user_data")
    db.commit()
    db.close()

@dp.message_handler(commands=['ctop', 'coin_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_coins FROM user_data ORDER BY user_coins DESC")
    items = c.fetchall()
    cb = []
    for el in items:
        cb.append(el[0])
        cb.append(el[1])
        cb.append(el[2])
        cb.append(el[3])
    
    c.execute("SELECT user_id FROM user_data ORDER BY user_coins DESC")
    utbitems = c.fetchall()
    utbis = []
    for el in utbitems:
        utbis.append(el[0])
    ut = 1
    for t in utbis:
        if t == message.from_user.id:
            break
        else:
            ut += 1
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_coins FROM user_data WHERE user_id = {message.from_user.id}")
    uitems = c.fetchall()
    utop = []
    for el in uitems:
        utop.append(el[0])
        utop.append(el[1])
        utop.append(el[2])
        utop.append(el[3])
    
    await message.answer(f"""Рейтинг: <b>Монеты</b>

1. <b><i>[{cb[1]}]</i></b> <a href='tg://user?id={cb[0]}'>{cb[2]}</a>   |   {cb[3]} монет
2. <b><i>[{cb[5]}]</i></b> <a href='tg://user?id={cb[4]}'>{cb[6]}</a>   |   {cb[7]} монет
3. <b><i>[{cb[9]}]</i></b> <a href='tg://user?id={cb[8]}'>{cb[10]}</a>   |   {cb[11]} монет
4. <b><i>[{cb[13]}]</i></b> <a href='tg://user?id={cb[12]}'>{cb[14]}</a>   |   {cb[15]} монет
5. <b><i>[{cb[17]}]</i></b> <a href='tg://user?id={cb[16]}'>{cb[18]}</a>   |   {cb[19]} монет
6. <b><i>[{cb[21]}]</i></b> <a href='tg://user?id={cb[20]}'>{cb[22]}</a>   |   {cb[23]} монет
7. <b><i>[{cb[25]}]</i></b> <a href='tg://user?id={cb[24]}'>{cb[26]}</a>   |   {cb[27]} монет
8. <b><i>[{cb[29]}]</i></b> <a href='tg://user?id={cb[28]}'>{cb[30]}</a>   |   {cb[31]} монет
9. <b><i>[{cb[33]}]</i></b> <a href='tg://user?id={cb[32]}'>{cb[34]}</a>   |   {cb[35]} монет
10. <b><i>[{cb[37]}]</i></b> <a href='tg://user?id={cb[36]}'>{cb[38]}</a>   |   {cb[39]} монет

<b>Вы:</b>
{round(ut)}. <b><i>[{utop[1]}]</i></b> <a href='tg://user?id={utop[0]}'>{utop[2]}</a>   |   {utop[3]} монет""", parse_mode="HTML")
    c.execute(f"SELECT * FROM user_data")
    db.commit()
    db.close()

@dp.message_handler(commands=['ptop', 'point_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_points FROM user_data ORDER BY user_points DESC")
    items = c.fetchall()
    cb = []
    for el in items:
        cb.append(el[0])
        cb.append(el[1])
        cb.append(el[2])
        cb.append(el[3])
    c.execute("SELECT user_id FROM user_data ORDER BY user_points DESC")
    utbitems = c.fetchall()
    utbis = []
    for el in utbitems:
        utbis.append(el[0])
    ut = 1
    for t in utbis:
        if t == message.from_user.id:
            break
        else:
            ut += 1
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_points FROM user_data WHERE user_id = {message.from_user.id}")
    uitems = c.fetchall()
    utop = []
    for el in uitems:
        utop.append(el[0])
        utop.append(el[1])
        utop.append(el[2])
        utop.append(el[3])
    
    await message.answer(f"""Рейтинг: <b>Очки</b>

1. <b><i>[{cb[1]}]</i></b> <a href='tg://user?id={cb[0]}'>{cb[2]}</a>  |   {cb[3]} очков
2. <b><i>[{cb[5]}]</i></b> <a href='tg://user?id={cb[4]}'>{cb[6]}</a>  |   {cb[7]} очков
3. <b><i>[{cb[9]}]</i></b> <a href='tg://user?id={cb[8]}'>{cb[10]}</a>  |   {cb[11]} очков
4. <b><i>[{cb[13]}]</i></b> <a href='tg://user?id={cb[12]}'>{cb[14]}</a>  |   {cb[15]} очков
5. <b><i>[{cb[17]}]</i></b> <a href='tg://user?id={cb[16]}'>{cb[18]}</a>  |   {cb[19]} очков
6. <b><i>[{cb[21]}]</i></b> <a href='tg://user?id={cb[20]}'>{cb[22]}</a>  |   {cb[23]} очков
7. <b><i>[{cb[25]}]</i></b> <a href='tg://user?id={cb[24]}'>{cb[26]}</a>  |   {cb[27]} очков
8. <b><i>[{cb[29]}]</i></b> <a href='tg://user?id={cb[28]}'>{cb[30]}</a>  |   {cb[31]} очков
9. <b><i>[{cb[33]}]</i></b> <a href='tg://user?id={cb[32]}'>{cb[34]}</a>  |   {cb[35]} очков
10. <b><i>[{cb[37]}]</i></b> <a href='tg://user?id={cb[36]}'>{cb[38]}</a>  |   {cb[39]} очков

<b>Вы:</b>
{round(ut)}. <b><i>[{utop[1]}]</i></b> <a href='tg://user?id={utop[0]}'>{utop[2]}</a>   |   {utop[3]} очков""", parse_mode="HTML")
    c.execute(f"SELECT * FROM user_data")
    db.commit()
    db.close()

@dp.message_handler(commands=['chtop', 'chapcha_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_chapchas FROM user_data ORDER BY user_chapchas DESC")
    items = c.fetchall()
    cb = []
    for el in items:
        cb.append(el[0])
        cb.append(el[1])
        cb.append(el[2])
        cb.append(el[3])
    
    c.execute("SELECT user_id FROM user_data ORDER BY user_chapchas DESC")
    utbitems = c.fetchall()
    utbis = []
    for el in utbitems:
        utbis.append(el[0])
    ut = 1
    for t in utbis:
        if t == message.from_user.id:
            break
        else:
            ut += 1
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_chapchas FROM user_data WHERE user_id = {message.from_user.id}")
    uitems = c.fetchall()
    utop = []
    for el in uitems:
        utop.append(el[0])
        utop.append(el[1])
        utop.append(el[2])
        utop.append(el[3])
    
    await message.answer(f"""Рейтинг: <b>Чапчи</b>

1. <b><i>[{cb[1]}]</i></b> <a href='tg://user?id={cb[0]}'>{cb[2]}</a>   |   {cb[3]} чапчей
2. <b><i>[{cb[5]}]</i></b> <a href='tg://user?id={cb[4]}'>{cb[6]}</a>   |   {cb[7]} чапчей
3. <b><i>[{cb[9]}]</i></b> <a href='tg://user?id={cb[8]}'>{cb[10]}</a>   |   {cb[11]} чапчей
4. <b><i>[{cb[13]}]</i></b> <a href='tg://user?id={cb[12]}'>{cb[14]}</a>   |   {cb[15]} чапчей
5. <b><i>[{cb[17]}]</i></b> <a href='tg://user?id={cb[16]}'>{cb[18]}</a>   |   {cb[19]} чапчей
6. <b><i>[{cb[21]}]</i></b> <a href='tg://user?id={cb[20]}'>{cb[22]}</a>   |   {cb[23]} чапчей
7. <b><i>[{cb[25]}]</i></b> <a href='tg://user?id={cb[24]}'>{cb[26]}</a>   |   {cb[27]} чапчей
8. <b><i>[{cb[29]}]</i></b> <a href='tg://user?id={cb[28]}'>{cb[30]}</a>   |   {cb[31]} чапчей
9. <b><i>[{cb[33]}]</i></b> <a href='tg://user?id={cb[32]}'>{cb[34]}</a>   |   {cb[35]} чапчей
10. <b><i>[{cb[37]}]</i></b> <a href='tg://user?id={cb[36]}'>{cb[38]}</a>   |   {cb[39]} чапчей

<b>Вы:</b>
{round(ut)}. <b><i>[{utop[1]}]</i></b> <a href='tg://user?id={utop[0]}'>{utop[2]}</a>   |   {utop[3]} чапчей""", parse_mode="HTML")
    c.execute(f"SELECT * FROM user_data")
    db.commit()
    db.close()

@dp.message_handler(commands=['ectop', 'eclair_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_eclairs FROM user_data ORDER BY user_eclairs DESC")
    items = c.fetchall()
    cb = []
    for el in items:
        cb.append(el[0])
        cb.append(el[1])
        cb.append(el[2])
        cb.append(el[3])
    
    c.execute("SELECT user_id FROM user_data ORDER BY user_eclairs DESC")
    utbitems = c.fetchall()
    utbis = []
    for el in utbitems:
        utbis.append(el[0])
    ut = 1
    for t in utbis:
        if t == message.from_user.id:
            break
        else:
            ut += 1
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_eclairs FROM user_data WHERE user_id = {message.from_user.id}")
    uitems = c.fetchall()
    utop = []
    for el in uitems:
        utop.append(el[0])
        utop.append(el[1])
        utop.append(el[2])
        utop.append(el[3])
    
    await message.answer(f"""Рейтинг: <b>Эклеры</b>

1. <b><i>[{cb[1]}]</i></b> <a href='tg://user?id={cb[0]}'>{cb[2]}</a>   |   {cb[3]} эклеров
2. <b><i>[{cb[5]}]</i></b> <a href='tg://user?id={cb[4]}'>{cb[6]}</a>   |   {cb[7]} эклеров
3. <b><i>[{cb[9]}]</i></b> <a href='tg://user?id={cb[8]}'>{cb[10]}</a>   |   {cb[11]} эклеров
4. <b><i>[{cb[13]}]</i></b> <a href='tg://user?id={cb[12]}'>{cb[14]}</a>   |   {cb[15]} эклеров
5. <b><i>[{cb[17]}]</i></b> <a href='tg://user?id={cb[16]}'>{cb[18]}</a>   |   {cb[19]} эклеров
6. <b><i>[{cb[21]}]</i></b> <a href='tg://user?id={cb[20]}'>{cb[22]}</a>   |   {cb[23]} эклеров
7. <b><i>[{cb[25]}]</i></b> <a href='tg://user?id={cb[24]}'>{cb[26]}</a>   |   {cb[27]} эклеров
8. <b><i>[{cb[29]}]</i></b> <a href='tg://user?id={cb[28]}'>{cb[30]}</a>   |   {cb[31]} эклеров
9. <b><i>[{cb[33]}]</i></b> <a href='tg://user?id={cb[32]}'>{cb[34]}</a>   |   {cb[35]} эклеров
10. <b><i>[{cb[37]}]</i></b> <a href='tg://user?id={cb[36]}'>{cb[38]}</a>   |   {cb[39]} эклеров

<b>Вы:</b>
{round(ut)}. <b><i>[{utop[1]}]</i></b> <a href='tg://user?id={utop[0]}'>{utop[2]}</a>   |   {utop[3]} эклеров""", parse_mode="HTML")
    c.execute(f"SELECT * FROM user_data")
    db.commit()
    db.close()

@dp.message_handler(commands=['ftop', 'freebas_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_freebases FROM user_data ORDER BY user_freebases DESC")
    items = c.fetchall()
    cb = []
    for el in items:
        cb.append(el[0])
        cb.append(el[1])
        cb.append(el[2])
        cb.append(el[3])
    
    c.execute("SELECT user_id FROM user_data ORDER BY user_freebases DESC")
    utbitems = c.fetchall()
    utbis = []
    for el in utbitems:
        utbis.append(el[0])
    ut = 1
    for t in utbis:
        if t == message.from_user.id:
            break
        else:
            ut += 1
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_freebases FROM user_data WHERE user_id = {message.from_user.id}")
    uitems = c.fetchall()
    utop = []
    for el in uitems:
        utop.append(el[0])
        utop.append(el[1])
        utop.append(el[2])
        utop.append(el[3])
    
    await message.answer(f"""Рейтинг: <b>Фрибасы</b>

1. <b><i>[{cb[1]}]</i></b> <a href='tg://user?id={cb[0]}'>{cb[2]}</a>   |   {cb[3]} фрибасов
2. <b><i>[{cb[5]}]</i></b> <a href='tg://user?id={cb[4]}'>{cb[6]}</a>   |   {cb[7]} фрибасов
3. <b><i>[{cb[9]}]</i></b> <a href='tg://user?id={cb[8]}'>{cb[10]}</a>   |   {cb[11]} фрибасов
4. <b><i>[{cb[13]}]</i></b> <a href='tg://user?id={cb[12]}'>{cb[14]}</a>   |   {cb[15]} фрибасов
5. <b><i>[{cb[17]}]</i></b> <a href='tg://user?id={cb[16]}'>{cb[18]}</a>   |   {cb[19]} фрибасов
6. <b><i>[{cb[21]}]</i></b> <a href='tg://user?id={cb[20]}'>{cb[22]}</a>   |   {cb[23]} фрибасов
7. <b><i>[{cb[25]}]</i></b> <a href='tg://user?id={cb[24]}'>{cb[26]}</a>   |   {cb[27]} фрибасов
8. <b><i>[{cb[29]}]</i></b> <a href='tg://user?id={cb[28]}'>{cb[30]}</a>   |   {cb[31]} фрибасов
9. <b><i>[{cb[33]}]</i></b> <a href='tg://user?id={cb[32]}'>{cb[34]}</a>   |   {cb[35]} фрибасов
10. <b><i>[{cb[37]}]</i></b> <a href='tg://user?id={cb[36]}'>{cb[38]}</a>   |   {cb[39]} фрибасов

<b>Вы:</b>
{round(ut)}. <b><i>[{utop[1]}]</i></b> <a href='tg://user?id={utop[0]}'>{utop[2]}</a>   |   {utop[3]} фрибасов""", parse_mode="HTML")
    c.execute(f"SELECT * FROM user_data")
    db.commit()
    db.close()

@dp.message_handler(commands=['rtop', 'reputation_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_reputation FROM user_data ORDER BY user_reputation DESC")
    items = c.fetchall()
    cb = []
    for el in items:
        cb.append(el[0])
        cb.append(el[1])
        cb.append(el[2])
        cb.append(el[3])
    
    c.execute("SELECT user_id FROM user_data ORDER BY user_reputation DESC")
    utbitems = c.fetchall()
    utbis = []
    for el in utbitems:
        utbis.append(el[0])
    ut = 1
    for t in utbis:
        if t == message.from_user.id:
            break
        else:
            ut += 1
    c.execute(f"SELECT user_id, user_prefix, user_nick, user_reputation FROM user_data WHERE user_id = {message.from_user.id}")
    uitems = c.fetchall()
    utop = []
    for el in uitems:
        utop.append(el[0])
        utop.append(el[1])
        utop.append(el[2])
        utop.append(el[3])
    
    await message.answer(f"""Рейтинг: <b>Репутация</b>

1. <b><i>[{cb[1]}]</i></b> <a href='tg://user?id={cb[0]}'>{cb[2]}</a>   |   {cb[3]} очков репутации
2. <b><i>[{cb[5]}]</i></b> <a href='tg://user?id={cb[4]}'>{cb[6]}</a>   |   {cb[7]} очков репутации
3. <b><i>[{cb[9]}]</i></b> <a href='tg://user?id={cb[8]}'>{cb[10]}</a>   |   {cb[11]} очков репутации
4. <b><i>[{cb[13]}]</i></b> <a href='tg://user?id={cb[12]}'>{cb[14]}</a>   |   {cb[15]} очков репутации
5. <b><i>[{cb[17]}]</i></b> <a href='tg://user?id={cb[16]}'>{cb[18]}</a>   |   {cb[19]} очков репутации
6. <b><i>[{cb[21]}]</i></b> <a href='tg://user?id={cb[20]}'>{cb[22]}</a>   |   {cb[23]} очков репутации
7. <b><i>[{cb[25]}]</i></b> <a href='tg://user?id={cb[24]}'>{cb[26]}</a>   |   {cb[27]} очков репутации
8. <b><i>[{cb[29]}]</i></b> <a href='tg://user?id={cb[28]}'>{cb[30]}</a>   |   {cb[31]} очков репутации
9. <b><i>[{cb[33]}]</i></b> <a href='tg://user?id={cb[32]}'>{cb[34]}</a>   |   {cb[35]} очков репутации
10. <b><i>[{cb[37]}]</i></b> <a href='tg://user?id={cb[36]}'>{cb[38]}</a>   |   {cb[39]} очков репутации

<b>Вы:</b>
{round(ut)}. <b><i>[{utop[1]}]</i></b> <a href='tg://user?id={utop[0]}'>{utop[2]}</a>   |   {utop[3]} очков репутации""", parse_mode="HTML")
    c.execute(f"SELECT * FROM user_data")
    db.commit()
    db.close()

@dp.message_handler(commands=['top', 'rate'])
async def process_giveeclairs_command(message: types.Message):
    await message.answer(f"""<b>Рейтинги:</b>

/balance_top - рейтинг по балансу
/point_top - рейтинг по очкам
/chapcha_top - рейтинг по чапчам
/freebas_top - рейтинг по фрибасам
/eclair_top - рейтинг по эклерам
/coin_top - рейтинг по монетам
/reputation_top - рейтинг по репутации""", parse_mode="HTML")