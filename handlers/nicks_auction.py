from aiogram import types
from dispatcher import bot, dp
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher.filters import Text
import sqlite3
import datetime

@dp.message_handler(commands=['auction', 'auc'])
async def process_auction_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT item, cena FROM nicks_auction ORDER BY item_time DESC")
    items = c.fetchall()
    iauci = []
    for el in items:
        iauci.append(el[0])
        iauci.append(el[1])
    auci = []
    for el in iauci:
        if el == None or el == '':
            pass
        else:
            auci.append(el)
    msg = ''
    num = 0
    fil1 = InlineKeyboardButton('📉 Сначала дешево', callback_data='nafil1:page:1')
    fil2 = InlineKeyboardButton('📈 Сначала дорого', callback_data='nafil2:page:1')
    fil3 = InlineKeyboardButton('⏳ Сначаа новое', callback_data='nafil3:page:1')
    fil4 = InlineKeyboardButton('⌛️ Сначала старое', callback_data='nafil4:page:1')
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).row(fil1, fil2).row(fil3, fil4)
    allitems = 0
    for el in auci:
        if allitems == 20:
            btn2 = InlineKeyboardButton('▶️ Вперед', callback_data='napage:2')
            floor.add(btn2)
            btnrk = True
            break
        if num == 0:
            msg += str(allitems+1) + ". <code>" + str(el) + "</code> | "
        else:
            msg += str(el) + " эклеров\n"
            num = -1
            allitems += 1
        num += 1
    if len(auci) == 0:
        await message.answer(f"""<b>Аукцион ников:</b>

Список пуст""", parse_mode="HTML")
        
    else:
        await message.answer(f"""<b>Аукцион ников:</b>

{msg}
Стр. 1""", parse_mode="HTML", reply_markup=floor)
    db.commit()
    db.close()









@dp.callback_query_handler(Text(startswith=['napage']))
async def process_auction_command(call: types.CallbackQuery):
    pagenum = int(call.data.split(':')[1])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT item, cena FROM nicks_auction ORDER BY item_time DESC")
    items = c.fetchall()
    iauci = []
    for el in items:
        iauci.append(el[0])
        iauci.append(el[1])
    auci = []
    for el in iauci:
        if el == None or el == '':
            pass
        else:
            auci.append(el)
    msg = ''
    num = 0
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    if pagenum == 1:
        fil1 = InlineKeyboardButton('📉 Сначала дешево', callback_data='nafil1:page:1')
        fil2 = InlineKeyboardButton('📈 Сначала дорого', callback_data='nafil2:page:1')
        fil3 = InlineKeyboardButton('⏳ Сначаа новое', callback_data='nafil3:page:1')
        fil4 = InlineKeyboardButton('⌛️ Сначала старое', callback_data='nafil4:page:1')
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
                msg += str(allitems+1) + ". <code>" + str(el) + "</code> | "
            else:
                msg += str(el) + " эклеров\n"
                num = -1
                allitems += 1
            num += 1
    back = InlineKeyboardButton('◀️ Назад', callback_data=f'napage:{pagenum-1}')
    btnn = InlineKeyboardButton('▶️ Вперед', callback_data=f'napage:{pagenum+1}')
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
            await call.message.edit_text(f"""<b>Аукцион ников</b>

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)
        else:
            await call.message.edit_text(f"""<b>Аукцион ников</b>

{msg}
Стр. {pagenum}""", parse_mode="HTML")
    except:
        await call.message.edit_text(f"""<b>Аукцион ников</b>

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)






