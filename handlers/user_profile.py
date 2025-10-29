from aiogram import types
from dispatcher import dp
import sqlite3

@dp.message_handler(commands=['profile', 'prof'])
async def profile(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
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
        if li == 0 and mbn == 0:
            cn = 'Отсутствует'
        else:
            if mbn != 0:
                c.execute(f"SELECT clan_name, clan_prefix FROM clan_data WHERE mb{mbn} = {message.from_user.id}")
            else:
                c.execute(f"SELECT clan_name, clan_prefix FROM clan_data WHERE leader_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                cn = el[0]
                cpr = el[1]
        c.execute(f"SELECT * FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        udl = []
        for el in items:
            for e in el:
                udl.append(e)
        ud = []
        for el in udl:
            if el == '' or el == None:
                ud.append("Нету")
            else:
                ud.append(el)
        c.execute(f"SELECT * FROM nicks_auction WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        unl = []
        for el in items:
            unl.append(el[2])
            unl.append(el[3])
            unl.append(el[4])
            unl.append(el[5])
            unl.append(el[6])
            unl.append(el[7])
            unl.append(el[8])
            unl.append(el[9])
        un = []
        for el in unl:
            if el == '' or el == None:
                un.append("Нету")
            else:
                un.append(el)
        if ud[8] == 'Нету':
            brak = 0
        else:
            brak = ud[8]
        if brak != 0:
            try:
                if brak == message.from_user.id:
                    c.execute(f"SELECT user2_id FROM mary WHERE user1_id = {brak}")
                else:
                    c.execute(f"SELECT user1_id FROM mary WHERE user2_id = {brak}")
                items = c.fetchall()
                for el in items:
                    pai = el[0]
                c.execute(f"SELECT user_prefix, user_nick FROM user_data WHERE user_id = {pai}")
                items = c.fetchall()
                for el in items:
                    pap = el[0]
                    pan = el[1]
            except:
                pass
        if brak == 0:
            if cn == 'Отсутствует':
                await message.answer(f"""👤 | <b>Профиль <i>[{ud[3]}]</i> <a href='tg://user?id={message.from_user.id}'>{ud[4]}</a></b>:

🆔 | ID:  <code>{ud[0]}</code>
💬 | Чат ID: <code>{message.chat.id}</code>
🏷 | Имя пользователя:  @{ud[1]}
🏷 | Имя:  {ud[2]}


🔰 | Префикс: <b><i>[{ud[3]}]</i></b>
🏷 | Ник в боте:  {ud[4]}
⭐️ | Репутация:  {ud[5]}
💼 | Профессия: <b>{ud[7]}</b>

📅 | Первое появление в боте:  {ud[6]}


🏷 | <b>Ник на продаже:</b>
📅 | Дата появления: {un[0]}
🏷 | Ник: {un[1]}
💲 | Цена: {un[2]}


🏷 | <b>Ники в мешке:</b>
🏷 | 1. <code>{un[3]}</code>
🏷 | 2. <code>{un[4]}</code>
🏷 | 3. <code>{un[5]}</code>
🏷 | 4. <code>{un[6]}</code>
🏷 | 5. <code>{un[7]}</code>


💰 | <b>В кошельке:</b>
🎰 | <b>Игровые очки:</b>
🎫 | Очки: {ud[9]}

💵 | <b>Обычная валюта:</b>
🧁 | Эклеры: {ud[10]}
🪙 | Монеты: {ud[11]}

💶 | <b>Драгоценная валюта:</b>
💎 | Чапчи: {ud[12]}
🪅 | Фрибасы: {ud[13]}""", parse_mode="HTML")
            else:
                await message.answer(f"""👤 | <b>Профиль <i>[{ud[3]}]</i> <a href='tg://user?id={message.from_user.id}'>{ud[4]}</a></b>:

🆔 | ID:  <code>{ud[0]}</code>
💬 | Чат ID: <code>{message.chat.id}</code>
🏷 | Имя пользователя:  @{ud[1]}
🏷 | Имя:  {ud[2]}


🔰 | Префикс: <b><i>[{ud[3]}]</i></b>
🏷 | Ник в боте:  {ud[4]}
⭐️ | Репутация:  {ud[5]}
💼 | Профессия: {ud[7]}

⚜️ | Клан: <b><i>[{cpr}]</i></b> {cn}

📅 | Первое появление в боте:  {ud[6]}


🏷 | <b>Ник на продаже:</b>
📅 | Дата появления: {un[0]}
🏷 | Ник: {un[1]}
💲 | Цена: {un[2]}


🏷 | <b>Ники в мешке:</b>
🏷 | 1. <code>{un[3]}</code>
🏷 | 2. <code>{un[4]}</code>
🏷 | 3. <code>{un[5]}</code>
🏷 | 4. <code>{un[6]}</code>
🏷 | 5. <code>{un[7]}</code>


💰 | <b>В кошельке:</b>
🎰 | <b>Игровые очки:</b>
🎫 | Очки: {ud[9]}

💵 | <b>Обычная валюта:</b>
🧁 | Эклеры: {ud[10]}
🪙 | Монеты: {ud[11]}

💶 | <b>Драгоценная валюта:</b>
💎 | Чапчи: {ud[12]}
🪅 | Фрибасы: {ud[13]}""", parse_mode="HTML")
        else:
            if cn == 'Отсутствует':
                await message.answer(f"""👤 | <b>Профиль <i>[{ud[3]}]</i> <a href='tg://user?id={message.from_user.id}'>{ud[4]}</a></b>:

🆔 | ID:  <code>{ud[0]}</code>
💬 | Чат ID: <code>{message.chat.id}</code>
🏷 | Имя пользователя:  @{ud[1]}
🏷 | Имя:  {ud[2]}


🔰 | Префикс: <b><i>[{ud[3]}]</i></b>
🏷 | Ник в боте:  {ud[4]}
⭐️ | Репутация:  {ud[5]}
💼 | Профессия: <b>{ud[7]}</b>
💝 | В браке с <b><i>[{pap}]</i> <a href='tg://user?id={pai}'>{pan}</a></b>

📅 | Первое появление в боте:  {ud[6]}


🏷 | <b>Ник на продаже:</b>
📅 | Дата появления: {un[0]}
🏷 | Ник: {un[1]}
💲 | Цена: {un[2]}


🏷 | <b>Ники в мешке:</b>
🏷 | 1. <code>{un[3]}</code>
🏷 | 2. <code>{un[4]}</code>
🏷 | 3. <code>{un[5]}</code>
🏷 | 4. <code>{un[6]}</code>
🏷 | 5. <code>{un[7]}</code>


💰 | <b>В кошельке:</b>
🎰 | <b>Игровые очки:</b>
🎫 | Очки: {ud[9]}

💵 | <b>Обычная валюта:</b>
🧁 | Эклеры: {ud[10]}
🪙 | Монеты: {ud[11]}

💶 | <b>Драгоценная валюта:</b>
💎 | Чапчи: {ud[12]}
🪅 | Фрибасы: {ud[13]}""", parse_mode="HTML")
            else:
                await message.answer(f"""👤 | <b>Профиль <i>[{ud[3]}]</i> <a href='tg://user?id={message.from_user.id}'>{ud[4]}</a></b>:

🆔 | ID:  <code>{ud[0]}</code>
💬 | Чат ID: <code>{message.chat.id}</code>
🏷 | Имя пользователя:  @{ud[1]}
🏷 | Имя:  {ud[2]}


🔰 | Префикс: <b><i>[{ud[3]}]</i></b>
🏷 | Ник в боте:  {ud[4]}
⭐️ | Репутация:  {ud[5]}
💼 | Профессия: {ud[7]}
💝 | В браке с <b><i>[{pap}]</i> <a href='tg://user?id={pai}'>{pan}</a></b>

⚜️ | Клан: <b><i>[{cpr}]</i></b> {cn}

📅 | Первое появление в боте:  {ud[6]}


🏷 | <b>Ник на продаже:</b>
📅 | Дата появления: {un[0]}
🏷 | Ник: {un[1]}
💲 | Цена: {un[2]}


🏷 | <b>Ники в мешке:</b>
🏷 | 1. <code>{un[3]}</code>
🏷 | 2. <code>{un[4]}</code>
🏷 | 3. <code>{un[5]}</code>
🏷 | 4. <code>{un[6]}</code>
🏷 | 5. <code>{un[7]}</code>


💰 | <b>В кошельке:</b>
🎰 | <b>Игровые очки:</b>
🎫 | Очки: {ud[9]}

💵 | <b>Обычная валюта:</b>
🧁 | Эклеры: {ud[10]}
🪙 | Монеты: {ud[11]}

💶 | <b>Драгоценная валюта:</b>
💎 | Чапчи: {ud[12]}
🪅 | Фрибасы: {ud[13]}""", parse_mode="HTML")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.message_handler(commands=['balance', 'b'])
async def balance(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT user_prefix, user_nick, user_points, user_eclairs, user_coins, user_chapchas, user_freebases FROM user_data WHERE user_id = {message.from_user.id}")
    items = c.fetchall()
    for el in items:
        await message.answer(f"""💰 | <b>В кошельке <i>[{el[0]}]</i> <a href='tg://user?id={message.from_user.id}'>{el[1]}</a></b>:

🎰 | <b>Игровые очки:</b>
🎫 | Очки: {el[2]}

💵 | <b>Обычная валюта:</b>
🧁 | Эклеры: {el[3]}
🪙 | Монеты: {el[4]}

💶 | <b>Драгоценная валюта:</b>
💎 | Чапчи: {el[5]}
🪅 | Фрибасы: {el[6]}""", parse_mode="HTML")
    db.commit()
    db.close()