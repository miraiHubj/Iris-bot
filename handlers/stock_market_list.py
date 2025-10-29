from aiogram import types
from dispatcher import bot, dp
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher.filters import Text
import sqlite3

@dp.message_handler(text=['Биржа', 'Рынок', 'Чап-биржа', 'Чап-рынок',  'биржа', 'рынок', 'чап-биржа', 'чап-рынок'])
async def process_auction_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT cena FROM stock_market_zakaz ORDER BY cena ASC")
    items = c.fetchall()
    for el in items:
        zakaz = el[0]
    c.execute(f"SELECT user_id, chapchas, cena FROM stock_market ORDER BY cena ASC")
    items = c.fetchall()
    auci = []
    for el in items:
        auci.append(el[0])
        auci.append(el[1])
        auci.append(el[2])
    msg = ''
    num = 0
    fil1 = InlineKeyboardButton('📉 Сначала дешево', callback_data='fil1:page:1')
    fil2 = InlineKeyboardButton('📈 Сначала дорого', callback_data='fil2:page:1')
    fil3 = InlineKeyboardButton('⬆️ Больше чапчей', callback_data='fil3:page:1')
    fil4 = InlineKeyboardButton('⬇️ Меньше чапчей', callback_data='fil4:page:1')
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).row(fil1, fil2).row(fil3, fil4)
    allitems = 0
    btnrk = False
    for el in auci:
        if allitems == 20:
            btn2 = InlineKeyboardButton('▶️ Вперед', callback_data='smpage:2')
            floor.add(btn2)
            btnrk = True
            break
        if num == 0:
            msg += "<code>" + str(el) + "</code>. "
        elif num == 1:
            msg += str(el) + " чапчей  | "
        else:
            msg += str(el) + " фрибасов\n"
            num = -1
            allitems += 1
        num += 1
    try:
        if allitems == 0:
            await message.answer(f"""<b>Биржа</b>
Запросы на покупку: {zakaz} фрибасов

Список пуст

Стр. 1""", parse_mode="HTML")
        else:
            if btnrk == False:
                await message.answer(f"""<b>Биржа</b>
Запросы на покупку: {zakaz} фрибасов

{msg}
Стр. 1""", parse_mode="HTML", reply_markup=floor)
            else:
                await message.answer(f"""<b>Биржа</b>
Запросы на покупку: {zakaz} фрибасов

{msg}
Стр. 1""", parse_mode="HTML", reply_markup=floor)
    except:
        
        if allitems == 0:
            await message.answer(f"""<b>Биржа</b>

Список пуст

Стр. 1""", parse_mode="HTML")
        else:
            if btnrk == False:
                await message.answer(f"""<b>Биржа</b>

{msg}
Стр. 1""", parse_mode="HTML", reply_markup=floor)
            else:
                await message.answer(f"""<b>Биржа</b>

{msg}
Стр. 1""", parse_mode="HTML", reply_markup=floor)



@dp.callback_query_handler(Text(startswith=['smpage']))
async def process_auction_command(call: types.CallbackQuery):
    pagenum = int(call.data.split(':')[1])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT cena FROM stock_market_zakaz ORDER BY cena ASC")
    items = c.fetchall()
    for el in items:
        zakaz = el[0]
    c.execute(f"SELECT user_id, chapchas, cena FROM stock_market ORDER BY cena ASC")
    items = c.fetchall()
    auci = []
    for el in items:
        auci.append(el[0])
        auci.append(el[1])
        auci.append(el[2])
    msg = ''
    num = 0
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    if pagenum == 1:
        fil1 = InlineKeyboardButton('📉 Сначала дешево', callback_data='fil1')
        fil2 = InlineKeyboardButton('📈 Сначала дорого', callback_data='fil2')
        fil3 = InlineKeyboardButton('⬆️ Больше чапчей', callback_data='fil3')
        fil4 = InlineKeyboardButton('⬇️ Меньше чапчей', callback_data='fil4')
        floor.row(fil1, fil2).row(fil3, fil4)
    allitems = 0
    btnrk = False
    numm = 0
    for el in auci:
        if numm < 60*(pagenum-1):
            numm += 1
        else:
            if allitems == 20:
                btnrk = True
                break
            if num == 0:
                msg += "<code>" + str(el) + "</code>. "
            elif num == 1:
                msg += str(el) + " чапчей  | "
            else:
                msg += str(el) + " фрибасов\n"
                num = -1
                allitems += 1
            num += 1
    back = InlineKeyboardButton('◀️ Назад', callback_data=f'smpage:{pagenum-1}')
    btnn = InlineKeyboardButton('▶️ Вперед', callback_data=f'smpage:{pagenum+1}')
    if btnrk:
        if pagenum == 1:
            floor.add(btnn)
        else:
            floor.row(back, btnn)
    else:
        if pagenum != 1:
            floor.add(back)
    try:
        if btnrk:
            await call.message.edit_text(f"""<b>Биржа</b>
Запросы на покупку: {zakaz} фрибасов

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)
        else:
            await call.message.edit_text(f"""<b>Биржа</b>
Запросы на покупку: {zakaz} фрибасов

{msg}
Стр. {pagenum}""", parse_mode="HTML")
    except:
        await call.message.edit_text(f"""<b>Биржа</b>

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)






