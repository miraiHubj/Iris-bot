from aiogram import types
from dispatcher import dp
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery
import sqlite3

@dp.message_handler(commands=['upgrades', 'ups'])
async def upgrades(message: types.Message):
    ppc = InlineKeyboardButton("👆 Мощность клика", callback_data='ppcbtn')
    dp = InlineKeyboardButton("💯 Шанс двойной мощности", callback_data='dpbtn')
    farm = InlineKeyboardButton("💰 Добыча фарма", callback_data='farmbtn')
    ft = InlineKeyboardButton("⌛️ Интервал фарма", callback_data='ftbtn')
    cx = InlineKeyboardButton("♨️ Множитель ставки кубика", callback_data='cxbtn')
    cx = InlineKeyboardButton("♨️ Кубик", callback_data='cxbtn')
    smx = InlineKeyboardButton("♨️ Рулетка", callback_data='smxbtn')
    dx = InlineKeyboardButton("♨️ Дартс", callback_data='dxbtn')
    bag = InlineKeyboardButton("💰 Мешок", callback_data='bagbtn')
    st = InlineKeyboardButton("🕶 Скрытность", callback_data='stbtn')
    s = InlineKeyboardButton("🕵️ Безопасность", callback_data='sbtn')
    pr = InlineKeyboardButton("💰 Дроп из кейса", callback_data='prbtn')
    kv = InlineKeyboardButton("💯 Шанс нахождения ключа", callback_data='kvbtn')
    floor = InlineKeyboardMarkup(row_width=2)
    floor.row(ppc, dp)
    floor.row(farm, ft)
    floor.row(cx, smx, dx)
    floor.row(bag, st, s)
    floor.row(pr, kv)
    await message.answer("<b>🆙 Выберите улучшение</b>", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text="backtoupsbtn")
async def back_to_upgrades(call: types.CallbackQuery):
    ppc = InlineKeyboardButton("👆 Мощность клика", callback_data='ppcbtn')
    dp = InlineKeyboardButton("💯 Шанс двойной мощности", callback_data='dpbtn')
    farm = InlineKeyboardButton("💰 Добыча фарма", callback_data='farmbtn')
    ft = InlineKeyboardButton("⌛️ Интервал фарма", callback_data='ftbtn')
    cx = InlineKeyboardButton("♨️ Кубик", callback_data='cxbtn')
    smx = InlineKeyboardButton("♨️ Рулетка", callback_data='smxbtn')
    dx = InlineKeyboardButton("♨️ Дартс", callback_data='dxbtn')
    bag = InlineKeyboardButton("💰 Мешок", callback_data='bagbtn')
    st = InlineKeyboardButton("🕶 Скрытность", callback_data='stbtn')
    s = InlineKeyboardButton("🕵️ Безопасность", callback_data='sbtn')
    pr = InlineKeyboardButton("💰 Дроп из кейса", callback_data='prbtn')
    kv = InlineKeyboardButton("💯 Шанс нахождения ключа", callback_data='kvbtn')
    floor = InlineKeyboardMarkup(row_width=2)
    floor.row(ppc, dp)
    floor.row(farm, ft)
    floor.row(cx, smx, dx)
    floor.row(bag, st, s)
    floor.row(pr, kv)
    await call.message.edit_text("<b>🆙 Выберите улучшение</b>", parse_mode="HTML", reply_markup=floor)


