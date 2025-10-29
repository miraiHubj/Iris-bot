from aiogram import types
from dispatcher import dp, bot
import sqlite3

@dp.message_handler(commands=['clanchtop', 'clan_chapcha_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT * from clan_data")
    items = c.fetchall()
    clanl = []
    for el in items:
        for e in el:
            clanl.append(e)
    clan = []
    for el in clanl:
        if el == '' or el == None or el == 'None':
            pass
        else:
            clan.append(el)
    li = 0
    mbn = 0
    for el in clan:
        if el == message.from_user.id:
            for i in range(1, 500):
                c.execute(f"SELECT leader_id FROM clan_data WHERE mb{i} = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    li = 0
                    if el[0] == None or el[0] == '':
                        pass
                    else:
                        li = el[0]
                        mbn = i
                        break
                if li != 0:
                    break
    c.execute(f"SELECT leader_id FROM clan_data WHERE leader_id = {message.from_user.id}")
    items = c.fetchall()
    for el in items:
        if el[0] == None or el[0] == '':
            pass
        else:
            li = el[0]
    else:
        if mbn != 0:
            c.execute(f"SELECT clan_name, clan_prefix, clan_chapchas FROM clan_data WHERE mb{mbn} = {message.from_user.id}")
        else:
            c.execute(f"SELECT clan_name, clan_prefix, clan_chapchas FROM clan_data WHERE leader_id = {message.from_user.id}")
    citems = c.fetchall()
    ctop = []
    for el in citems:
        ctop.append(el[1])
        ctop.append(el[0])
        ctop.append(el[2])
    c.execute("SELECT leader_id FROM clan_data ORDER BY clan_chapchas DESC")
    ctbitems = c.fetchall()
    ctbis = []
    for el in ctbitems:
        ctbis.append(el[0])
    ct = 1
    for t in ctbis:
        if t == message.from_user.id:
            break
        else:
            ct += 1
    c.execute(f"SELECT clan_name, clan_prefix, clan_chapchas FROM clan_data ORDER BY clan_chapchas DESC")
    items = c.fetchall()
    cb = []
    for el in items:
        cb.append(el[1])
        cb.append(el[0])
        cb.append(el[2])
    
    if len(ctop) < 3:
        if len(cb) < 3:
            await message.answer("""Рейтинг кланов: <b>Чапчи</b>

Список пуст""", parse_mode="HTML")
        elif len(cb) == 3:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей""", parse_mode="HTML")
        elif len(cb) == 6:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей""", parse_mode="HTML")
        elif len(cb) == 9:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей""", parse_mode="HTML")
        elif len(cb) == 12:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей""", parse_mode="HTML")
        elif len(cb) == 15:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} чапчей""", parse_mode="HTML")
        elif len(cb) == 18:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} чапчей
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} чапчей""", parse_mode="HTML")
        elif len(cb) == 21:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} чапчей
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} чапчей
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} чапчей""", parse_mode="HTML")
        elif len(cb) == 24:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} чапчей
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} чапчей
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} чапчей
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} чапчей""", parse_mode="HTML")
        elif len(cb) == 27:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} чапчей
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} чапчей
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} чапчей
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} чапчей
9. <b><i>[{cb[24]}]</i></b> {cb[25]}   |   {cb[26]} чапчей""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} чапчей
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} чапчей
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} чапчей
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} чапчей
9. <b><i>[{cb[24]}]</i></b> {cb[25]}   |   {cb[26]} чапчей
10. <b><i>[{cb[27]}]</i></b> {cb[28]}   |   {cb[29]} чапчей""", parse_mode="HTML")
    else:
        if len(cb) < 3:
            await message.answer("""Рейтинг кланов: <b>Чапчи</b>

Список пуст""", parse_mode="HTML")
        elif len(cb) == 3:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} чапчей""", parse_mode="HTML")
        elif len(cb) == 6:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} чапчей""", parse_mode="HTML")
        elif len(cb) == 9:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} чапчей""", parse_mode="HTML")
        elif len(cb) == 12:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} чапчей""", parse_mode="HTML")
        elif len(cb) == 15:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} чапчей


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} чапчей""", parse_mode="HTML")
        elif len(cb) == 18:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} чапчей
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} чапчей


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} чапчей""", parse_mode="HTML")
        elif len(cb) == 21:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} чапчей
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} чапчей
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} чапчей


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} чапчей""", parse_mode="HTML")
        elif len(cb) == 24:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} чапчей
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} чапчей
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} чапчей
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} чапчей


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} чапчей""", parse_mode="HTML")
        elif len(cb) == 27:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} чапчей
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} чапчей
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} чапчей
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} чапчей
9. <b><i>[{cb[24]}]</i></b> {cb[25]}   |   {cb[26]} чапчей


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} чапчей""", parse_mode="HTML")
        elif len(cb) == 30:
            await message.answer(f"""Рейтинг кланов: <b>Чапчи</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} чапчей
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} чапчей
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} чапчей
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} чапчей
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} чапчей
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} чапчей
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} чапчей
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} чапчей
9. <b><i>[{cb[24]}]</i></b> {cb[25]}   |   {cb[26]} чапчей
10. <b><i>[{cb[27]}]</i></b> {cb[28]}   |   {cb[29]} чапчей


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} чапчей""", parse_mode="HTML")
    db.commit()
    db.close()