@dp.callback_query_handler(Text(startswith=['nafil1:page']))
async def process_auction_command(call: types.CallbackQuery):
    pagenum = int(call.data.split(':')[2])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT item, cena FROM nicks_auction ORDER BY cena ASC")
    items = c.fetchall()
    iauci = []
    for el in items:
        iauci.append(el[0])
        iauci.append(el[1])
    auci = []
    for el in iauci:
        if el == None or el == '':
            pass
        else:
            auci.append(el)
    msg = ''
    num = 0
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    if pagenum == 1:
        fil1 = InlineKeyboardButton('📉 Сначала дешево', callback_data='nafil1:page:1')
        fil2 = InlineKeyboardButton('📈 Сначала дорого', callback_data='nafil2:page:1')
        fil3 = InlineKeyboardButton('⏳ Сначаа новое', callback_data='nafil3:page:1')
        fil4 = InlineKeyboardButton('⌛️ Сначала старое', callback_data='nafil4:page:1')
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
                msg += str(allitems+1) + ". <code>" + str(el) + "</code> | "
            else:
                msg += str(el) + " эклеров\n"
                num = -1
                allitems += 1
            num += 1
    back = InlineKeyboardButton('◀️ Назад', callback_data=f'nafil1:page:{pagenum-1}')
    btnn = InlineKeyboardButton('▶️ Вперед', callback_data=f'nafil1:page:{pagenum+1}')
    if btnrk:
        if pagenum == 1:
            floor.add(btnn)
        else:
            floor.row(back, btnn)
    else:
        if pagenum != 1:
            floor.add(back)
    try:
        await call.message.edit_text(f"""<b>Аукцион ников: Сначала дешево</b>

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)
    except:
        pass






@dp.callback_query_handler(Text(startswith=['nafil2:page']))
async def process_auction_command(call: types.CallbackQuery):
    pagenum = int(call.data.split(':')[2])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT item, cena FROM nicks_auction ORDER BY cena DESC")
    items = c.fetchall()
    iauci = []
    for el in items:
        iauci.append(el[0])
        iauci.append(el[1])
    auci = []
    for el in iauci:
        if el == None or el == '':
            pass
        else:
            auci.append(el)
    msg = ''
    num = 0
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    if pagenum == 1:
        fil1 = InlineKeyboardButton('📉 Сначала дешево', callback_data='nafil1:page:1')
        fil2 = InlineKeyboardButton('📈 Сначала дорого', callback_data='nafil2:page:1')
        fil3 = InlineKeyboardButton('⏳ Сначаа новое', callback_data='nafil3:page:1')
        fil4 = InlineKeyboardButton('⌛️ Сначала старое', callback_data='nafil4:page:1')
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
                msg += str(allitems+1) + ". <code>" + str(el) + "</code> | "
            else:
                msg += str(el) + " эклеров\n"
                num = -1
                allitems += 1
            num += 1
    back = InlineKeyboardButton('◀️ Назад', callback_data=f'nafil2:page:{pagenum-1}')
    btnn = InlineKeyboardButton('▶️ Вперед', callback_data=f'nafil2:page:{pagenum+1}')
    if btnrk:
        if pagenum == 1:
            floor.add(btnn)
        else:
            floor.row(back, btnn)
    else:
        if pagenum != 1:
            floor.add(back)
    try:
        await call.message.edit_text(f"""<b>Аукцион ников: Сначала дорого</b>

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)
    except:
        pass