@dp.callback_query_handler(text="ppcbtn")
async def points_per_click(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upppcbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_ppc, up_ppc, cena_ppc FROM game_clicker WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_ppc = el[0]
            up_ppc = el[1]
            cena_ppc = el[2]
        if lvl_ppc >= 1000:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
            await call.message.edit_text(f"""<b>👆 | Мощность клика</b>

<b>⬆️ | Уровень:</b> MAX
<b>👆 | Мощность клика:</b> {up_ppc} очков""", parse_mode="HTML", reply_markup=floor)
        else:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
            await call.message.edit_text(f"""<b>👆 | Мощность клика</b>

<b>⬆️ | Уровень:</b> {lvl_ppc}
<b>👆 | Мощность клика:</b> {up_ppc} очков

<b>🆙 | Улучшение:</b> {up_ppc} очков ➡️ {up_ppc + 1} очков
<b>💲 | Цена:</b> {cena_ppc} монет""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="upppcbtn")
async def up_points_per_click(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upppcbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_ppc, up_ppc, cena_ppc FROM game_clicker WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_ppc = el[0]
            up_ppc = el[1]
            cena_ppc = el[2]
        c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uc = el[0]
        if uc >= cena_ppc:
            lvl_ppc += 1
            up_ppc += 1
            price_coins = uc - cena_ppc
            cena_ppc += 1000
            c.execute(f"UPDATE game_clicker SET lvl_ppc = {lvl_ppc}, up_ppc = {up_ppc}, cena_ppc = {cena_ppc} WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            if lvl_ppc >= 1000:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
                await call.message.edit_text(f"""<b>👆 | Мощность клика</b>

<b>⬆️ | Уровень:</b> MAX
<b>👆 | Мощность клика:</b> {up_ppc} очков""", parse_mode="HTML", reply_markup=floor)
            else:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
                await call.message.edit_text(f"""<b>👆 | Мощность клика</b>

<b>⬆️ | Уровень:</b> {lvl_ppc}
<b>👆 | Мощность клика:</b> {up_ppc} очков

<b>🆙 | Улучшение:</b> {up_ppc} очков ➡️ {up_ppc + 1} очков
<b>💲 | Цена:</b> {cena_ppc} монет""", parse_mode="HTML", reply_markup=floor)
            await call.answer('Мощность клика улучшена!')
        else:
            await call.answer('Недостаточно средств!')
            
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()


@dp.callback_query_handler(text="dpbtn")
async def double_points(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='updpbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_dp, up_dp, cena_dp FROM game_clicker WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_dp = el[0]
            up_dp = el[1]
            cena_dp = el[2]
        if lvl_dp >= 75:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
            await call.message.edit_text(f"""<b>💯 | Шанс двойной мощности</b>

<b>⬆️ | Уровень:</b> MAX
<b>💯 | Шанс двойной мощности:</b> {up_dp}%""", parse_mode="HTML", reply_markup=floor)
        else:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
            await call.message.edit_text(f"""<b>💯 | Шанс двойной мощности</b>

<b>⬆️ | Уровень:</b> {lvl_dp}
<b>💯 | Шанс двойной мощности:</b> {up_dp}%

<b>🆙 | Улучшение:</b> {up_dp}% ➡️ {up_dp + 1}%
<b>💲 | Цена:</b> {cena_dp} монет""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="updpbtn")
async def up_double_points(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='updpbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_dp, up_dp, cena_dp FROM game_clicker WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_dp = el[0]
            up_dp = el[1]
            cena_dp = el[2]
        c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uc = el[0]
        if uc >= cena_dp:
            lvl_dp += 1
            up_dp += 1
            price_coins = uc - cena_dp
            cena_dp += 10000
            c.execute(f"UPDATE game_clicker SET lvl_dp = {lvl_dp}, up_dp = {up_dp}, cena_dp = {cena_dp} WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            if lvl_dp >= 75:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
                await call.message.edit_text(f"""<b>💯 | Шанс двойной мощности</b>

<b>⬆️ | Уровень:</b> MAX
<b>💯 | Шанс двойной мощности:</b> {up_dp}%""", parse_mode="HTML", reply_markup=floor)
            else:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
                await call.message.edit_text(f"""<b>💯 | Шанс двойной мощности</b>

<b>⬆️ | Уровень:</b> {lvl_dp}
<b>💯 | Шанс двойной мощности:</b> {up_dp}%

<b>🆙 | Улучшение:</b> {up_dp}% ➡️ {up_dp + 1}%
<b>💲 | Цена:</b> {cena_dp} монет""", parse_mode="HTML", reply_markup=floor)
            await call.answer('Шанс двойной мощности улучшен!')
        else:
            await call.answer('Недостаточно средств!')
            
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()





@dp.callback_query_handler(text="farmbtn")
async def help_bt(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upfarmbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_farm, up_farm, cena_farm FROM game_farm WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_farm = el[0]
            up_farm = el[1]
            cena_farm = el[2]
        if lvl_farm >= 1000:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
            await call.message.edit_text(f"""<b>💰 | Добыча фарма</b>

<b>⬆️ | Уровень:</b> MAX
<b>💰 | Добыча фарма:</b> {up_farm} очков""", parse_mode="HTML", reply_markup=floor)
        else:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
            await call.message.edit_text(f"""<b>💰 | Добыча фарма</b>

<b>⬆️ | Уровень:</b> {lvl_farm}
<b>💰 | Добыча фарма:</b> {up_farm} очков

<b>🆙 | Улучшение:</b> {up_farm} очков ➡️ {up_farm + 100} очков
<b>💲 | Цена:</b> {cena_farm} монет""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="upfarmbtn")
async def help_bt(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upfarmbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_farm, up_farm, cena_farm FROM game_farm WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_farm = el[0]
            up_farm = el[1]
            cena_farm = el[2]
        c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uc = el[0]
        if uc >= cena_farm:
            lvl_farm += 1
            up_farm += 100
            price_coins = uc - cena_farm
            cena_farm += 100000
            c.execute(f"UPDATE game_farm SET lvl_farm = {lvl_farm}, up_farm = {up_farm}, cena_farm = {cena_farm} WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            if lvl_farm >= 100000:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
                await call.message.edit_text(f"""<b>💰 | Добыча фарма</b>

<b>⬆️ | Уровень:</b> MAX
<b>💰 | Добыча фарма:</b> {up_farm} очков""", parse_mode="HTML", reply_markup=floor)
            else:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
                await call.message.edit_text(f"""<b>💰 | Добыча фарма</b>

<b>⬆️ | Уровень:</b> {lvl_farm}
<b>💰 | Добыча фарма:</b> {up_farm} очков

<b>🆙 | Улучшение:</b> {up_farm} очков ➡️ {up_farm + 100} очков
<b>💲 | Цена:</b> {cena_farm} монет""", parse_mode="HTML", reply_markup=floor)
            await call.answer('Добыча фарма улучшена!')
        else:
            await call.answer('Недостаточно средств!')
            
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()


@dp.callback_query_handler(text="ftbtn")
async def help_bt(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upftbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_ft, up_ft, cena_ft FROM game_farm WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_ft = el[0]
            up_ft = el[1]
            cena_ft = el[2]
        if lvl_ft >= 5:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
            await call.message.edit_text(f"""<b>⌛️ | Интервал фарма</b>

<b>⬆️ | Уровень:</b> MAX
<b>⌛️ | Интервал фарма:</b> {up_ft} часов""", parse_mode="HTML", reply_markup=floor)
        else:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
            await call.message.edit_text(f"""<b>⌛️ | Интервал фарма</b>

<b>⬆️ | Уровень:</b> {lvl_ft}
<b>⌛️ | Интервал фарма:</b> {up_ft} часов

<b>🆙 | Улучшение:</b> {up_ft} часов ➡️ {up_ft - 1} часов
<b>💲 | Цена:</b> {cena_ft} монет""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="upftbtn")
async def help_bt(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upftbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_ft, up_ft, cena_ft FROM game_farm WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_ft = el[0]
            up_ft = el[1]
            cena_ft = el[2]
        c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uc = el[0]
        if uc >= cena_ft:
            lvl_ft += 1
            up_ft -= 1
            price_coins = uc - cena_ft
            cena_ft += 1000
            c.execute(f"UPDATE game_farm SET lvl_ft = {lvl_ft}, up_ft = {up_ft}, cena_ft = {cena_ft} WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            if lvl_ft >= 5:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
                await call.message.edit_text(f"""<b>⌛️ | Интервал фарма</b>

<b>⬆️ | Уровень:</b> MAX
<b>⌛️ | Интервал фарма:</b> {up_ft} часов""", parse_mode="HTML", reply_markup=floor)
            else:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
                await call.message.edit_text(f"""<b>⌛️ | Интервал фарма</b>

<b>⬆️ | Уровень:</b> {lvl_ft}
<b>⌛️ | Интервал фарма:</b> {up_ft} часов

<b>🆙 | Улучшение:</b> {up_ft} часов ➡️ {up_ft - 1} часов
<b>💲 | Цена:</b> {cena_ft} монет""", parse_mode="HTML", reply_markup=floor)
            await call.answer('Интервал фарма улучшен!')
        else:
            await call.answer('Недостаточно средств!')
            
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()






@dp.callback_query_handler(text="cxbtn")
async def help_bt(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upcxbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_x, up_x, cena_x FROM game_cube WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_x = el[0]
            up_x = el[1]
            cena_x = el[2]
        if up_x >= 10:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
            await call.message.edit_text(f"""<b>♨️ | Множитель ставки кубика</b>

<b>⬆️ | Уровень:</b> MAX
<b>♨️ | Множитель ставки кубика:</b> {up_x}x""", parse_mode="HTML", reply_markup=floor)
        else:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
            await call.message.edit_text(f"""<b>♨️ | Множитель ставки кубика</b>

<b>⬆️ | Уровень:</b> {lvl_x}
<b>♨️ | Множитель ставки кубика:</b> {up_x}x

<b>🆙 | Улучшение:</b> {up_x}x ➡️ {up_x + 0.5}x
<b>💲 | Цена:</b> {cena_x} монет""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="upcxbtn")
async def help_bt(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upcxbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_x, up_x, cena_x FROM game_cube WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_x = el[0]
            up_x = el[1]
            cena_x = el[2]
        c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uc = el[0]
        if uc >= cena_x:
            lvl_x += 1
            up_x += 0.5
            price_coins = uc - cena_x
            cena_x += 5000
            c.execute(f"UPDATE game_cube SET lvl_x = {lvl_x}, up_x = {up_x}, cena_x = {cena_x} WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            if up_x >= 10:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
                await call.message.edit_text(f"""<b>♨️ | Множитель ставки кубика</b>

<b>⬆️ | Уровень:</b> MAX
<b>♨️ | Множитель ставки кубика:</b> {up_x}x""", parse_mode="HTML", reply_markup=floor)
            else:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
                await call.message.edit_text(f"""<b>♨️ | Множитель ставки кубика</b>

<b>⬆️ | Уровень:</b> {lvl_x}
<b>♨️ | Множитель ставки кубика:</b> {up_x}x

<b>🆙 | Улучшение:</b> {up_x}x ➡️ {up_x + 0.5}x
<b>💲 | Цена:</b> {cena_x} монет""", parse_mode="HTML", reply_markup=floor)
            await call.answer('Множитель ставки кубика улучшен!')
        else:
            await call.answer('Недостаточно средств!')
            
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()






@dp.callback_query_handler(text="smxbtn")
async def help_bt(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upsmxbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_x, up_x, cena_x FROM game_slot_machine WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_x = el[0]
            up_x = el[1]
            cena_x = el[2]
        if up_x >= 20:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
            await call.message.edit_text(f"""<b>♨️ | Множитель ставки рулетки</b>

<b>⬆️ | Уровень:</b> MAX
<b>♨️ | Множитель ставки рулетки:</b> {up_x}x""", parse_mode="HTML", reply_markup=floor)
        else:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
            await call.message.edit_text(f"""<b>♨️ | Множитель ставки рулетки</b>

<b>⬆️ | Уровень:</b> {lvl_x}
<b>♨️ | Множитель ставки рулетки:</b> {up_x}x

<b>🆙 | Улучшение:</b> {up_x}x ➡️ {up_x + 0.5}x
<b>💲 | Цена:</b> {cena_x} монет""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="upsmxbtn")
async def help_bt(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upsmxbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_x, up_x, cena_x FROM game_slot_machine WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_x = el[0]
            up_x = el[1]
            cena_x = el[2]
        c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uc = el[0]
        if uc >= cena_x:
            lvl_x += 1
            up_x += 0.5
            price_coins = uc - cena_x
            cena_x += 5000
            c.execute(f"UPDATE game_slot_machine SET lvl_x = {lvl_x}, up_x = {up_x}, cena_x = {cena_x} WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            if up_x >= 20:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
                await call.message.edit_text(f"""<b>♨️ | Множитель ставки рулетки</b>

<b>⬆️ | Уровень:</b> MAX
<b>♨️ | Множитель ставки рулетки:</b> {up_x}x""", parse_mode="HTML", reply_markup=floor)
            else:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
                await call.message.edit_text(f"""<b>♨️ | Множитель ставки рулетки</b>

<b>⬆️ | Уровень:</b> {lvl_x}
<b>♨️ | Множитель ставки рулетки:</b> {up_x}x

<b>🆙 | Улучшение:</b> {up_x}x ➡️ {up_x + 0.5}x
<b>💲 | Цена:</b> {cena_x} монет""", parse_mode="HTML", reply_markup=floor)
            await call.answer('Множитель ставки рулетки улучшен!')
        else:
            await call.answer('Недостаточно средств!')
            
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()





@dp.callback_query_handler(text="dxbtn")
async def help_bt(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='updxbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_x, up_x, cena_x FROM game_darts WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_x = el[0]
            up_x = el[1]
            cena_x = el[2]
        if up_x >= 10:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
            await call.message.edit_text(f"""<b>♨️ | Множитель ставки дартса</b>

<b>⬆️ | Уровень:</b> MAX
<b>♨️ | Множитель ставки дартса:</b> {up_x}x""", parse_mode="HTML", reply_markup=floor)
        else:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
            await call.message.edit_text(f"""<b>♨️ | Множитель ставки дартса</b>

<b>⬆️ | Уровень:</b> {lvl_x}
<b>♨️ | Множитель ставки дартса:</b> {up_x}x

<b>🆙 | Улучшение:</b> {up_x}x ➡️ {up_x + 0.5}x
<b>💲 | Цена:</b> {cena_x} монет""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="updxbtn")
async def help_bt(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='updxbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_x, up_x, cena_x FROM game_darts WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_x = el[0]
            up_x = el[1]
            cena_x = el[2]
        c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uc = el[0]
        if uc >= cena_x:
            lvl_x += 1
            up_x += 0.5
            price_coins = uc - cena_x
            cena_x += 5000
            c.execute(f"UPDATE game_darts SET lvl_x = {lvl_x}, up_x = {up_x}, cena_x = {cena_x} WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            if up_x >= 10:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
                await call.message.edit_text(f"""<b>♨️ | Множитель ставки дартса</b>

<b>⬆️ | Уровень:</b> MAX
<b>♨️ | Множитель ставки дартса:</b> {up_x}x""", parse_mode="HTML", reply_markup=floor)
            else:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
                await call.message.edit_text(f"""<b>♨️ | Множитель ставки дартса</b>

<b>⬆️ | Уровень:</b> {lvl_x}
<b>♨️ | Множитель ставки дартса:</b> {up_x}x

<b>🆙 | Улучшение:</b> {up_x}x ➡️ {up_x + 0.5}x
<b>💲 | Цена:</b> {cena_x} монет""", parse_mode="HTML", reply_markup=floor)
            await call.answer('Множитель ставки дартса улучшен!')
        else:
            await call.answer('Недостаточно средств!')
            
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()



@dp.callback_query_handler(text="bagbtn")
async def points_per_click(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upbagbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_bag, up_bag, cena_bag FROM game_stealing WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_bag = el[0]
            up_bag = el[1]
            cena_bag = el[2]
        if up_bag >= 10000:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
            await call.message.edit_text(f"""<b>💰 | Вместительность мешка</b>

<b>⬆️ | Уровень:</b> MAX
<b>💰 | Вместительность мешка:</b> {up_bag} монет""", parse_mode="HTML", reply_markup=floor)
        else:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
            await call.message.edit_text(f"""<b>💰 | Вместительность мешка</b>

<b>⬆️ | Уровень:</b> {lvl_bag}
<b>💰 | Вместительность мешка:</b> {up_bag} монет

<b>🆙 | Улучшение:</b> {up_bag} монет ➡️ {up_bag + 10} монет
<b>💲 | Цена:</b> {cena_bag} монет""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="upbagbtn")
async def up_points_per_click(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upbagbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_bag, up_bag, cena_bag FROM game_stealing WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_bag = el[0]
            up_bag = el[1]
            cena_bag = el[2]
        c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uc = el[0]
        if uc >= cena_bag:
            lvl_bag += 1
            up_bag += 10
            price_coins = uc - cena_bag
            cena_bag += 10000
            c.execute(f"UPDATE game_stealing SET lvl_bag = {lvl_bag}, up_bag = {up_bag}, cena_bag = {cena_bag} WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            if up_bag >= 10000:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
                await call.message.edit_text(f"""<b>💰 | Вместительность мешка</b>

<b>⬆️ | Уровень:</b> MAX
<b>💰 | Вместительность мешка:</b> {up_bag} монет""", parse_mode="HTML", reply_markup=floor)
            else:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
                await call.message.edit_text(f"""<b>💰 | Вместительность мешка</b>

<b>⬆️ | Уровень:</b> {lvl_bag}
<b>💰 | Вместительность мешка:</b> {up_bag} монет

<b>🆙 | Улучшение:</b> {up_bag} монет ➡️ {up_bag + 10} монет
<b>💲 | Цена:</b> {cena_bag} монет""", parse_mode="HTML", reply_markup=floor)
            await call.answer('Вместительность мешка улучшена!')
        else:
            await call.answer('Недостаточно средств!')
            
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()



@dp.callback_query_handler(text="stbtn")
async def points_per_click(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upstbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_st, up_st, cena_st FROM game_stealing WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_st = el[0]
            up_st = el[1]
            cena_st = el[2]
        if up_st >= 80:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
            await call.message.edit_text(f"""<b>🕶 | Скрытность</b>

<b>⬆️ | Уровень:</b> MAX
<b>🕶 | Скрытность:</b> {up_st}%""", parse_mode="HTML", reply_markup=floor)
        else:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
            await call.message.edit_text(f"""<b>🕶 | Скрытность</b>

<b>⬆️ | Уровень:</b> {lvl_st}
<b>🕶 | Скрытность:</b> {up_st}%

<b>🆙 | Улучшение:</b> {up_st}% ➡️ {up_st + 1}%
<b>💲 | Цена:</b> {cena_st} монет""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="upstbtn")
async def up_points_per_click(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upstbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_st, up_st, cena_st FROM game_stealing WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_st = el[0]
            up_st = el[1]
            cena_st = el[2]
        c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uc = el[0]
        if uc >= cena_st:
            lvl_st += 1
            up_st += 1
            price_coins = uc - cena_st
            cena_st += 10000
            c.execute(f"UPDATE game_stealing SET lvl_st = {lvl_st}, up_st = {up_st}, cena_st = {cena_st} WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            if up_st >= 80:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
                await call.message.edit_text(f"""<b>🕶 | Скрытность</b>

<b>⬆️ | Уровень:</b> MAX
<b>🕶 | Скрытность:</b> {up_st}%""", parse_mode="HTML", reply_markup=floor)
            else:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
                await call.message.edit_text(f"""<b>🕶 | Скрытность</b>

<b>⬆️ | Уровень:</b> {lvl_st}
<b>🕶 | Скрытность:</b> {up_st}%

<b>🆙 | Улучшение:</b> {up_st}% ➡️ {up_st + 1}%
<b>💲 | Цена:</b> {cena_st} монет""", parse_mode="HTML", reply_markup=floor)
            await call.answer('Скрытность улучшена!')
        else:
            await call.answer('Недостаточно средств!')
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()



@dp.callback_query_handler(text="sbtn")
async def points_per_click(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upsbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_s, up_s, cena_s FROM game_stealing WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_s = el[0]
            up_s = el[1]
            cena_s = el[2]
        if up_s >= 80:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
            await call.message.edit_text(f"""<b>🕵️ | Безопасность</b>

<b>⬆️ | Уровень:</b> MAX
<b>🕵️ | Безопасность:</b> {up_s}%""", parse_mode="HTML", reply_markup=floor)
        else:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
            await call.message.edit_text(f"""<b>🕵️ | Безопасность</b>

<b>⬆️ | Уровень:</b> {lvl_s}
<b>🕵️ | Безопасность:</b> {up_s}%

<b>🆙 | Улучшение:</b> {up_s}% ➡️ {up_s + 1}%
<b>💲 | Цена:</b> {cena_s} монет""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="upsbtn")
async def up_points_per_click(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upsbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_s, up_s, cena_s FROM game_stealing WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_s = el[0]
            up_s = el[1]
            cena_s = el[2]
        c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uc = el[0]
        if uc >= cena_s:
            lvl_s += 1
            up_s += 1
            price_coins = uc - cena_s
            cena_s += 1000
            c.execute(f"UPDATE game_stealing SET lvl_s = {lvl_s}, up_s = {up_s}, cena_s = {cena_s} WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            if up_s >= 80:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
                await call.message.edit_text(f"""<b>🕵️ | Безопасность</b>

<b>⬆️ | Уровень:</b> MAX
<b>🕵️ | Безопасность:</b> {up_s}%""", parse_mode="HTML", reply_markup=floor)
            else:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
                await call.message.edit_text(f"""<b>🕵️ | Безопасность</b>

<b>⬆️ | Уровень:</b> {lvl_s}
<b>🕵️ | Безопасность:</b> {up_s}%

<b>🆙 | Улучшение:</b> {up_s}% ➡️ {up_s + 1}%
<b>💲 | Цена:</b> {cena_s} монет""", parse_mode="HTML", reply_markup=floor)
            await call.answer('Безопасность улучшена!')
        else:
            await call.answer('Недостаточно средств!')
            
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()





@dp.callback_query_handler(text="kvbtn")
async def double_points(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upkvbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_kv, up_kv, cena_kv FROM game_case WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_kv = el[0]
            up_kv = el[1]
            cena_kv = el[2]
        if lvl_kv >= 50:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
            await call.message.edit_text(f"""<b>💯 | Шанс нахождения ключа</b>

<b>⬆️ | Уровень:</b> MAX
<b>💯 | Шанс нахождения ключа:</b> {up_kv}%""", parse_mode="HTML", reply_markup=floor)
        else:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
            await call.message.edit_text(f"""<b>💯 | Шанс нахождения ключа</b>

<b>⬆️ | Уровень:</b> {lvl_kv}
<b>💯 | Шанс нахождения ключа:</b> {up_kv}%

<b>🆙 | Улучшение:</b> {up_kv}% ➡️ {up_kv + 0.5}%
<b>💲 | Цена:</b> {cena_kv} монет""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="upkvbtn")
async def up_double_points(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upkvbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_kv, up_kv, cena_kv FROM game_case WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_kv = el[0]
            up_kv = el[1]
            cena_kv = el[2]
        c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uc = el[0]
        if uc >= cena_kv:
            lvl_kv += 1
            up_kv += 0.5
            price_coins = uc - cena_kv
            cena_kv += 100000
            c.execute(f"UPDATE game_case SET lvl_kv = {lvl_kv}, up_kv = {up_kv}, cena_kv = {cena_kv} WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            if lvl_kv >= 50:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
                await call.message.edit_text(f"""<b>💯 | Шанс нахождения ключа</b>

<b>⬆️ | Уровень:</b> MAX
<b>💯 | Шанс нахождения ключа:</b> {up_kv}%""", parse_mode="HTML", reply_markup=floor)
            else:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
                await call.message.edit_text(f"""<b>💯 | Шанс нахождения ключа</b>

<b>⬆️ | Уровень:</b> {lvl_kv}
<b>💯 | Шанс нахождения ключа:</b> {up_kv}%

<b>🆙 | Улучшение:</b> {up_kv}% ➡️ {up_kv + 0.5}%
<b>💲 | Цена:</b> {cena_kv} монет""", parse_mode="HTML", reply_markup=floor)
            await call.answer('Шанс нахождения ключа улучшен!')
        else:
            await call.answer('Недостаточно средств!')
            
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()





@dp.callback_query_handler(text="prbtn")
async def double_points(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upprbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_pr, up_pr, cena_pr FROM game_case WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_pr = el[0]
            up_pr = el[1]
            cena_pr = el[2]
        if up_pr >= 100:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
            await call.message.edit_text(f"""<b>💰 | Дроп из кейса</b>

<b>⬆️ | Уровень:</b> MAX
<b>💰 | Дроп из кейса:</b> {up_pr}%""", parse_mode="HTML", reply_markup=floor)
        else:
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
            await call.message.edit_text(f"""<b>💰 | Дроп из кейса</b>

<b>⬆️ | Уровень:</b> {lvl_pr}
<b>💰 | Дроп из кейса:</b> {up_pr} монет

<b>🆙 | Улучшение:</b> {up_pr} монет ➡️ {up_pr + 10} монет
<b>💲 | Цена:</b> {cena_pr} монет""", parse_mode="HTML", reply_markup=floor)
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.callback_query_handler(text="upprbtn")
async def up_double_points(call: types.CallbackQuery):
    back = InlineKeyboardButton("⬅️ Назад", callback_data='backtoupsbtn')
    up = InlineKeyboardButton("🆙 Улучшить", callback_data='upprbtn')
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT lvl_pr, up_pr, cena_pr FROM game_case WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            lvl_pr = el[0]
            up_pr = el[1]
            cena_pr = el[2]
        c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            uc = el[0]
        if uc >= cena_pr:
            lvl_pr += 1
            up_pr += 10
            price_coins = uc - cena_pr
            cena_pr += 10000
            c.execute(f"UPDATE game_case SET lvl_pr = {lvl_pr}, up_pr = {up_pr}, cena_pr = {cena_pr} WHERE user_id = {call.from_user.id}")
            c.execute(f"UPDATE user_data SET user_coins = {price_coins} WHERE user_id = {call.from_user.id}")
            if lvl_pr >= 100:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back)
                await call.message.edit_text(f"""<b>💰 | Дроп из кейса</b>

<b>⬆️ | Уровень:</b> MAX
<b>💰 | Дроп из кейса:</b> {up_pr}%""", parse_mode="HTML", reply_markup=floor)
            else:
                floor = InlineKeyboardMarkup(resize_keyboard=True).add(back).add(up)
                await call.message.edit_text(f"""<b>💰 | Дроп из кейса</b>

<b>⬆️ | Уровень:</b> {lvl_pr}
<b>💰 | Дроп из кейса:</b> {up_pr} монет

<b>🆙 | Улучшение:</b> {up_pr} монет ➡️ {up_pr + 10} монет
<b>💲 | Цена:</b> {cena_pr} монет""", parse_mode="HTML", reply_markup=floor)
            await call.answer('Дроп из улучшен!')
        else:
            await call.answer('Недостаточно средств!')
            
    except:
        await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()