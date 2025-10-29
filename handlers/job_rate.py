from aiogram import types
from dispatcher import dp, bot
import sqlite3

@dp.message_handler(commands=['jobtop', 'worktop', 'workertop'])
async def process_giveeclairs_command(message: types.Message):
    await message.answer("""<b>Рейтинги работ:</b>

/architect_top - рейтинг по архитекторам
/bloger_top - рейтинг по блогерам
/builder_top - рейтинг по строителям
/miner_top - рейтинг по шахтерам
/developer_top - рейтинг по разработчикам
/cybersportsman_top - рейтинг по киберспортсменам
/farmer_top - рейтинг по фермерам
/killer_top - рейтинг по киллерам
/programmer_top - рейтинг по программистам
/teacher_top - рейтинг по учителям""")

@dp.message_handler(commands=['artop', 'architect_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT worker_id FROM job_architector ORDER BY working DESC")
    items = c.fetchall()
    wil = []
    for el in items:
        num = 0
        for e in el:
            wil.append(e)
    ct = 1
    for t in wil:
        if t == message.from_user.id:
            break
        else:
            ct += 1
    c.execute(f"SELECT worker_prefix, worker_nick, working FROM job_architector WHERE worker_id = {message.from_user.id}")
    items = c.fetchall()
    ud = []
    try:
        for el in items:
            ud.append(el[0])
            ud.append(el[1])
            ud.append(el[2])
    except:
        pass
    c.execute(f"SELECT worker_id, worker_prefix, worker_nick, working FROM job_architector ORDER BY working DESC")
    items = c.fetchall()
    wd = []
    for el in items:
        for e in el:
            wd.append(e)
    if len(ud) < 3:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Архитекторы</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработано""", parse_mode="HTML")
    else:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Архитекторы</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработаноcs""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Архитекторы</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработаноcs


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
    db.commit()
    db.close()



@dp.message_handler(commands=['bltop', 'bloger_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT worker_id FROM job_bloger ORDER BY working DESC")
    items = c.fetchall()
    wil = []
    for el in items:
        num = 0
        for e in el:
            wil.append(e)
    ct = 1
    for t in wil:
        if t == message.from_user.id:
            break
        else:
            ct += 1
    c.execute(f"SELECT worker_prefix, worker_nick, working FROM job_bloger WHERE worker_id = {message.from_user.id}")
    items = c.fetchall()
    ud = []
    try:
        for el in items:
            ud.append(el[0])
            ud.append(el[1])
            ud.append(el[2])
    except:
        pass
    c.execute(f"SELECT worker_id, worker_prefix, worker_nick, working FROM job_bloger ORDER BY working DESC")
    items = c.fetchall()
    wd = []
    for el in items:
        for e in el:
            wd.append(e)
    if len(ud) < 3:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Блогеры</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработано""", parse_mode="HTML")
    else:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Блогеры</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработаноcs""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Блогеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработаноcs


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
    db.commit()
    db.close()



@dp.message_handler(commands=['mitop', 'miner_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT worker_id FROM job_miner ORDER BY working DESC")
    items = c.fetchall()
    wil = []
    for el in items:
        num = 0
        for e in el:
            wil.append(e)
    ct = 1
    for t in wil:
        if t == message.from_user.id:
            break
        else:
            ct += 1
    c.execute(f"SELECT worker_prefix, worker_nick, working FROM job_miner WHERE worker_id = {message.from_user.id}")
    items = c.fetchall()
    ud = []
    try:
        for el in items:
            ud.append(el[0])
            ud.append(el[1])
            ud.append(el[2])
    except:
        pass
    c.execute(f"SELECT worker_id, worker_prefix, worker_nick, working FROM job_miner ORDER BY working DESC")
    items = c.fetchall()
    wd = []
    for el in items:
        for e in el:
            wd.append(e)
    if len(ud) < 3:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Шахтеры</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработано""", parse_mode="HTML")
    else:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Шахтеры</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработаноcs""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Шахтеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработаноcs


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
    db.commit()
    db.close()



@dp.message_handler(commands=['devtop', 'developer_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT worker_id FROM job_developer ORDER BY working DESC")
    items = c.fetchall()
    wil = []
    for el in items:
        num = 0
        for e in el:
            wil.append(e)
    ct = 1
    for t in wil:
        if t == message.from_user.id:
            break
        else:
            ct += 1
    c.execute(f"SELECT worker_prefix, worker_nick, working FROM job_developer WHERE worker_id = {message.from_user.id}")
    items = c.fetchall()
    ud = []
    try:
        for el in items:
            ud.append(el[0])
            ud.append(el[1])
            ud.append(el[2])
    except:
        pass
    c.execute(f"SELECT worker_id, worker_prefix, worker_nick, working FROM job_developer ORDER BY working DESC")
    items = c.fetchall()
    wd = []
    for el in items:
        for e in el:
            wd.append(e)
    if len(ud) < 3:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Разработчики</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработано""", parse_mode="HTML")
    else:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Разработчики</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработаноcs""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Разработчики</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработаноcs


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
    db.commit()
    db.close()



@dp.message_handler(commands=['csportop', 'cybersportsman_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT worker_id FROM job_esportsman ORDER BY working DESC")
    items = c.fetchall()
    wil = []
    for el in items:
        num = 0
        for e in el:
            wil.append(e)
    ct = 1
    for t in wil:
        if t == message.from_user.id:
            break
        else:
            ct += 1
    c.execute(f"SELECT worker_prefix, worker_nick, working FROM job_esportsman WHERE worker_id = {message.from_user.id}")
    items = c.fetchall()
    ud = []
    try:
        for el in items:
            ud.append(el[0])
            ud.append(el[1])
            ud.append(el[2])
    except:
        pass
    c.execute(f"SELECT worker_id, worker_prefix, worker_nick, working FROM job_esportsman ORDER BY working DESC")
    items = c.fetchall()
    wd = []
    for el in items:
        for e in el:
            wd.append(e)
    if len(ud) < 3:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Киберспортсмены</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработано""", parse_mode="HTML")
    else:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Киберспортсмены</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработаноcs""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Киберспортсмены</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработаноcs


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
    db.commit()
    db.close()



@dp.message_handler(commands=['fatop', 'farmer_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT worker_id FROM job_farmer ORDER BY working DESC")
    items = c.fetchall()
    wil = []
    for el in items:
        num = 0
        for e in el:
            wil.append(e)
    ct = 1
    for t in wil:
        if t == message.from_user.id:
            break
        else:
            ct += 1
    c.execute(f"SELECT worker_prefix, worker_nick, working FROM job_farmer WHERE worker_id = {message.from_user.id}")
    items = c.fetchall()
    ud = []
    try:
        for el in items:
            ud.append(el[0])
            ud.append(el[1])
            ud.append(el[2])
    except:
        pass
    c.execute(f"SELECT worker_id, worker_prefix, worker_nick, working FROM job_farmer ORDER BY working DESC")
    items = c.fetchall()
    wd = []
    for el in items:
        for e in el:
            wd.append(e)
    if len(ud) < 3:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Фермеры</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработано""", parse_mode="HTML")
    else:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Фермеры</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработаноcs""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Фермеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработаноcs


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
    db.commit()
    db.close()



@dp.message_handler(commands=['kitop', 'killer_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT worker_id FROM job_killer ORDER BY working DESC")
    items = c.fetchall()
    wil = []
    for el in items:
        num = 0
        for e in el:
            wil.append(e)
    ct = 1
    for t in wil:
        if t == message.from_user.id:
            break
        else:
            ct += 1
    c.execute(f"SELECT worker_prefix, worker_nick, working FROM job_killer WHERE worker_id = {message.from_user.id}")
    items = c.fetchall()
    ud = []
    try:
        for el in items:
            ud.append(el[0])
            ud.append(el[1])
            ud.append(el[2])
    except:
        pass
    c.execute(f"SELECT worker_id, worker_prefix, worker_nick, working FROM job_killer ORDER BY working DESC")
    items = c.fetchall()
    wd = []
    for el in items:
        for e in el:
            wd.append(e)
    if len(ud) < 3:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Киллеры</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработано""", parse_mode="HTML")
    else:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Киллеры</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработаноcs""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Киллеры</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработаноcs


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
    db.commit()
    db.close()



@dp.message_handler(commands=['progtop', 'programmer_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT worker_id FROM job_programmer ORDER BY working DESC")
    items = c.fetchall()
    wil = []
    for el in items:
        num = 0
        for e in el:
            wil.append(e)
    ct = 1
    for t in wil:
        if t == message.from_user.id:
            break
        else:
            ct += 1
    c.execute(f"SELECT worker_prefix, worker_nick, working FROM job_programmer WHERE worker_id = {message.from_user.id}")
    items = c.fetchall()
    ud = []
    try:
        for el in items:
            ud.append(el[0])
            ud.append(el[1])
            ud.append(el[2])
    except:
        pass
    c.execute(f"SELECT worker_id, worker_prefix, worker_nick, working FROM job_programmer ORDER BY working DESC")
    items = c.fetchall()
    wd = []
    for el in items:
        for e in el:
            wd.append(e)
    if len(ud) < 3:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Программисты</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработано""", parse_mode="HTML")
    else:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Программисты</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработаноcs""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Программисты</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработаноcs


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
    db.commit()
    db.close()



@dp.message_handler(commands=['tetop', 'teacher_top'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT worker_id FROM job_teacher ORDER BY working DESC")
    items = c.fetchall()
    wil = []
    for el in items:
        num = 0
        for e in el:
            wil.append(e)
    ct = 1
    for t in wil:
        if t == message.from_user.id:
            break
        else:
            ct += 1
    c.execute(f"SELECT worker_prefix, worker_nick, working FROM job_teacher WHERE worker_id = {message.from_user.id}")
    items = c.fetchall()
    ud = []
    try:
        for el in items:
            ud.append(el[0])
            ud.append(el[1])
            ud.append(el[2])
    except:
        pass
    c.execute(f"SELECT worker_id, worker_prefix, worker_nick, working FROM job_teacher ORDER BY working DESC")
    items = c.fetchall()
    wd = []
    for el in items:
        for e in el:
            wd.append(e)
    if len(ud) < 3:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Учителя</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработано""", parse_mode="HTML")
    else:
        if len(wd) < 4:
            await message.answer("""Рейтинг работников: <b>Учителя</b>

Список пуст""", parse_mode="HTML")
        elif len(wd) == 4:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 8:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 12:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 16:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 20:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 24:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 28:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 32:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
        elif len(wd) == 36:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработаноcs""", parse_mode="HTML")
        else:
            await message.answer(f"""Рейтинг работников: <b>Учителя</b>

1. <b><i>[{wd[1]}]</i></b> <a href='tg://user?id={wd[0]}'>{wd[2]}</a>   |   {wd[3]} дней отработано
2. <b><i>[{wd[5]}]</i></b> <a href='tg://user?id={wd[4]}'>{wd[6]}</a>   |   {wd[7]} дней отработано
3. <b><i>[{wd[9]}]</i></b> <a href='tg://user?id={wd[8]}'>{wd[10]}</a>   |   {wd[11]} дней отработано
4. <b><i>[{wd[13]}]</i></b> <a href='tg://user?id={wd[12]}'>{wd[14]}</a>   |   {wd[15]} дней отработано
5. <b><i>[{wd[17]}]</i></b> <a href='tg://user?id={wd[16]}'>{wd[18]}</a>   |   {wd[19]} дней отработано
6. <b><i>[{wd[21]}]</i></b> <a href='tg://user?id={wd[20]}'>{wd[22]}</a>   |   {wd[23]} дней отработано
7. <b><i>[{wd[25]}]</i></b> <a href='tg://user?id={wd[24]}'>{wd[26]}</a>   |   {wd[27]} дней отработано
8. <b><i>[{wd[29]}]</i></b> <a href='tg://user?id={wd[28]}'>{wd[30]}</a>   |   {wd[31]} дней отработано
9. <b><i>[{wd[33]}]</i></b> <a href='tg://user?id={wd[32]}'>{wd[34]}</a>   |   {wd[35]} дней отработано
10. <b><i>[{wd[37]}]</i></b> <a href='tg://user?id={wd[36]}'>{wd[38]}</a>   |   {wd[39]} дней отработаноcs


<b>Вы:</b>
{round(ct)}. <b><i>[{ud[0]}]</i></b> {ud[1]}   |   {ud[2]} дней отработано""", parse_mode="HTML")
    db.commit()
    db.close()