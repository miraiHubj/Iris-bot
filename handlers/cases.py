from aiogram import types
from dispatcher import bot, dp
from random import randint
import sqlite3
import datetime

@dp.message_handler(text=['Кейсы', 'кейсы'])
async def process_auction_command(message: types.Message):
    try:
        await message.answer("""<b>Кейсы</b>

<code>Обычный кейс</code>
<code>Редкий кейс</code>
<code>Эпический кейс</code>
<code>Легендарный кейс</code>
<code>Мифический кейс</code>
<code>Ежедневный кейс</code>

<code>Открыть</code> Кейс - открыть кейс""", parse_mode="HTML")
    except:
        pass

@dp.message_handler(text=['Ключи', 'ключи'])
async def process_auction_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT up_kv, key_regular, key_rare, key_epic, key_legendary, key_mifik FROM game_case WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            kv = el[0]
            rk = el[1]
            rak = el[2]
            ek = el[3]
            lk = el[4]
            mk = el[5]
        c.execute(f"SELECT user_prefix, user_nick FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            up = el[0]
            un = el[1]
            ui = message.from_user.id
        if kv <= 49:
            mkv = 0
        else:
            mkv = (kv-49)/100
        if kv <= 36:
            lkv = 0
        else:
            lkv = (kv-36)/100
        if kv < 24:
            ekv = 0
        else:
            ekv = (kv-24)/100
        if kv < 24:
            rakv = 0
        else:
            rakv = (kv-12)/100
        rkv = kv/100
        c.execute(f"SELECT every_day_case FROM game_case WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            evc = el[0]
        evc = datetime.datetime.strptime(str(evc), '%Y-%m-%d %H:%M:%S')
        date_now = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        date_now = datetime.datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S')
        if date_now >= evc:
            evc = "Доступен"
        else:
            evc = "Недоступен"
        await message.answer(f"""<b>Ключи пользователя <i>[{up}]</i> <a href='tg://user?id={ui}'>{un}</a>:</b>

Обычный кейс: <b>{rk} ключей</b>     | {rkv}%
Редкий кейс: <b>{rak} ключей</b>     | {rakv}%
Эпический кейс: <b>{ek} ключей</b>   | {ekv}%
Легендарный кейс: <b>{lk} ключей</b> | {lkv}%
Мифический кейс: <b>{mk} ключей</b>  | {mkv}%
Ежедневный кейс: <b>{evc}</b>""", parse_mode="HTML")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.message_handler(text=['Открыть обычный кейс', 'Открыть ок', '!ок'])
async def process_auction_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT up_pr, key_regular FROM game_case WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            pr = el[0]
            keys = el[1]
        c.execute(f"SELECT user_nick, user_coins FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            uc = el[1]
        if kyes > 0:
            price = randint(5, pr)
            price_coins = uc + price
            price_keys = uk - 1
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {message.from_user.id}")
            c.execute(f"UPDATE game_case SET key_regular = {price_keys} WHERE user_id = {message.from_user.id}")
            await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{un}</a> получил <b>{farm} монет</b> из обычного кейса!", parse_mode="HTML")
        else:
            await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{un}</a> у Вас нету ключей от обычного кейса")
        db.commit()
        db.close()
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")

@dp.message_handler(text=['Открыть редкий кейс', 'Открыть рк', '!рк'])
async def process_auction_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT up_pr, key_rare FROM game_case WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            pr = el[0]
            keys = el[1]
        c.execute(f"SELECT user_nick, user_coins FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            uc = el[1]
        if kyes > 0:
            price = randint(10, pr*2)
            price_coins = uc + price
            price_keys = uk - 1
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {message.from_user.id}")
            c.execute(f"UPDATE game_case SET key_rare = {price_keys} WHERE user_id = {message.from_user.id}")
            await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{un}</a> получил <b>{farm} монет</b> из редкого кейса!", parse_mode="HTML")
        else:
            await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{un}</a> у Вас нету ключей от редкого кейса")
        db.commit()
        db.close()
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")

@dp.message_handler(text=['Открыть эпический кейс', 'Открыть эк', '!эк'])
async def process_auction_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT up_pr, key_epic FROM game_case WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            pr = el[0]
            keys = el[1]
        c.execute(f"SELECT user_nick, user_coins FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            uc = el[1]
        if kyes > 0:
            price = randint(15, pr*3)
            price_coins = uc + price
            price_keys = uk - 1
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {message.from_user.id}")
            c.execute(f"UPDATE game_case SET key_epic = {price_keys} WHERE user_id = {message.from_user.id}")
            await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{un}</a> получил <b>{farm} монет</b> из эпического кейса!", parse_mode="HTML")
        else:
            await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{un}</a> у Вас нету ключей от эпического кейса")
        db.commit()
        db.close()
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")

@dp.message_handler(text=['Открыть легендарный кейс', 'Открыть лк', '!лк'])
async def process_auction_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT up_pr, key_legendary FROM game_case WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            pr = el[0]
            keys = el[1]
        c.execute(f"SELECT user_nick, user_coins FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            uc = el[1]
        if kyes > 0:
            price = randint(20, pr*4)
            price_coins = uc + price
            price_keys = uk - 1
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {message.from_user.id}")
            c.execute(f"UPDATE game_case SET key_legendary = {price_keys} WHERE user_id = {message.from_user.id}")
            await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{un}</a> получил <b>{farm} монет</b> из легендарного кейса!", parse_mode="HTML")
        else:
            await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{un}</a> у Вас нету ключей от обычного кейса")
        db.commit()
        db.close()
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")

@dp.message_handler(text=['Открыть мифический кейс', 'Открыть мк', '!мк'])
async def process_auction_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT up_pr, key_mifik FROM game_case WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            pr = el[0]
            keys = el[1]
        c.execute(f"SELECT user_nick, user_coins FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            uc = el[1]
        if kyes > 0:
            price = randint(25, pr*5)
            price_coins = uc + price
            price_keys = uk - 1
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {message.from_user.id}")
            c.execute(f"UPDATE game_case SET key_mifik = {price_keys} WHERE user_id = {message.from_user.id}")
            await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{un}</a> получил <b>{farm} монет</b> из мифический кейса!", parse_mode="HTML")
        else:
            await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{un}</a> у Вас нету ключей от обычного кейса")
        db.commit()
        db.close()
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")