@dp.callback_query_handler(Text(startswith=['nafil3:page']))
async def process_auction_command(call: types.CallbackQuery):
    pagenum = int(call.data.split(':')[2])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT item, cena FROM nicks_auction ORDER BY item_time ASC")
    items = c.fetchall()
    iauci = []
    for el in items:
        iauci.append(el[0])
        iauci.append(el[1])
    auci = []
    for el in iauci:
        if el == None or el == '':
            pass
        else:
            auci.append(el)
    msg = ''
    num = 0
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    if pagenum == 1:
        fil1 = InlineKeyboardButton('📉 Сначала дешево', callback_data='nafil1:page:1')
        fil2 = InlineKeyboardButton('📈 Сначала дорого', callback_data='nafil2:page:1')
        fil3 = InlineKeyboardButton('⏳ Сначаа новое', callback_data='nafil3:page:1')
        fil4 = InlineKeyboardButton('⌛️ Сначала старое', callback_data='nafil4:page:1')
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
                msg += str(allitems+1) + ". <code>" + str(el) + "</code> | "
            else:
                msg += str(el) + " эклеров\n"
                num = -1
                allitems += 1
            num += 1
    back = InlineKeyboardButton('◀️ Назад', callback_data=f'nafil3:page:{pagenum-1}')
    btnn = InlineKeyboardButton('▶️ Вперед', callback_data=f'nafil3:page:{pagenum+1}')
    if btnrk:
        if pagenum == 1:
            floor.add(btnn)
        else:
            floor.row(back, btnn)
    else:
        if pagenum != 1:
            floor.add(back)
    try:
        await call.message.edit_text(f"""<b>Аукцион ников: Сначала новое</b>

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)
    except:
        pass






@dp.callback_query_handler(Text(startswith=['nafil4:page']))
async def process_auction_command(call: types.CallbackQuery):
    pagenum = int(call.data.split(':')[2])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT item, cena FROM nicks_auction ORDER BY item_time DESC")
    items = c.fetchall()
    iauci = []
    for el in items:
        iauci.append(el[0])
        iauci.append(el[1])
    auci = []
    for el in iauci:
        if el == None or el == '':
            pass
        else:
            auci.append(el)
    msg = ''
    num = 0
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    if pagenum == 1:
        fil1 = InlineKeyboardButton('📉 Сначала дешево', callback_data='nafil1:page:1')
        fil2 = InlineKeyboardButton('📈 Сначала дорого', callback_data='nafil2:page:1')
        fil3 = InlineKeyboardButton('⏳ Сначаа новое', callback_data='nafil3:page:1')
        fil4 = InlineKeyboardButton('⌛️ Сначала старое', callback_data='nafil4:page:1')
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
                msg += str(allitems+1) + ". <code>" + str(el) + "</code> | "
            else:
                msg += str(el) + " эклеров\n"
                num = -1
                allitems += 1
            num += 1
    back = InlineKeyboardButton('◀️ Назад', callback_data=f'nafil4:page:{pagenum-1}')
    btnn = InlineKeyboardButton('▶️ Вперед', callback_data=f'nafil4:page:{pagenum+1}')
    if btnrk:
        if pagenum == 1:
            floor.add(btnn)
        else:
            floor.row(back, btnn)
    else:
        if pagenum != 1:
            floor.add(back)
    try:
        await call.message.edit_text(f"""<b>Аукцион ников: Сначала старое</b>

{msg}
Стр. {pagenum}""", parse_mode="HTML", reply_markup=floor)
    except:
        pass










#qssellnick
@dp.message_handler(commands=['sellnick'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT nick_1, nick_2, nick_3, nick_4, nick_5 FROM nicks_auction WHERE user_id = {message.from_user.id}")
    unl = c.fetchall()
    un = []
    for el in unl:
        un.append(el[0])
        un.append(el[1])
        un.append(el[2])
        un.append(el[3])
        un.append(el[4])
    uns = []
    for el in un:
        if el == '' or el == None:
            pass
        else:
            uns.append(el)
    c.execute(f"SELECT item FROM nicks_auction")
    items = c.fetchall()
    anoal = []
    for n in items:
        anoal.append(n[0])
    anoa = []
    for n in anoal:
        if n == '' or n == None:
            pass
        else:
            anoa.append(n)
    c.execute(f"SELECT item, nick_1, nick_2, nick_3, nick_4, nick_5 FROM nicks_auction WHERE user_id <> {message.from_user.id}")
    anll = c.fetchall()
    anl = []
    for n in anll:
        anl.append(n[0])
        anl.append(n[1])
        anl.append(n[2])
        anl.append(n[3])
        anl.append(n[4])
        anl.append(n[5])
    an = []
    for n in anl:
        if n == '' or n == None:
            pass
        else:
            an.append(n)
    try:
        cm = message.text.split(' ')[1]
        cena = int(message.text.split(' ')[-1])
        lll = len(str(cena)) + 1
        nick = message.text[10:-lll]
        while nick.find(' ') == 0:
            nick = nick[2:]
        while nick.find(' ') == len(nick) - 1:
            nick = nick[:-1]
        while nick.find('ㅤ') == 0:
            nick = nick[1:]
        while nick.find('ㅤ') == len(nick) - 1:
            nick = nick[:-1]
        while nick.find('у') != -1:
            nick1 = nick[:nick.find('у')]
            nick2 = nick[nick.find('у')+1:]
            nick = nick1 + 'y' + nick2
        while nick.find('е') != -1:
            nick1 = nick[:nick.find('е')]
            nick2 = nick[nick.find('е')+1:]
            nick = nick1 + 'e' + nick2
        while nick.find('х') != -1:
            nick1 = nick[:nick.find('х')]
            nick2 = nick[nick.find('х')+1:]
            nick = nick1 + 'x' + nick2
        while nick.find('а') != -1:
            nick1 = nick[:nick.find('а')]
            nick2 = nick[nick.find('а')+1:]
            nick = nick1 + 'a' + nick2
        while nick.find('р') != -1:
            nick1 = nick[:nick.find('р')]
            nick2 = nick[nick.find('р')+1:]
            nick = nick1 + 'p' + nick2
        while nick.find('о') != -1:
            nick1 = nick[:nick.find('о')]
            nick2 = nick[nick.find('о')+1:]
            nick = nick1 + 'o' + nick2
        while nick.find('с') != -1:
            nick1 = nick[:nick.find('с')]
            nick2 = nick[nick.find('с')+1:]
            nick = nick1 + 'c' + nick2
        while nick.find('К') != -1:
            nick1 = nick[:nick.find('К')]
            nick2 = nick[nick.find('К')+1:]
            nick = nick1 + 'K' + nick2
        while nick.find('Е') != -1:
            nick1 = nick[:nick.find('Е')]
            nick2 = nick[nick.find('Е')+1:]
            nick = nick1 + 'E' + nick2
        while nick.find('Н') != -1:
            nick1 = nick[:nick.find('Н')]
            nick2 = nick[nick.find('Н')+1:]
            nick = nick1 + 'H' + nick2
        while nick.find('Х') != -1:
            nick1 = nick[:nick.find('Х')]
            nick2 = nick[nick.find('Х')+1:]
            nick = nick1 + 'X' + nick2
        while nick.find('В') != -1:
            nick1 = nick[:nick.find('В')]
            nick2 = nick[nick.find('В')+1:]
            nick = nick1 + 'B' + nick2
        while nick.find('А') != -1:
            nick1 = nick[:nick.find('А')]
            nick2 = nick[nick.find('А')+1:]
            nick = nick1 + 'A' + nick2
        while nick.find('Р') != -1:
            nick1 = nick[:nick.find('Р')]
            nick2 = nick[nick.find('Р')+1:]
            nick = nick1 + 'P' + nick2
        while nick.find('О') != -1:
            nick1 = nick[:nick.find('О')]
            nick2 = nick[nick.find('О')+1:]
            nick = nick1 + 'O' + nick2
        while nick.find('С') != -1:
            nick1 = nick[:nick.find('С')]
            nick2 = nick[nick.find('С')+1:]
            nick = nick1 + 'C' + nick2
        while nick.find('М') != -1:
            nick1 = nick[:nick.find('М')]
            nick2 = nick[nick.find('М')+1:]
            nick = nick1 + 'M' + nick2
        while nick.find('Т') != -1:
            nick1 = nick[:nick.find('Т')]
            nick2 = nick[nick.find('Т')+1:]
            nick = nick1 + 'T' + nick2
        if nick == '':
            await message.answer("/sellnick Ник Число")
        else:
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
            date_pre = datetime.datetime.now()
            date_time = date_pre.strftime("%d.%m.%y %H:%M")
            ni = False
            rn = 0
            c.execute(f"SELECT user_nick FROM nicks_auction WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                unib = el[0]
            for n in uns:
                if n == nick:
                    rn += 1
                    break
            if len(uns) == 5:
                await message.answer("Нельзя выставить ник на продажу, мешок ников заполнен!")
            else:
                for n in an:
                    if n == nick:
                        await message.answer("Эээ, закатай губу, такой ник уже существует")
                        ni = True
                if len(nick) <= 20 and ni == False:
                    if cena >= 5 and cena <= 1000000:
                        if unib == nick:
                            if work1 != 'Нету':
                                c.execute(f"UPDATE job_{work1} SET worker_nick = '{nick}' WHERE worker_id = {message.from_user.id}")
                            c.execute(f"UPDATE user_data SET user_nick = NULL WHERE user_id = {message.from_user.id}")
                        if rn > 0:
                            if unib == nick:
                                c.execute(f"UPDATE nicks_auction SET user_nick = NULL WHERE user_id = {message.from_user.id}")
                            c.execute(f"UPDATE nicks_auction SET item_time = '{str(date_time)}', item = '{nick}', cena = {cena} WHERE user_id = {message.from_user.id}")
                            await message.answer("Ник выставлен на продажу!")
                        else:
                            if unib == nick:
                                c.execute(f"UPDATE nicks_auction SET user_nick = NULL WHERE user_id = {message.from_user.id}")
                            c.execute(f"UPDATE nicks_auction SET item_time = '{str(date_time)}', item = '{nick}', cena = {cena}, nick_{len(uns) + 1} = '{nick}' WHERE user_id = {message.from_user.id}")
                            await message.answer("Ник выставлен на продажу!")
                    else:
                        await message.answer("Минимальная цена ника 5 эклеров\nМаксимальная цена ника 1 000 000 эклеров")
                elif len(nick) > 20 and ni == False:
                    await message.answer("Максимальная длина ника 20 символов")
    except:
        await message.answer("/sellnick Ник Число")
    db.commit()
    db.close()

#qsbuynick
@dp.message_handler(commands=['buynick'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        nick = message.text[9:]
        while nick.find('у') != -1:
            nick1 = nick[:nick.find('у')]
            nick2 = nick[nick.find('у')+1:]
            nick = nick1 + 'y' + nick2
        while nick.find('е') != -1:
            nick1 = nick[:nick.find('е')]
            nick2 = nick[nick.find('е')+1:]
            nick = nick1 + 'e' + nick2
        while nick.find('х') != -1:
            nick1 = nick[:nick.find('х')]
            nick2 = nick[nick.find('х')+1:]
            nick = nick1 + 'x' + nick2
        while nick.find('а') != -1:
            nick1 = nick[:nick.find('а')]
            nick2 = nick[nick.find('а')+1:]
            nick = nick1 + 'a' + nick2
        while nick.find('р') != -1:
            nick1 = nick[:nick.find('р')]
            nick2 = nick[nick.find('р')+1:]
            nick = nick1 + 'p' + nick2
        while nick.find('о') != -1:
            nick1 = nick[:nick.find('о')]
            nick2 = nick[nick.find('о')+1:]
            nick = nick1 + 'o' + nick2
        while nick.find('с') != -1:
            nick1 = nick[:nick.find('с')]
            nick2 = nick[nick.find('с')+1:]
            nick = nick1 + 'c' + nick2
        while nick.find('К') != -1:
            nick1 = nick[:nick.find('К')]
            nick2 = nick[nick.find('К')+1:]
            nick = nick1 + 'K' + nick2
        while nick.find('Е') != -1:
            nick1 = nick[:nick.find('Е')]
            nick2 = nick[nick.find('Е')+1:]
            nick = nick1 + 'E' + nick2
        while nick.find('Н') != -1:
            nick1 = nick[:nick.find('Н')]
            nick2 = nick[nick.find('Н')+1:]
            nick = nick1 + 'H' + nick2
        while nick.find('Х') != -1:
            nick1 = nick[:nick.find('Х')]
            nick2 = nick[nick.find('Х')+1:]
            nick = nick1 + 'X' + nick2
        while nick.find('В') != -1:
            nick1 = nick[:nick.find('В')]
            nick2 = nick[nick.find('В')+1:]
            nick = nick1 + 'B' + nick2
        while nick.find('А') != -1:
            nick1 = nick[:nick.find('А')]
            nick2 = nick[nick.find('А')+1:]
            nick = nick1 + 'A' + nick2
        while nick.find('Р') != -1:
            nick1 = nick[:nick.find('Р')]
            nick2 = nick[nick.find('Р')+1:]
            nick = nick1 + 'P' + nick2
        while nick.find('О') != -1:
            nick1 = nick[:nick.find('О')]
            nick2 = nick[nick.find('О')+1:]
            nick = nick1 + 'O' + nick2
        while nick.find('С') != -1:
            nick1 = nick[:nick.find('С')]
            nick2 = nick[nick.find('С')+1:]
            nick = nick1 + 'C' + nick2
        while nick.find('М') != -1:
            nick1 = nick[:nick.find('М')]
            nick2 = nick[nick.find('М')+1:]
            nick = nick1 + 'M' + nick2
        while nick.find('Т') != -1:
            nick1 = nick[:nick.find('Т')]
            nick2 = nick[nick.find('Т')+1:]
            nick = nick1 + 'T' + nick2
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
            c.execute(f"SELECT user_id FROM nicks_auction WHERE item = '{nick}'")
            seil = c.fetchall()
            for i in seil:
                sei = i[0]
            c.execute(f"SELECT item_time, item, cena FROM nicks_auction WHERE user_id = {sei}")
            sednal = c.fetchall()
            sedna = []
            for d in sednal:
                sedna.append(d[0])
                sedna.append(d[1])
                sedna.append(d[2])
            c.execute(f"SELECT user_eclairs FROM user_data WHERE user_id = {sei}")
            sedl = c.fetchall()
            for d in sedl:
                sed = d[0]
            c.execute(f"SELECT nick_1, nick_2, nick_3, nick_4, nick_5 FROM nicks_auction WHERE user_id = {sei}")
            senl = c.fetchall()
            sen = []
            for n in senl:
                sen.append(n[0])
                sen.append(n[1])
                sen.append(n[2])
                sen.append(n[3])
                sen.append(n[4])
            nn = 1
            for n in sen:
                if n == nick:
                    break
                else:
                    nn += 1
            c.execute(f"SELECT item, cena FROM nicks_auction WHERE item = '{nick}'")
            ioal = c.fetchall()
            ioa = []
            for i in ioal:
                niit = i[0]
                itce = i[1]
            c.execute(f"SELECT nick_1, nick_2, nick_3, nick_4, nick_5 FROM nicks_auction WHERE user_id = {message.from_user.id}")
            unl = c.fetchall()
            usnl = []
            for n in unl:
                usnl.append(n[0])
                usnl.append(n[1])
                usnl.append(n[2])
                usnl.append(n[3])
                usnl.append(n[4])
            usn = []
            for n in usnl:
                if n == '' or n == None:
                    pass
                else:
                    usn.append(n)
            c.execute(f"SELECT user_id, user_nick, user_eclairs FROM user_data WHERE user_id = {message.from_user.id}")
            ud = c.fetchall()
            for n in ud:
                ubi = n[0]
                un = n[1]
                uec = n[2]
            if len(usn) == 5:
                await message.answer("Нельзя купить ник, мешок ников заполнен!")
            else:
                if uec >= itce and message.from_user.id != sei:
                    price_nick = nick
                    price_eclairs = uec - itce
                    seller_price_eclairs = sed + itce
                    c.execute(f"UPDATE user_data SET user_eclairs = {seller_price_eclairs} WHERE user_id = {sei}")
                    c.execute(f"UPDATE nicks_auction SET item_time = NULL, item = NULL, cena = NULL, nick_{nn} = NULL WHERE user_id = {sei}")
                    c.execute(f"UPDATE user_data SET user_nick = '{price_nick}', user_eclairs = {price_eclairs} WHERE user_id = {message.from_user.id}")
                    if work1 != 'Нету':
                        c.execute(f"UPDATE job_{work1} SET worker_nick = '{price_nick}' WHERE worker_id = {message.from_user.id}")
                    numair = 1
                    cbnn = True
                    for el in usnl:
                        if el == None or el == '':
                            c.execute(f"UPDATE nicks_auction SET user_nick = '{price_nick}', nick_{numair} = '{price_nick}' WHERE user_id = {message.from_user.id}")
                            await message.answer("Ник успешно куплен!")
                            await bot.send_message(sei, f"Пользователь <b><a href='tg://user?id={ubi}'>{un}</a> купил Ваш ник</b>!", parse_mode="HTML")
                            cbnn = False
                            break
                        else:
                            numair += 1
                    if cbnn:
                        c.execute(f"UPDATE nicks_auction SET user_nick = '{price_nick}', nick_{len(usn) + 1} = '{price_nick}' WHERE user_id = {message.from_user.id}")
                        await message.answer("Ник успешно куплен!")
                        await bot.send_message(sei, f"Пользователь <b><a href='tg://user?id={ubi}'>{un}</a> купил Ваш ник</b>!", parse_mode="HTML")
                elif uec < itce:
                    await message.answer("Недостаточно эклеров!")
                elif message.from_user.id == sei:
                    await message.answer("Чел, это твой ник...")
        except:
            await message.answer("Ник не найден")
    except:
        await message.answer("/buynick Ник")
    db.commit()
    db.close()

#qswfs
@dp.message_handler(commands=['wfs'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT item_time, item, cena FROM nicks_auction WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        iosl = []
        for i in items:
            iosl.append(i[0])
            iosl.append(i[1])
            iosl.append(i[2])
        ios = []
        for i in iosl:
            if i == '' or i == None:
                pass
            else:
                ios.append(i)
        if len(ios) == 0:
            await message.answer("У Вас нету ников на продаже")
        else:
            c.execute(f"UPDATE nicks_auction SET item_time = NULL, item = NULL, cena = NULL WHERE user_id = {message.from_user.id}")
            await message.answer(f'Ник "{ios[1]}" снят с продажи')
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

#qsgetnick
@dp.message_handler(commands=['getnick'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        nick = message.text[9:]
        while nick.find(' ') == 0:
            nick = nick[1:]
        while nick.find(' ') == len(nick) - 1:
            nick = nick[:-1]
        while nick.find('ㅤ') == 0:
            nick = nick[1:]
        while nick.find('ㅤ') == len(nick) - 1:
            nick = nick[:-1]
        while nick.find('у') != -1:
            nick1 = nick[:nick.find('у')]
            nick2 = nick[nick.find('у')+1:]
            nick = nick1 + 'y' + nick2
        while nick.find('е') != -1:
            nick1 = nick[:nick.find('е')]
            nick2 = nick[nick.find('е')+1:]
            nick = nick1 + 'e' + nick2
        while nick.find('х') != -1:
            nick1 = nick[:nick.find('х')]
            nick2 = nick[nick.find('х')+1:]
            nick = nick1 + 'x' + nick2
        while nick.find('а') != -1:
            nick1 = nick[:nick.find('а')]
            nick2 = nick[nick.find('а')+1:]
            nick = nick1 + 'a' + nick2
        while nick.find('р') != -1:
            nick1 = nick[:nick.find('р')]
            nick2 = nick[nick.find('р')+1:]
            nick = nick1 + 'p' + nick2
        while nick.find('о') != -1:
            nick1 = nick[:nick.find('о')]
            nick2 = nick[nick.find('о')+1:]
            nick = nick1 + 'o' + nick2
        while nick.find('с') != -1:
            nick1 = nick[:nick.find('с')]
            nick2 = nick[nick.find('с')+1:]
            nick = nick1 + 'c' + nick2
        while nick.find('К') != -1:
            nick1 = nick[:nick.find('К')]
            nick2 = nick[nick.find('К')+1:]
            nick = nick1 + 'K' + nick2
        while nick.find('Е') != -1:
            nick1 = nick[:nick.find('Е')]
            nick2 = nick[nick.find('Е')+1:]
            nick = nick1 + 'E' + nick2
        while nick.find('Н') != -1:
            nick1 = nick[:nick.find('Н')]
            nick2 = nick[nick.find('Н')+1:]
            nick = nick1 + 'H' + nick2
        while nick.find('Х') != -1:
            nick1 = nick[:nick.find('Х')]
            nick2 = nick[nick.find('Х')+1:]
            nick = nick1 + 'X' + nick2
        while nick.find('В') != -1:
            nick1 = nick[:nick.find('В')]
            nick2 = nick[nick.find('В')+1:]
            nick = nick1 + 'B' + nick2
        while nick.find('А') != -1:
            nick1 = nick[:nick.find('А')]
            nick2 = nick[nick.find('А')+1:]
            nick = nick1 + 'A' + nick2
        while nick.find('Р') != -1:
            nick1 = nick[:nick.find('Р')]
            nick2 = nick[nick.find('Р')+1:]
            nick = nick1 + 'P' + nick2
        while nick.find('О') != -1:
            nick1 = nick[:nick.find('О')]
            nick2 = nick[nick.find('О')+1:]
            nick = nick1 + 'O' + nick2
        while nick.find('С') != -1:
            nick1 = nick[:nick.find('С')]
            nick2 = nick[nick.find('С')+1:]
            nick = nick1 + 'C' + nick2
        while nick.find('М') != -1:
            nick1 = nick[:nick.find('М')]
            nick2 = nick[nick.find('М')+1:]
            nick = nick1 + 'M' + nick2
        while nick.find('Т') != -1:
            nick1 = nick[:nick.find('Т')]
            nick2 = nick[nick.find('Т')+1:]
            nick = nick1 + 'T' + nick2
        if nick == '':
            await message.answer("/getnick Ник")
        else:
            if len(nick) > 20:
                await message.answer("Максимальная длина ника 20 символов")
            else:
                try:
                    c.execute(f"SELECT nick_1, nick_2, nick_3, nick_4, nick_5 FROM nicks_auction WHERE user_id = {message.from_user.id}")
                    items = c.fetchall()
                    unsl = []
                    for i in items:
                        unsl.append(i[0])
                        unsl.append(i[1])
                        unsl.append(i[2])
                        unsl.append(i[3])
                        unsl.append(i[4])
                    uns = []
                    print(unsl)
                    for i in unsl:
                        if i == '' or i == None:
                            pass
                        else:
                            uns.append(i)
                    c.execute(f"SELECT nick_1, nick_2, nick_3, nick_4, nick_5 FROM nicks_auction WHERE user_id <> {message.from_user.id}")
                    items = c.fetchall()
                    aunsl = []
                    for i in items:
                        aunsl.append(i[0])
                        aunsl.append(i[1])
                        aunsl.append(i[2])
                        aunsl.append(i[3])
                        aunsl.append(i[4])
                    auns = []
                    for i in aunsl:
                        if i == '' or i == None:
                            pass
                        else:
                            auns.append(i)
                    for n in auns:
                        if n == nick:
                            print(forerrorprint)
                    if len(uns) == 5:
                        await message.answer("Мешок ников заполнен")
                    else:
                        for n in unsl:
                            if n == nick:
                                print(forerrorprint)
                        numair = 1
                        cgnn = True
                        for el in unsl:
                            if el == None or el == '':
                                c.execute(f"UPDATE nicks_auction SET nick_{numair} = '{nick}' WHERE user_id = {message.from_user.id}")
                                await message.answer(f'Ник "<b>{nick}</b>" добавлен в мешок!', parse_mode="HTML")
                                cgnn = False
                                break
                            else:
                                numair += 1
                        if cgnn:
                            c.execute(f"UPDATE nicks_auction SET nick_{len(uns) + 1} = '{nick}' WHERE user_id = {message.from_user.id}")
                            await message.answer(f'Ник "<b>{nick}</b>" добавлен в мешок!', parse_mode="HTML")
                except:
                    cnc = 0
                    for n in auns:
                        if n == nick:
                            await message.answer(f'Ник "<b>{nick}</b>" занят', parse_mode="HTML")
                            cnc += 1
                    for n in unsl:
                            if n == nick:
                                await message.answer(f'Ник "<b>{nick}</b>" уже есть в Вашем мешке', parse_mode="HTML")
                                cnc += 1
                    if cnc == 0:
                        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    except:
        await message.answer("/getnick Ник")
    db.commit()
    db.close()

#qsdelnick
@dp.message_handler(commands=['delnick'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        nick = message.text[9:]
        while nick.find('у') != -1:
            nick1 = nick[:nick.find('у')]
            nick2 = nick[nick.find('у')+1:]
            nick = nick1 + 'y' + nick2
        while nick.find('е') != -1:
            nick1 = nick[:nick.find('е')]
            nick2 = nick[nick.find('е')+1:]
            nick = nick1 + 'e' + nick2
        while nick.find('х') != -1:
            nick1 = nick[:nick.find('х')]
            nick2 = nick[nick.find('х')+1:]
            nick = nick1 + 'x' + nick2
        while nick.find('а') != -1:
            nick1 = nick[:nick.find('а')]
            nick2 = nick[nick.find('а')+1:]
            nick = nick1 + 'a' + nick2
        while nick.find('р') != -1:
            nick1 = nick[:nick.find('р')]
            nick2 = nick[nick.find('р')+1:]
            nick = nick1 + 'p' + nick2
        while nick.find('о') != -1:
            nick1 = nick[:nick.find('о')]
            nick2 = nick[nick.find('о')+1:]
            nick = nick1 + 'o' + nick2
        while nick.find('с') != -1:
            nick1 = nick[:nick.find('с')]
            nick2 = nick[nick.find('с')+1:]
            nick = nick1 + 'c' + nick2
        while nick.find('К') != -1:
            nick1 = nick[:nick.find('К')]
            nick2 = nick[nick.find('К')+1:]
            nick = nick1 + 'K' + nick2
        while nick.find('Е') != -1:
            nick1 = nick[:nick.find('Е')]
            nick2 = nick[nick.find('Е')+1:]
            nick = nick1 + 'E' + nick2
        while nick.find('Н') != -1:
            nick1 = nick[:nick.find('Н')]
            nick2 = nick[nick.find('Н')+1:]
            nick = nick1 + 'H' + nick2
        while nick.find('Х') != -1:
            nick1 = nick[:nick.find('Х')]
            nick2 = nick[nick.find('Х')+1:]
            nick = nick1 + 'X' + nick2
        while nick.find('В') != -1:
            nick1 = nick[:nick.find('В')]
            nick2 = nick[nick.find('В')+1:]
            nick = nick1 + 'B' + nick2
        while nick.find('А') != -1:
            nick1 = nick[:nick.find('А')]
            nick2 = nick[nick.find('А')+1:]
            nick = nick1 + 'A' + nick2
        while nick.find('Р') != -1:
            nick1 = nick[:nick.find('Р')]
            nick2 = nick[nick.find('Р')+1:]
            nick = nick1 + 'P' + nick2
        while nick.find('О') != -1:
            nick1 = nick[:nick.find('О')]
            nick2 = nick[nick.find('О')+1:]
            nick = nick1 + 'O' + nick2
        while nick.find('С') != -1:
            nick1 = nick[:nick.find('С')]
            nick2 = nick[nick.find('С')+1:]
            nick = nick1 + 'C' + nick2
        while nick.find('М') != -1:
            nick1 = nick[:nick.find('М')]
            nick2 = nick[nick.find('М')+1:]
            nick = nick1 + 'M' + nick2
        while nick.find('Т') != -1:
            nick1 = nick[:nick.find('Т')]
            nick2 = nick[nick.find('Т')+1:]
            nick = nick1 + 'T' + nick2
        try:
            c.execute(f"SELECT nick_1, nick_2, nick_3, nick_4, nick_5 FROM nicks_auction WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            unsl = []
            for i in items:
                unsl.append(i[0])
                unsl.append(i[1])
                unsl.append(i[2])
                unsl.append(i[3])
                unsl.append(i[4])
            uns = []
            for i in unsl:
                if i == '' or i == None:
                    pass
                else:
                    uns.append(i)
            nn = 1
            for n in unsl:
                if n == nick:
                    break
                else:
                    nn += 1
            if len(uns) == 0:
                await message.answer("В мешке нету ников")
            else:
                c.execute(f"UPDATE nicks_auction SET nick_{nn} = NULL WHERE user_id = {message.from_user.id}")
                await message.answer(f'Ник "<b>{nick}</b>" удален из мешка!', parse_mode="HTML")
        except:
            await message.answer("В Вашем мешке нету такого ника")
    except:
        await message.answer("/delnick Ник")
    db.commit()
    db.close()

#qsmynicks
@dp.message_handler(commands=['mynicks'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT nick_1, nick_2, nick_3, nick_4, nick_5 FROM nicks_auction WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        unll = []
        for el in items:
            unll.append(el[0])
            unll.append(el[1])
            unll.append(el[2])
            unll.append(el[3])
            unll.append(el[4])
        unl = []
        for el in unll:
            if el == '' or el == None:
                unl.append("Нету")
            else:
                unl.append(el)
        c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
        await message.answer(f"""<b>Ники в мешке <a href='tg://user?id={message.from_user.id}'>{un}</a>:</b>

1. <code>{unl[0]}</code>
2. <code>{unl[1]}</code>
3. <code>{unl[2]}</code>
4. <code>{unl[3]}</code>
5. <code>{unl[4]}</code>""", parse_mode="HTML")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()