@dp.message_handler(commands=['clanftop', 'clan_freebas_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT * from clan_data")
    items = c.fetchall()
    clanl = []
    for el in items:
        for e in el:
            clanl.append(e)
    clan = []
    for el in clanl:
        if el == '' or el == None or el == 'None':
            pass
        else:
            clan.append(el)
    li = 0
    mbn = 0
    for el in clan:
        if el == message.from_user.id:
            for i in range(1, 500):
                c.execute(f"SELECT leader_id FROM clan_data WHERE mb{i} = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    li = 0
                    if el[0] == None or el[0] == '':
                        pass
                    else:
                        li = el[0]
                        mbn = i
                        break
                if li != 0:
                    break
    c.execute(f"SELECT leader_id FROM clan_data WHERE leader_id = {message.from_user.id}")
    items = c.fetchall()
    for el in items:
        if el[0] == None or el[0] == '':
            pass
        else:
            li = el[0]
    else:
        if mbn != 0:
            c.execute(f"SELECT clan_name, clan_prefix, clan_freebases FROM clan_data WHERE mb{mbn} = {message.from_user.id}")
        else:
            c.execute(f"SELECT clan_name, clan_prefix, clan_freebases FROM clan_data WHERE leader_id = {message.from_user.id}")
    citems = c.fetchall()
    ctop = []
    for el in citems:
        ctop.append(el[1])
        ctop.append(el[0])
        ctop.append(el[2])
    c.execute("SELECT leader_id FROM clan_data ORDER BY clan_freebases DESC")
    ctbitems = c.fetchall()
    ctbis = []
    for el in ctbitems:
        ctbis.append(el[0])
    ct = 1
    for t in ctbis:
        if t == message.from_user.id:
            break
        else:
            ct += 1
    c.execute(f"SELECT clan_name, clan_prefix, clan_freebases FROM clan_data ORDER BY clan_freebases DESC")
    items = c.fetchall()
    cb = []
    for el in items:
        cb.append(el[1])
        cb.append(el[0])
        cb.append(el[2])
    
    if len(ctop) < 3:
        if len(cb) < 3:
            await message.answer("""Рейтинг кланов: <b>Фрибасы</b>

Список пуст""", parse_mode="HTML")
        elif len(cb) == 3:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 6:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 9:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 12:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 15:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 18:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} фрибасов
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 21:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} фрибасов
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} фрибасов
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 24:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} фрибасов
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} фрибасов
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} фрибасов
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 27:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} фрибасов
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} фрибасов
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} фрибасов
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} фрибасов
9. <b><i>[{cb[24]}]</i></b> {cb[25]}   |   {cb[26]} фрибасов""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} фрибасов
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} фрибасов
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} фрибасов
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} фрибасов
9. <b><i>[{cb[24]}]</i></b> {cb[25]}   |   {cb[26]} фрибасов
10. <b><i>[{cb[27]}]</i></b> {cb[28]}   |   {cb[29]} фрибасов""", parse_mode="HTML")
    else:
        if len(cb) < 3:
            await message.answer("""Рейтинг кланов: <b>Фрибасы</b>

Список пуст""", parse_mode="HTML")
        elif len(cb) == 3:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 6:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 9:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 12:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 15:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} фрибасов


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 18:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} фрибасов
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} фрибасов


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 21:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} фрибасов
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} фрибасов
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} фрибасов


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 24:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} фрибасов
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} фрибасов
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} фрибасов
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} фрибасов


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 27:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} фрибасов
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} фрибасов
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} фрибасов
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} фрибасов
9. <b><i>[{cb[24]}]</i></b> {cb[25]}   |   {cb[26]} фрибасов


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} фрибасов""", parse_mode="HTML")
        elif len(cb) == 30:
            await message.answer(f"""Рейтинг кланов: <b>Фрибасы</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} фрибасов
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} фрибасов
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} фрибасов
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} фрибасов
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} фрибасов
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} фрибасов
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} фрибасов
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} фрибасов
9. <b><i>[{cb[24]}]</i></b> {cb[25]}   |   {cb[26]} фрибасов
10. <b><i>[{cb[27]}]</i></b> {cb[28]}   |   {cb[29]} фрибасов


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} фрибасов""", parse_mode="HTML")
    db.commit()
    db.close()





