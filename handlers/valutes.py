from aiogram import types
from dispatcher import dp
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery
import sqlite3

@dp.message_handler(commands=['cv'])
async def process_giveeclairs_command(message: types.Message):
    try:
        await message.answer(f"""<b>Курс валют:</b>

<b>Очки:</b>
10 000 очков - 1 монета
1 000 000 очков - 1 эклер

<b>Монеты:</b>
100 монет - 1 эклер

<b>Эклеры:</b>
1 000 000 эклеров - 1 фрибас
1 эклер - 1 000 000 очков

<b>Фрибасы:</b>
1 фрибас - 1 000 000 эклеров

<b>Чапчи:</b>
1 чапча - 1 000 000 000 000 эклеров
1 чапча - 1 000 000 фрибасов

/buypoints Число - купить очки
/buyeclairs Число - купить эклеры
/buycoins Число - купить монеты
/buyfreebases Число - купить фрибасы""", parse_mode="HTML")
    except:
        pass

@dp.message_handler(commands=['buyeclairs'])
async def process_ckb_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        be = True
        buyforpoints = InlineKeyboardButton("Заплатить очками", callback_data="befp")
        buyforcoins = InlineKeyboardButton("Заплатить монетами", callback_data="befc")
        buyforfreebases = InlineKeyboardButton("Заплатить фрибасами", callback_data="beff")
        buyforchapchas = InlineKeyboardButton("Заплатить чапчами", callback_data="befch")
        cncl = InlineKeyboardButton("Отмена", callback_data="cnclb")
        try:
            num = int(message.text.split(' ')[1])
        except:
            await message.answer("/buyeclairs Число")
            be = False
        if be:
            c.execute(f"UPDATE purchases SET sum_buy_eclairs = {num} WHERE user_id = {message.from_user.id}")
            c.execute(f"SELECT user_points, user_coins, user_freebases, user_chapchas FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                up = el[0]
                uc = el[1]
                uf = el[2]
                uch = el[3]
            floor = InlineKeyboardMarkup()
            if uc >= num * 100:
                floor = floor.add(buyforcoins)
            if up >= num * 1000000:
                floor = floor.add(buyforpoints)
            if num % 1000000 == 0:
                if uf >= num / 1000000:
                    floor = floor.add(buyforfreebases)
            if num % 1000000000000 == 0:
                if uch >= num / 1000000000000:
                    floor = floor.add(buyforchapchas)
            floor = floor.add(cncl)
            if uc < num * 100 and up < num * 1000000 and uf < num / 1000000 and uch < num / 1000000000000:
                await message.answer("Недостаточно средств!")
                be = False
            if be:
                await message.answer("<b>Выберите способ оплаты</b>", parse_mode="HTML", reply_markup=floor)
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="befp")
async def help_bt(call: types.CallbackQuery):
    buy = InlineKeyboardButton("Подтвердить покупку", callback_data="sbefp")
    cncl = InlineKeyboardButton("Отмена", callback_data="cnclb")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(buy).add(cncl)
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_points, user_eclairs FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            up = el[3]
            uec = el[4]
        c.execute(f"SELECT sum_buy_eclairs FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubec = el[0]
        await call.message.edit_text(f"""<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершает покупку</b>:

Покупка: <b>{ubec} эклеров</b>
Цена: <b>{ubec * 1000000} очков</b>""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="sbefp")
async def help_bt(call: types.CallbackQuery):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT sum_buy_eclairs FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubec = el[0]
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_points, user_eclairs FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            up = el[3]
            uec = el[4]
        if up >= ubec * 1000000:
            price_points = up - (ubec * 1000000)
            price_eclairs = uec + ubec
            c.execute(f"UPDATE purchases SET sum_buy_eclairs = 0 WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_points = {price_points}, user_eclairs = {price_eclairs} WHERE user_id = {call.from_user.id}")
            await call.message.edit_text(f"<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершил покупку!</b>", parse_mode="HTML")
        else:
            await call.message.edit_text("Недостаточно средств!")
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="befc")
async def help_bt(call: types.CallbackQuery):
    buy = InlineKeyboardButton("Подтвердить покупку", callback_data="sbefc")
    cncl = InlineKeyboardButton("Отмена", callback_data="cnclb")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(buy).add(cncl)
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            uc = el[3]
        c.execute(f"SELECT sum_buy_eclairs FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubec = el[0]
        await call.message.edit_text(f"""<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершает покупку</b>:

Покупка: <b>{ubec} эклеров</b>
Цена: <b>{ubec * 100} монет</b>""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="sbefc")
async def help_bt(call: types.CallbackQuery):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT sum_buy_eclairs FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubec = el[0]
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_coins, user_eclairs FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            uc = el[3]
            uec = el[4]
        if uc >= ubec * 100:
            price_coins = uc - (ubec * 100)
            price_eclairs = uec + ubec
            c.execute(f"UPDATE purchases SET sum_buy_eclairs = 0 WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins}, user_eclairs = {price_eclairs} WHERE user_id = {call.from_user.id}")
            await call.message.edit_text(f"<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершил покупку!</b>", parse_mode="HTML")
        else:
            await call.message.edit_text("Недостаточно средств!")
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()



@dp.callback_query_handler(text="beff")
async def help_bt(call: types.CallbackQuery):
    buy = InlineKeyboardButton("Подтвердить покупку", callback_data="sbeff")
    cncl = InlineKeyboardButton("Отмена", callback_data="cnclb")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(buy).add(cncl)
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_freebases FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            uf = el[3]
        c.execute(f"SELECT sum_buy_eclairs FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubec = el[0]
        await call.message.edit_text(f"""<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершает покупку</b>:

Покупка: <b>{ubec} эклеров</b>
Цена: <b>{round(ubec / 1000000)} фрибасов</b>""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="sbeff")
async def help_bt(call: types.CallbackQuery):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT sum_buy_eclairs FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubec = el[0]
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_freebases, user_eclairs FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            uf = el[3]
            uec = el[4]
        if uf >= ubec / 1000000:
            price_freebases = uf - round((ubec / 1000000))
            price_eclairs = uec + ubec
            c.execute(f"UPDATE purchases SET sum_buy_eclairs = 0 WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_freebases = {price_freebases}, user_eclairs = {price_eclairs} WHERE user_id = {call.from_user.id}")
            await call.message.edit_text(f"<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершил покупку!</b>", parse_mode="HTML")
        else:
            await call.message.edit_text("Недостаточно средств!")
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()



@dp.callback_query_handler(text="befch")
async def help_bt(call: types.CallbackQuery):
    buy = InlineKeyboardButton("Подтвердить покупку", callback_data="sbefch")
    cncl = InlineKeyboardButton("Отмена", callback_data="cnclb")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(buy).add(cncl)
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_chapchas FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            uch = el[3]
        c.execute(f"SELECT sum_buy_eclairs FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubec = el[0]
        await call.message.edit_text(f"""<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершает покупку</b>:

Покупка: <b>{ubec} эклеров</b>
Цена: <b>{round(ubec / 1000000000000)} чапчей</b>""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="sbefch")
async def help_bt(call: types.CallbackQuery):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT sum_buy_eclairs FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubec = el[0]
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_chapchas, user_eclairs FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            uch = el[3]
            uec = el[4]
        if uch >= ubec / 1000000000000:
            price_chapchas = uch - round((ubec / 1000000000000))
            price_eclairs = uec + ubec
            c.execute(f"UPDATE purchases SET sum_buy_eclairs = 0 WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_chapchas = {price_chapchas}, user_eclairs = {price_eclairs} WHERE user_id = {call.from_user.id}")
            await call.message.edit_text(f"<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершил покупку!</b>", parse_mode="HTML")
        else:
            await call.message.edit_text("Недостаточно средств!")
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()




@dp.message_handler(commands=['buycoins'])
async def process_ckb_command(message: types.Message):
    buy = InlineKeyboardButton("Подтвердить покупку", callback_data="sbcfp")
    cncl = InlineKeyboardButton("Отмена", callback_data="cnclb")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(buy).add(cncl)
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        be = True
        try:
            num = message.text.split(' ')[1]
        except:
            await message.answer("/buycoins Число")
            be = False
        if be:
            c.execute(f"UPDATE purchases SET sum_buy_coins = {num} WHERE user_id = {message.from_user.id}")
            db.commit()
            c.execute(f"SELECT user_id, user_prefix, user_nick, user_points FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                uid = el[0]
                upr = el[1]
                un = el[2]
                up = el[3]
            c.execute(f"SELECT sum_buy_coins FROM purchases WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                ubc = el[0]
            if up >= ubc * 10000:
                await message.answer(f"""<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершает покупку</b>:

Покупка: <b>{ubc} монет</b>
Цена: <b>{ubc * 10000} очков</b>""", parse_mode="HTML", reply_markup=floor)
            else:
                await message.answer("Недостаточно средств!")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="sbcfp")
async def help_bt(call: types.CallbackQuery):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT sum_buy_coins FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubc = el[0]
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_points, user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            up = el[3]
            uc = el[4]
        if up >= ubc * 10000:
            price_points = up - (ubc * 10000)
            price_coins = uc + ubc
            c.execute(f"UPDATE purchases SET sum_buy_coins = 0 WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_points = {price_points}, user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            await call.message.edit_text(f"<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершил покупку!</b>", parse_mode="HTML")
        else:
            await call.message.edit_text("Недостаточно средств!")
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()



@dp.message_handler(commands=['buyfreebases'])
async def process_ckb_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        be = True
        buyforeclairs = InlineKeyboardButton("Заплатить эклерами", callback_data="bffe")
        buyforchapchas = InlineKeyboardButton("Заплатить чапчами", callback_data="bffch")
        cncl = InlineKeyboardButton("Отмена", callback_data="cnclb")
        try:
            num = int(message.text.split(' ')[1])
        except:
            await message.answer("/buyfreebases Число")
            be = False
        if be:
            c.execute(f"UPDATE purchases SET sum_buy_freebases = {num} WHERE user_id = {message.from_user.id}")
            c.execute(f"SELECT user_eclairs, user_chapchas FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                uec = el[0]
                uch = el[1]
            floor = InlineKeyboardMarkup()
            if uec >= num * 1000000:
                floor = floor.add(buyforeclairs)
            if num % 1000000 == 0:
                if uch >= num / 1000000:
                    floor = floor.add(buyforchapchas)
            floor = floor.add(cncl)
            if uec < num * 1000000 and uch < num / 1000000:
                await message.answer("Недостаточно средств!")
                be = False
            if be:
                await message.answer("<b>Выберите способ оплаты</b>", parse_mode="HTML", reply_markup=floor)
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="bffe")
async def help_bt(call: types.CallbackQuery):
    buy = InlineKeyboardButton("Подтвердить покупку", callback_data="sbffe")
    cncl = InlineKeyboardButton("Отмена", callback_data="cnclb")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(buy).add(cncl)
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_eclairs FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            uec = el[3]
        c.execute(f"SELECT sum_buy_freebases FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubf = el[0]
        await call.message.edit_text(f"""<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершает покупку</b>:

Покупка: <b>{ubf} фрибасов</b>
Цена: <b>{ubf * 1000000} эклеров</b>""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="sbffe")
async def help_bt(call: types.CallbackQuery):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT sum_buy_freebases FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubf = el[0]
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_eclairs, user_freebases FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            uec = el[3]
            uf = el[4]
        if uec >= ubf * 1000000:
            price_eclairs = uec - (ubf * 1000000)
            price_freebases = uf + ubf
            c.execute(f"UPDATE purchases SET sum_buy_freebases = 0 WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_eclairs = {price_eclairs}, user_freebases = {price_freebases} WHERE user_id = {call.from_user.id}")
            await call.message.edit_text(f"<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершил покупку!</b>", parse_mode="HTML")
        else:
            await call.message.edit_text("Недостаточно средств!")
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()





@dp.callback_query_handler(text="bffch")
async def help_bt(call: types.CallbackQuery):
    buy = InlineKeyboardButton("Подтвердить покупку", callback_data="sbffch")
    cncl = InlineKeyboardButton("Отмена", callback_data="cnclb")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(buy).add(cncl)
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_chapchas FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            uch = el[3]
        c.execute(f"SELECT sum_buy_freebases FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubf = el[0]
        await call.message.edit_text(f"""<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершает покупку</b>:

Покупка: <b>{ubf} фрибасов</b>
Цена: <b>{round(ubf / 1000000)} чапчей</b>""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="sbffch")
async def help_bt(call: types.CallbackQuery):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT sum_buy_freebases FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubf = el[0]
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_chapchas, user_freebases FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            uch = el[3]
            uf = el[4]
        if uch >= ubf / 1000000:
            price_chapchas = uch - round((ubf / 1000000))
            price_freebases = uf + ubf
            c.execute(f"UPDATE purchases SET sum_buy_freebases = 0 WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_chapchas = {price_chapchas}, user_freebases = {price_freebases} WHERE user_id = {call.from_user.id}")
            await call.message.edit_text(f"<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершил покупку!</b>", parse_mode="HTML")
        else:
            await call.message.edit_text("Недостаточно средств!")
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()





@dp.message_handler(commands=['buypoints'])
async def process_ckb_command(message: types.Message):
    buy = InlineKeyboardButton("Подтвердить покупку", callback_data="sbpfe")
    cncl = InlineKeyboardButton("Отмена", callback_data="cnclb")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(buy).add(cncl)
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        be = True
        try:
            num = int(message.text.split(' ')[1])
        except:
            await message.answer("/buypoints Число")
            be = False
        if be:
            c.execute(f"UPDATE purchases SET sum_buy_points = {num} WHERE user_id = {message.from_user.id}")
            db.commit()
            c.execute(f"SELECT user_id, user_prefix, user_nick, user_eclairs FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                uid = el[0]
                upr = el[1]
                un = el[2]
                uec = el[3]
            c.execute(f"SELECT sum_buy_points FROM purchases WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                ubp = el[0]
            print(ubp)
            if ubp%1000000 != 0:
                ubp = round(ubp)
                print(ubp)
                if ubp%1000000 != 0:
                    ubp = str(ubp)
                    while int(ubp)%1000000 != 0:
                        ubp += "0"
                ubp = int(ubp)
                c.execute(f"UPDATE purchases SET sum_buy_points = {ubp} WHERE user_id = {message.from_user.id}")
                db.commit()
            while ubp%1000000 != 0:
                ubp = int(ubp[:1])
                print(ubp)
            if ubp%1000000 == 0:
                if uec >= ubp / 1000000:
                    await message.answer(f"""<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершает покупку</b>:

Покупка: <b>{ubp} очков</b>
Цена: <b>{round(ubp / 1000000)} эклеров</b>""", parse_mode="HTML", reply_markup=floor)
                else:
                    await message.answer("Недостаточно средств!")
            else:
                await message.answer("Минимальная сумма покупки 10 000 000 очков")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="sbpfe")
async def help_bt(call: types.CallbackQuery):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT sum_buy_points FROM purchases WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ubp = el[0]
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_points, user_eclairs FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uid = el[0]
            upr = el[1]
            un = el[2]
            up = el[3]
            uec = el[4]
        if uec >= ubp / 1000000:
            price_points = up + ubp
            price_eclairs = uec - round((ubp / 1000000))
            c.execute(f"UPDATE purchases SET sum_buy_points = 0 WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_points = {price_points}, user_eclairs = {price_eclairs} WHERE user_id = {call.from_user.id}")
            await call.message.edit_text(f"<b>Пользователь <i>[{upr}]</i> <a href='tg://user?id={uid}'>{un}</a> совершил покупку!</b>", parse_mode="HTML")
        else:
            await call.message.edit_text("Недостаточно средств!")
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()


@dp.callback_query_handler(text="cnclb")
async def help_bt(call: types.CallbackQuery):
    await call.message.edit_text("Покупка отменена")