@dp.callback_query_handler(Text(startswith=['fil1:page']))
async def process_auction_command(call: types.CallbackQuery):
    pagenum = int(call.data.split(':')[2])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT cena FROM stock_market_zakaz ORDER BY cena ASC")
    items = c.fetchall()
    for el in items:
        zakaz = el[0]
    c.execute(f"SELECT user_id, chapchas, cena FROM stock_market ORDER BY cena ASC")
    items = c.fetchall()
    auci = []
    for el in items:
        auci.append(el[0])
        auci.append(el[1])
        auci.append(el[2])
    msg = ''
    num = 0
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    if pagenum == 1:
        fil1 = InlineKeyboardButton('📉 Сначала дешево', callback_data='fil1:page:1')
        fil2 = InlineKeyboardButton('📈 Сначала дорого', callback_data='fil2:page:1')
        fil3 = InlineKeyboardButton('⬆️ Больше чапчей', callback_data='fil3:page:1')
        fil4 = InlineKeyboardButton('⬇️ Меньше чапчей', callback_data='fil4:page:1')
        floor.row(fil1, fil2).row(fil3, fil4)
    allitems = 0
    btnrk = False
    numm = 0
    for el in auci:
        if numm < 60*(pagenum-1):
            numm += 1
        else:
            if allitems == 20:
                btnrk = True
                break
            if num == 0:
                msg += "<code>" + str(el) + "</code>. "
            elif num == 1:
                msg += str(el) + " чапчей  | "
            else:
                msg += str(el) + " фрибасов\n"
                num = -1
                allitems += 1
            num += 1
    back = InlineKeyboardButton('◀️ Назад', callback_data=f'fil1:page:{pagenum-1}')
    btnn = InlineKeyboardButton('▶️ Вперед', callback_data=f'fil1:page:{pagenum+1}')
    if btnrk:
        if pagenum == 1:
            floor.add(btnn)
        else:
            floor.row(back, btnn)
    else:
        if pagenum != 1:
            floor.add(back)
    try:
        if btnrk:
            await call.message.edit_text(f"""<b>Биржа: Сначала дешево</b>
Запросы на покупку: {zakaz} фрибасов

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)
        else:
            await call.message.edit_text(f"""<b>Биржа: Сначала дешево</b>
Запросы на покупку: {zakaz} фрибасов

{msg}
Стр. {pagenum}""", parse_mode="HTML")
    except:
        await call.message.edit_text(f"""<b>Биржа: Сначала дешево</b>

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)






@dp.callback_query_handler(Text(startswith=['fil2:page']))
async def process_auction_command(call: types.CallbackQuery):
    pagenum = int(call.data.split(':')[2])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT cena FROM stock_market_zakaz ORDER BY cena ASC")
    items = c.fetchall()
    for el in items:
        zakaz = el[0]
    c.execute(f"SELECT user_id, chapchas, cena FROM stock_market ORDER BY cena DESC")
    items = c.fetchall()
    auci = []
    for el in items:
        auci.append(el[0])
        auci.append(el[1])
        auci.append(el[2])
    msg = ''
    num = 0
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    if pagenum == 1:
        fil1 = InlineKeyboardButton('📉 Сначала дешево', callback_data='fil1:page:1')
        fil2 = InlineKeyboardButton('📈 Сначала дорого', callback_data='fil2:page:1')
        fil3 = InlineKeyboardButton('⬆️ Больше чапчей', callback_data='fil3:page:1')
        fil4 = InlineKeyboardButton('⬇️ Меньше чапчей', callback_data='fil4:page:1')
        floor.row(fil1, fil2).row(fil3, fil4)
    allitems = 0
    btnrk = False
    numm = 0
    for el in auci:
        if numm < 60*(pagenum-1):
            numm += 1
        else:
            if allitems == 20:
                btnrk = True
                break
            if num == 0:
                msg += "<code>" + str(el) + "</code>. "
            elif num == 1:
                msg += str(el) + " чапчей  | "
            else:
                msg += str(el) + " фрибасов\n"
                num = -1
                allitems += 1
            num += 1
    back = InlineKeyboardButton('◀️ Назад', callback_data=f'fil2:page:{pagenum-1}')
    btnn = InlineKeyboardButton('▶️ Вперед', callback_data=f'fil2:page:{pagenum+1}')
    if btnrk:
        if pagenum == 1:
            floor.add(btnn)
        else:
            floor.row(back, btnn)
    else:
        if pagenum != 1:
            floor.add(back)
    try:
        if btnrk:
            await call.message.edit_text(f"""<b>Биржа: Сначала дорого</b>
Запросы на покупку: {zakaz} фрибасов

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)
        else:
            await call.message.edit_text(f"""<b>Биржа: Сначала дорого</b>
Запросы на покупку: {zakaz} фрибасов

{msg}
Стр. {pagenum}""", parse_mode="HTML")
    except:
        await call.message.edit_text(f"""<b>Биржа: Сначала дорого</b>

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)