@dp.message_handler(commands=['clanrtop', 'clan_reputation_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT * from clan_data")
    items = c.fetchall()
    clanl = []
    for el in items:
        for e in el:
            clanl.append(e)
    clan = []
    for el in clanl:
        if el == '' or el == None or el == 'None':
            pass
        else:
            clan.append(el)
    li = 0
    mbn = 0
    for el in clan:
        if el == message.from_user.id:
            for i in range(1, 500):
                c.execute(f"SELECT leader_id FROM clan_data WHERE mb{i} = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    li = 0
                    if el[0] == None or el[0] == '':
                        pass
                    else:
                        li = el[0]
                        mbn = i
                        break
                if li != 0:
                    break
    c.execute(f"SELECT leader_id FROM clan_data WHERE leader_id = {message.from_user.id}")
    items = c.fetchall()
    for el in items:
        if el[0] == None or el[0] == '':
            pass
        else:
            li = el[0]
    else:
        if mbn != 0:
            c.execute(f"SELECT clan_name, clan_prefix, clan_reputation FROM clan_data WHERE mb{mbn} = {message.from_user.id}")
        else:
            c.execute(f"SELECT clan_name, clan_prefix, clan_reputation FROM clan_data WHERE leader_id = {message.from_user.id}")
    citems = c.fetchall()
    ctop = []
    for el in citems:
        ctop.append(el[1])
        ctop.append(el[0])
        ctop.append(el[2])
    c.execute("SELECT leader_id FROM clan_data ORDER BY clan_reputation DESC")
    ctbitems = c.fetchall()
    ctbis = []
    for el in ctbitems:
        ctbis.append(el[0])
    ct = 1
    for t in ctbis:
        if t == message.from_user.id:
            break
        else:
            ct += 1
    c.execute(f"SELECT clan_name, clan_prefix, clan_reputation FROM clan_data ORDER BY clan_reputation DESC")
    items = c.fetchall()
    cb = []
    for el in items:
        cb.append(el[1])
        cb.append(el[0])
        cb.append(el[2])
    
    if len(ctop) < 3:
        if len(cb) < 3:
            await message.answer("""Рейтинг кланов: <b>Репутация</b>

Список пуст""", parse_mode="HTML")
        elif len(cb) == 3:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 6:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 9:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 12:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 15:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 18:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} очков репутации
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 21:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} очков репутации
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} очков репутации
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 24:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} очков репутации
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} очков репутации
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} очков репутации
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 27:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} очков репутации
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} очков репутации
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} очков репутации
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} очков репутации
9. <b><i>[{cb[24]}]</i></b> {cb[25]}   |   {cb[26]} очков репутации""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} очков репутации
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} очков репутации
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} очков репутации
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} очков репутации
9. <b><i>[{cb[24]}]</i></b> {cb[25]}   |   {cb[26]} очков репутации
10. <b><i>[{cb[27]}]</i></b> {cb[28]}   |   {cb[29]} очков репутации""", parse_mode="HTML")
    else:
        if len(cb) < 3:
            await message.answer("""Рейтинг кланов: <b>Репутация</b>

Список пуст""", parse_mode="HTML")
        elif len(cb) == 3:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 6:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 9:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 12:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 15:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} очков репутации


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 18:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} очков репутации
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} очков репутации


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 21:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} очков репутации
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} очков репутации
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} очков репутации


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 24:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} очков репутации
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} очков репутации
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} очков репутации
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} очков репутации


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 27:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} очков репутации
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} очков репутации
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} очков репутации
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} очков репутации
9. <b><i>[{cb[24]}]</i></b> {cb[25]}   |   {cb[26]} очков репутации


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} очков репутации""", parse_mode="HTML")
        elif len(cb) == 30:
            await message.answer(f"""Рейтинг кланов: <b>Репутация</b>

1. <b><i>[{cb[0]}]</i></b> {cb[1]}   |   {cb[2]} очков репутации
2. <b><i>[{cb[3]}]</i></b> {cb[4]}   |   {cb[5]} очков репутации
3. <b><i>[{cb[6]}]</i></b> {cb[7]}   |   {cb[8]} очков репутации
4. <b><i>[{cb[9]}]</i></b> {cb[10]}   |   {cb[11]} очков репутации
5. <b><i>[{cb[12]}]</i></b> {cb[13]}   |   {cb[14]} очков репутации
6. <b><i>[{cb[15]}]</i></b> {cb[16]}   |   {cb[17]} очков репутации
7. <b><i>[{cb[18]}]</i></b> {cb[19]}   |   {cb[20]} очков репутации
8. <b><i>[{cb[21]}]</i></b> {cb[22]}   |   {cb[23]} очков репутации
9. <b><i>[{cb[24]}]</i></b> {cb[25]}   |   {cb[26]} очков репутации
10. <b><i>[{cb[27]}]</i></b> {cb[28]}   |   {cb[29]} очков репутации


<b>Ваш клан:</b>
{round(ct)}. <b><i>[{ctop[0]}]</i></b> {ctop[1]}   |   {ctop[2]} очков репутации""", parse_mode="HTML")
    db.commit()
    db.close()

@dp.message_handler(commands=['clan_top', 'clan_rate'])
async def process_giveeclairs_command(message: types.Message):
    await message.answer(f"""<b>Рейтинги кланов:</b>

/clan_chapcha_top - рейтинг кланов по чапчам
/clan_freebas_top - рейтинг кланов по фрибасам
/clan_reputation_top - рейтинг кланов по репутации""", parse_mode="HTML")