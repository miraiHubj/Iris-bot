from aiogram import types
from dispatcher import dp, bot
import sqlite3

@dp.message_handler(commands=['clan_prefixes', 'clanpref'])
async def process_balance_command(message: types.Message):
    await message.answer("""<b>Префиксы клана:</b>

1. <code>Бомжатник</code> - 100 000 эклеров
2. <code>Крысы</code> - 250 000 эклеров
3. <code>Немощи</code> - 500 000 эклеров
4. <code>Ясельки</code> - 750 000 эклеров
5. <code>Курятник</code> - 1 000 000 эклеров
6. <code>Проходной дворик</code> - 2 500 000 эклеров
7. <code>Детдом</code> - 5 000 000 эклеров
8. <code>Anonymous228</code> - 7 500 000
9. <code>Приват зона</code> - 10 000 000 эклеров
10. <code>Тюряга</code> - 10 000 фрибасов
11. <code>Минекруфт сервер</code> - 25 000 фрибасов
12. <code>ГейКлуб</code> - 50 000 фрибасов
13. <code>Женский туалет</code> - 75 000 фрибасов
14. <code>Дети Фриби</code> - 100 000 фрибасов
15. <code>Царство</code> - 100 000 чапчей
16. <code>Главари</code> - 1 000 000 чапчей

/buy_clan_prefix Префикс - купить префикс""", parse_mode="HTML")

#qsbuyprefix
@dp.message_handler(commands=['buy_clan_prefix'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        pr = message.text[17:]
        c.execute(f"SELECT clan_prefix FROM clan_data WHERE leader_id = {message.from_user.id}")
        items = c.fetchall()
        for p in items:
            cp = p[0]
        if p == '' or p == None or p == 'None':
            await message.answer("У Вас нету клана")
        else:
            if cp == 'Общага':
                pn = 0
            elif cp == 'Бомжатник':
                pn = 1
            elif cp == 'Крысы':
                pn = 2
            elif cp == 'Немощи':
                pn = 3
            elif cp == 'Яселька':
                pn = 4
            elif cp == 'Курятник':
                pn = 5
            elif cp == 'Проходной дворик':
                pn = 6
            elif cp == 'Детдом':
                pn = 7
            elif cp == 'Anonymous228':
                pn = 8
            elif cp == 'Приват зона':
                pn = 9
            elif cp == 'Тюряга':
                pn = 10
            elif cp == 'Минекруфт сервер':
                pn = 11
            elif cp == 'ГейКлуб':
                pn = 12
            elif cp == 'Женский туалет':
                pn = 13
            elif cp == 'Дети Фриби':
                pn = 14
            elif cp == 'Царство':
                pn = 15
            elif cp == 'Главари':
                pn = 16
            else:
                pn = 17
            
            if pr == 'Бомжатник':
                prn = 1
            elif pr == 'Крысы':
                prn = 2
            elif pr == 'Немощи':
                prn = 3
            elif pr == 'Яселька':
                prn = 4
            elif pr == 'Курятник':
                prn = 5
            elif pr == 'Проходной дворик':
                prn = 6
            elif pr == 'Детдом':
                prn = 7
            elif pr == 'Anonymous228':
                prn = 8
            elif pr == 'Приват зона':
                prn = 9
            elif pr == 'Тюряга':
                prn = 10
            elif pr == 'Минекруфт сервер':
                prn = 11
            elif pr == 'ГейКлуб':
                prn = 12
            elif pr == 'Женский туалет':
                prn = 13
            elif pr == 'Дети Фриби':
                prn = 14
            elif pr == 'Царство':
                prn = 15
            elif pr == 'Главари':
                prn = 16
            elif pr == '' or pr == ' ':
                print(forerrorprint)
            else:
                prn = 17
            c.execute(f"SELECT user_eclairs, user_chapchas, user_freebases FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for i in items:
                uec = i[0]
                uch = i[1]
                ufr = i[2]
            if prn == pn:
                await message.answer("У Вашего клана уже установлен такой префикс")
            elif prn > pn:
                if prn == 1:
                    if uec >= 100000:
                        price_eclairs = uec - 100000
                        c.execute(f"UPDATE user_data SET user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 2:
                    if uec >= 250000:
                        price_eclairs = uec - 250000
                        c.execute(f"UPDATE user_data SET user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 3:
                    if uec >= 500000:
                        price_eclairs = uec - 500000
                        c.execute(f"UPDATE user_data SET user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 4:
                    if uec >= 750000:
                        price_eclairs = uec - 750000
                        c.execute(f"UPDATE user_data SET user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 5:
                    if uec >= 1000000:
                        price_eclairs = uec - 1000000
                        c.execute(f"UPDATE user_data SET user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 6:
                    if uec >= 2500000:
                        price_eclairs = uec - 2500000
                        c.execute(f"UPDATE user_data SET user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 7:
                    if uec >= 5000000:
                        price_eclairs = uec - 5000000
                        c.execute(f"UPDATE user_data SET user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 8:
                    if uec >= 7500000:
                        price_eclairs = uec - 7500000
                        c.execute(f"UPDATE user_data SET user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 9:
                    if uec >= 10000000:
                        price_eclairs = uec - 10000000
                        c.execute(f"UPDATE user_data SET user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 10:
                    if ufr >= 10000:
                        price_eclairs = ufr - 10000
                        c.execute(f"UPDATE user_data SET user_freebases = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 11:
                    if ufr >= 25000:
                        price_eclairs = ufr - 25000
                        c.execute(f"UPDATE user_data SET user_freebases = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 12:
                    if ufr >= 50000:
                        price_eclairs = ufr - 50000
                        c.execute(f"UPDATE user_data SET user_freebases = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 13:
                    if ufr >= 75000:
                        price_eclairs = ufr - 75000
                        c.execute(f"UPDATE user_data SET user_freebases = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 14:
                    if ufr >= 100000:
                        price_eclairs = ufr - 100000
                        c.execute(f"UPDATE user_data SET user_freebases = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                elif prn == 15:
                    if uch >= 100000:
                        price_eclairs = uch - 100000
                        c.execute(f"UPDATE user_data SET user_chapchas = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                elif prn == 16:
                    if uch >= 1000000:
                        price_eclairs = uch - 1000000
                        c.execute(f"UPDATE user_data SET user_chapchas = {price_eclairs} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE clan_data SET clan_prefix = '{pr}' WHERE leader_id = {message.from_user.id}")
                        await message.answer("Префикс клана установлен!")
                    else:
                        await message.answer("Недостаточно средств")
                else:
                    await message.answer("Префикс не найден")
            else:
                await message.answer("Префикс клана выше")
    except:
        await message.answer("/buy_clan_prefix Префикс")
    db.commit()
    db.close()