@dp.callback_query_handler(Text(startswith=['fil3:page']))
async def process_auction_command(call: types.CallbackQuery):
    pagenum = int(call.data.split(':')[2])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT cena FROM stock_market_zakaz ORDER BY cena ASC")
    items = c.fetchall()
    for el in items:
        zakaz = el[0]
    c.execute(f"SELECT user_id, chapchas, cena FROM stock_market ORDER BY chapchas DESC")
    items = c.fetchall()
    auci = []
    for el in items:
        auci.append(el[0])
        auci.append(el[1])
        auci.append(el[2])
    msg = ''
    num = 0
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    if pagenum == 1:
        fil1 = InlineKeyboardButton('📉 Сначала дешево', callback_data='fil1:page:1')
        fil2 = InlineKeyboardButton('📈 Сначала дорого', callback_data='fil2:page:1')
        fil3 = InlineKeyboardButton('⬆️ Больше чапчей', callback_data='fil3:page:1')
        fil4 = InlineKeyboardButton('⬇️ Меньше чапчей', callback_data='fil4:page:1')
        floor.row(fil1, fil2).row(fil3, fil4)
    allitems = 0
    btnrk = False
    numm = 0
    for el in auci:
        if numm < 60*(pagenum-1):
            numm += 1
        else:
            if allitems == 20:
                btnrk = True
                break
            if num == 0:
                msg += "<code>" + str(el) + "</code>. "
            elif num == 1:
                msg += str(el) + " чапчей  | "
            else:
                msg += str(el) + " фрибасов\n"
                num = -1
                allitems += 1
            num += 1
    back = InlineKeyboardButton('◀️ Назад', callback_data=f'fil3:page:{pagenum-1}')
    btnn = InlineKeyboardButton('▶️ Вперед', callback_data=f'fil3:page:{pagenum+1}')
    if btnrk:
        if pagenum == 1:
            floor.add(btnn)
        else:
            floor.row(back, btnn)
    else:
        if pagenum != 1:
            floor.add(back)
    try:
        if btnrk:
            await call.message.edit_text(f"""<b>Биржа: Больше чапчей</b>
Запросы на покупку: {zakaz} фрибасов

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)
        else:
            await call.message.edit_text(f"""<b>Биржа: Больше чапчей</b>
Запросы на покупку: {zakaz} фрибасов

{msg}
Стр. {pagenum}""", parse_mode="HTML")
    except:
        await call.message.edit_text(f"""<b>Биржа: Больше чапчей</b>

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)






@dp.callback_query_handler(Text(startswith=['fil4:page']))
async def process_auction_command(call: types.CallbackQuery):
    pagenum = int(call.data.split(':')[2])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute("SELECT cena FROM stock_market_zakaz ORDER BY cena ASC")
    items = c.fetchall()
    for el in items:
        zakaz = el[0]
    c.execute(f"SELECT user_id, chapchas, cena FROM stock_market ORDER BY chapchas ASC")
    items = c.fetchall()
    auci = []
    for el in items:
        auci.append(el[0])
        auci.append(el[1])
        auci.append(el[2])
    msg = ''
    num = 0
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    if pagenum == 1:
        fil1 = InlineKeyboardButton('📉 Сначала дешево', callback_data='fil1:page:1')
        fil2 = InlineKeyboardButton('📈 Сначала дорого', callback_data='fil2:page:1')
        fil3 = InlineKeyboardButton('⬆️ Больше чапчей', callback_data='fil3:page:1')
        fil4 = InlineKeyboardButton('⬇️ Меньше чапчей', callback_data='fil4:page:1')
        floor.row(fil1, fil2).row(fil3, fil4)
    allitems = 0
    btnrk = False
    numm = 0
    for el in auci:
        if numm < 60*(pagenum-1):
            numm += 1
        else:
            if allitems == 20:
                btnrk = True
                break
            if num == 0:
                msg += "<code>" + str(el) + "</code>. "
            elif num == 1:
                msg += str(el) + " чапчей  | "
            else:
                msg += str(el) + " фрибасов\n"
                num = -1
                allitems += 1
            num += 1
    back = InlineKeyboardButton('◀️ Назад', callback_data=f'fil4:page:{pagenum-1}')
    btnn = InlineKeyboardButton('▶️ Вперед', callback_data=f'fil4:page:{pagenum+1}')
    if btnrk:
        if pagenum == 1:
            floor.add(btnn)
        else:
            floor.row(back, btnn)
    else:
        if pagenum != 1:
            floor.add(back)
    try:
        if btnrk:
            await call.message.edit_text(f"""<b>Биржа: Меньше чапчей</b>
Запросы на покупку: {zakaz} фрибасов

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)
        else:
            await call.message.edit_text(f"""<b>Биржа: Меньше чапчей</b>
Запросы на покупку: {zakaz} фрибасов

{msg}
Стр. {pagenum}""", parse_mode="HTML")
    except:
        await call.message.edit_text(f"""<b>Биржа: Меньше чапчей</b>

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)