from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from dispatcher import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,
                                      MessageToDeleteNotFound)
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery
import sqlite3
import datetime

@dp.message_handler(Text(startswith=['создать клан', 'Создать клан']))
async def process_start_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        comm = message.text[13:]
        if comm.find("""
""") != -1:
            clan_name = comm.split("""
""")[0]
            clan_desc = comm[len(clan_name)+1:]
        else:
            clan_name = comm
            clan_desc = None
        if len(clan_name) > 20:
            await message.answer("Максимальная длина названия клана 20 символов")
            print(forerrorprint)
        if clan_desc != None:
            if len(clan_desc) > 50:
                await message.answer("Максимальная длина описания клана 50 символов")
                print(forerrorprint)
        if clan_name == '' or clan_name == ' ':
            await message.answer("Создать клан Название\nОписание")
            print(forerrorprint)
        if clan_desc == '' or clan_desc == ' ':
            clan_desc == None
        ui = message.from_user.id
        c.execute(f"SELECT user_prefix, user_nick, user_chapchas FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            upr = el[0]
            un = el[1]
            uch = el[2]
        try:
            c.execute(f"SELECT leader_id FROM clan_data WHERE leader_id = {ui}")
            items = c.fetchall()
            for el in items:
                li = el[0]
            if li == ui:
                await message.answer("У Вас уже есть клан!")
        except:
            try:
                c.execute(f"SELECT clan_name FROM clan_data")
                items = c.fetchall()
                for el in items:
                    if clan_name == el[0]:
                        await message.answer("Клан с таким названием уже существует")
                        gcc = False
                        break
                    else:
                        pass
                if gcc:
                    print(forerrorprint)
            except:
                try:
                    gccc = True
                    c.execute(f"SELECT * FROM clan_data")
                    items = c.fetchall()
                    for el in items:
                        for e in el:
                            if e == message.from_user.id:
                                await message.answer("Вы уже состоите в клане!")
                                gccc = False
                    if gccc:
                        print(forerrorprint)
                except:
                    if uch >= 500:
                        cncl = InlineKeyboardButton("Отмена", callback_data='cnclcreateclan')
                        create = InlineKeyboardButton("Создать клан", callback_data='createclan')
                        floor = InlineKeyboardMarkup().add(cncl).add(create)
                        if clan_desc != None:
                            await message.answer(f"""⚜️ | Пользователь <a href='tg://user?id={ui}'>{un}</a> создает клан:

🏷 | <b>Название:</b> {clan_name}
🗓 | <b>Описание:</b> {clan_desc}
💲 | <b>Цена:</b> 500 чапчей""", parse_mode="HTML", reply_markup=floor)
                            try:
                                c.execute(f"INSERT INTO clan_events VALUES (?, ?, ?, ?)",
                                          (ui, clan_name, clan_desc, None))
                            except:
                                c.execute(f"UPDATE clan_events SET clan_name = {clan_name}, clan_desc = {clan_desc} WHERE user_id = {ui}")
                        else:
                            await message.answer(f"""⚜️ | Пользователь <a href='tg://user?id={ui}'>{un}</a> создает клан:

🏷 | <b>Название:</b> {clan_name}
💲 | <b>Цена:</b> 500 чапчей""", parse_mode="HTML", reply_markup=floor)
                            try:
                                c.execute(f"INSERT INTO clan_events VALUES (?, ?, ?, ?)",
                                          (ui, clan_name, '', None))
                            except:
                                c.execute(f"UPDATE clan_events SET clan_name = {clan_name}, clan_desc = '' WHERE user_id = {ui}")
                    else:
                        await message.answer("Недостаточно средств для создания клана!")
    except:
        pass
    db.commit()
    db.close()





#qsdeleteclan
@dp.message_handler(Text(startswith=['удалить клан', 'Удалить клан']))
async def process_start_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        ci = message.text[14:]
        c.execute(f"SELECT leader_id, clan_name FROM clan_data WHERE leader_id = {message.from_user.id}")
        items = c.fetchall()
        cd = []
        for el in items:
            for e in el:
                cd.append(e)
        if len(cd) < 2:
            await message.answer("У Вас нету клана")
            print(forerrorprint)
        try:
            c.execute("INSERT INTO clan_events VALUES (?, ?, ?, ?)",
                      (message.from_user.id, None, None, ci))
        except:
            c.execute(f"UPDATE clan_events SET clan_del = {ci} WHERE user_id = {message.from_user.id}")
        cncl = InlineKeyboardButton("Отмена", callback_data='cncldelclan')
        dc = InlineKeyboardButton("Удалить", callback_data='delclan')
        floor = InlineKeyboardMarkup().add(cncl).add(dc)
        await message.answer(f"Удаление клана <b>{cd[1]}</b>", parse_mode="HTML", reply_markup=floor)
    except:
        pass


@dp.callback_query_handler(text=['cnclcreateclan'])
async def turn_on_bad_words(call: types.CallbackQuery):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"DELETE FROM clan_events WHERE user_id = {call.from_user.id}")
        await call.message.edit_text("Создание клана отменено")
    except:
        pass
    db.commit()
    db.close()

@dp.callback_query_handler(text=['cncldelclan'])
async def turn_on_bad_words(call: types.CallbackQuery):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"DELETE FROM clan_events WHERE user_id = {call.from_user.id}")
        await call.message.edit_text("Удаление клана отменено")
    except:
        pass
    db.commit()
    db.close()

@dp.callback_query_handler(text=['createclan'])
async def turn_on_bad_words(call: types.CallbackQuery):
    date_pre = datetime.datetime.now()
    date_time = date_pre.strftime("%d.%m.%y %H:%M")
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_id, user_prefix, user_nick, user_reputation, user_points, user_eclairs, user_coins, user_chapchas, user_freebases FROM user_data WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ui = el[0]
            upr = el[1]
            un = el[2]
            ur = el[3]
            up = el[4]
            uec = el[5]
            uc = el[6]
            uch = el[7]
            uf = el[8]
        if ui == '' or ui == None:
            await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
            print(forerrorprint)
        try:
            c.execute(f"SELECT leader_id FROM clan_data WHERE leader_id = {ui}")
            items = c.fetchall()
            for el in items:
                li = el[0]
            if li == ui:
                await message.answer("У Вас уже есть клан!")
            else:
                print(forerrorprint)
        except:
            try:
                c.execute(f"SELECT clan_name FROM clan_data")
                items = c.fetchall()
                for el in items:
                    if clan_name == el[0]:
                        await message.answer("Клан с таким названием уже существует")
                        gcc = False
                    else:
                        pass
                if gcc:
                    print(forerrorprint)
            except:
                try:
                    c.execute(f"SELECT * FROM clan_events WHERE user_id = {call.from_user.id}")
                    items = c.fetchall()
                    for el in items:
                        clan_name = el[1]
                        clan_desc = el[2]
                except:
                    await call.message.edit_text("Ошибка")
                if uch >= 500:
                    price_chapchas = uch - 500
                    if clan_desc == '' or clan_desc == None:
                        c.execute("INSERT INTO clan_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (ui, clan_name, 'Отсутствует', date_time, 'Общага', ur, 0, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None))
                    else:
                        c.execute("INSERT INTO clan_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (ui, clan_name, clan_desc, date_time, 'Общага', ur, 0, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None))
                    
                    c.execute(f"DELETE FROM clan_events WHERE user_id = {ui}")
                    c.execute(f"UPDATE user_data SET user_chapchas = {price_chapchas} WHERE user_id = {ui}")
                    await call.message.edit_text(f"Клан <b>{clan_name}</b> успешно создан!", parse_mode="HTML")
                else:
                    await call.message.edit_text("Недостаточно средств для создания клана!")
    except:
        pass
    db.commit()
    db.close()

@dp.callback_query_handler(text=['delclan'])
async def turn_on_bad_words(call: types.CallbackQuery):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT clan_del FROM clan_events WHERE user_id = {call.from_user.id}")
        items = c.fetchall()
        for el in items:
            ci = el[0]
        c.execute(f"SELECT clan_name FROM clan_data WHERE leader_id = {ci}")
        items = c.fetchall()
        for el in items:
            cn = el[0]
        if ci != call.from_user.id:
            await call.answer("Эээ, руки прибрал(а)")
        else:
            c.execute(f"DELETE FROM clan_data WHERE leader_id = {ci}")
            c.execute(f"DELETE FROM clan_events WHERE user_id = {ci}")
            await call.message.edit_text(f"Клан <b>{cn}</b> удален", parse_mode="HTML")
    except:
        pass
    db.commit()
    db.close()


@dp.message_handler(text=['Мой клан', 'Клан', 'мой клан', 'клан'])
async def my_clan(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT * from clan_data")
    items = c.fetchall()
    clanl = []
    try:
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
            await message.answer("Вы не состоите в клане((")
        else:
            if mbn != 0:
                c.execute(f"SELECT leader_id, clan_name, clan_desc, clan_register_date, clan_prefix, clan_reputation, clan_chapchas, clan_freebases FROM clan_data WHERE mb{mbn} = {message.from_user.id}")
            else:
                c.execute(f"SELECT leader_id, clan_name, clan_desc, clan_register_date, clan_prefix, clan_reputation, clan_chapchas, clan_freebases FROM clan_data WHERE leader_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                li = el[0]
                cn = el[1]
                cd = el[2]
                cregd = el[3]
                cpr = el[4]
                crd = el[5]
                cch = el[6]
                cf = el[7]
            c.execute(f"SELECT user_prefix, user_nick, user_reputation FROM user_data WHERE user_id = {li}")
            items = c.fetchall()
            for el in items:
                upr = el[0]
                un = el[1]
                urep = el[2]
            c.execute(f"SELECT * FROM clan_data WHERE leader_id = {li}")
            items = c.fetchall()
            mbsl = []
            for el in items:
                for e in el:
                    mbsl.append(e)
            mbs = []
            itsn = -8
            for el in mbsl:
                itsn += 1
                if itsn > 0:
                    if el == '' or el == None or el == 'None':
                        pass
                    else:
                        mbs.append(el)
            sumar = urep
            mbicn = 0
            for el in mbs:
                mbicn += 1
                c.execute(f"SELECT user_reputation FROM user_data WHERE user_id = {el}")
                items = c.fetchall()
                for el in items:
                    urta = el[0]
                try:
                    sumar += urta
                except:
                    itsn -= 1
                    c.execute(f"UPDATE clan_data SET mb{mbicn} = Null WHERE leader_id = {li}")
            if sumar != crd:
                c.execute(f"UPDATE clan_data SET clan_reputation = {sumar} WHERE leader_id = {li}")
            if cd == 'Отсутствует':
                await message.answer(f"""Клан <b><i>[{cpr}]</i></b> {cn}

<b>Лидер:</b> <b><i>[{upr}]</i></b> <a href='tg://user?id={li}'>{un}</a>
<b>Дата основания:</b> {cregd}
<b>Репутация:</b> {sumar}
<b>Участников:</b> {len(clan) - 7}

Баланс:
<b>Чапчи:</b> {cch}
<b>Фрибасы:</b> {cf}

<code>Вступить в клан {li}</code>""", parse_mode="HTML")
            else:
                await message.answer(f"""Клан <b><i>[{cpr}]</i></b> {cn}
{cd}

<b>Лидер:</b> <b><i>[{upr}]</i> </b><a href='tg://user?id={li}'>{un}</a>
<b>Дата основания:</b> {cregd}
<b>Репутация:</b> {sumar}
<b>Участников:</b> {len(clan) - 7}

Баланс:
<b>Чапчи:</b> {cch}
<b>Фрибасы:</b> {cf}

<code>Вступить в клан {li}</code>""", parse_mode="HTML")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()


@dp.message_handler(Text(startswith=['Вступить в клан', 'вступить в клан']))
async def vst_v_clan(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        ci = message.text[16:]
        try:
            c.execute(f"SELECT user_id, user_prefix, user_nick, user_reputation FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                ui = el[0]
                upr = el[1]
                un = el[2]
                ur = el[3]
            try:
                c.execute(f"SELECT * FROM clan_data WHERE leader_id = {ci}")
                items = c.fetchall()
                cdl = []
                for el in items:
                    cn = el[1]
                    for e in el:
                        cdl.append(e)
                cd = []
                for el in cdl:
                    if el == '' or el == None or el == 'None':
                        pass
                    else:
                        cd.append(el)
                c.execute(f"SELECT * FROM clan_data")
                items = c.fetchall()
                for el in items:
                    for e in el:
                        if e == message.from_user.id:
                            await message.answer("Вы уже состоите в клане!")
                            print(forerrorprint)
                for el in cd:
                    if el == message.from_user.id:
                        await message.answer(f"<a href='tg://user?id={ui}'>{un}</a> Вы уже состоите в клане!", parse_mode="HTML")
                        print(forerrorprint)
                print(message.from_user.id)
                mbnn = -8
                for el in items:
                    for e in el:
                        mbnn += 1
                        if e == '' or e == None or e == 'None' and mbnn > 0:
                            c.execute(f"UPDATE clan_data SET mb{mbnn} = {message.from_user.id} WHERE leader_id = {ci}")
                            await message.answer(f"<a href='tg://user?id={ui}'>{un}</a> Вы вступили в клан <b>{cn}</b>!", parse_mode="HTML")
                            print(forerrorprint)
                c.execute(f"UPDATE clan_data SET mb{len(cd) - 7} = {message.from_user.id} WHERE leader_id = {ci}")
                await message.answer(f"<a href='tg://user?id={ui}'>{un}</a> Вы вступили в клан <b>{cn}</b>!", parse_mode="HTML")
            except:
                pass
        except:
            await message.answer("Вступить в клан ID")
    except:
        pass
    db.commit()
    db.close()

@dp.message_handler(Text(startswith=['Покинуть клан', 'покинуть клан']))
async def vst_v_clan(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        ci = int(message.text[14:])
        try:
            if ci == message.from_user.id:
                await message.answer("Лидер клана не может покинуть клан!")
                print(forerrorprint)
            c.execute(f"SELECT user_id, user_prefix, user_nick, user_reputation FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                ui = el[0]
                upr = el[1]
                un = el[2]
                ur = el[3]
            try:
                c.execute(f"SELECT * FROM clan_data WHERE leader_id = {ci}")
                items = c.fetchall()
                cdl = []
                for el in items:
                    cn = el[1]
                    for e in el:
                        cdl.append(e)
                cd = []
                for el in cdl:
                    if el == '' or el == None or el == 'None':
                        pass
                    else:
                        cd.append(el)
                mbn = -8
                for el in cd:
                    mbn += 1
                    if el == message.from_user.id and mbn > 0:
                        c.execute(f"UPDATE clan_data SET mb{mbn} = 'None' WHERE leader_id = {ci}")
                        await message.answer(f"<a href='tg://user?id={ui}'>{un}</a> покинул(а) клан <b>{cn}</b>!", parse_mode="HTML")
                        print(forerrorprint)
                await message.answer("Вы не состоите в этом клане")
            except:
                pass
        except:
            pass
    except:
        await message.answer("Покинуть клан ID")
    db.commit()
    db.close()

@dp.message_handler(Text(startswith=['Выгнать из клана', 'выгнать из клана']))
async def vst_v_clan(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        mi = int(message.text[17:])
        try:
            c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {mi}")
            items = c.fetchall()
            for el in items:
                un = el[0]
            c.execute(f"SELECT * FROM clan_data WHERE leader_id = {message.from_user.id}")
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
            if len(clan) < 11:
                await message.answer("У Вас нету клана")
            else:
                mbn = -8
                ck = False
                cn = clan[1]
                for el in clan:
                    mbn += 1
                    if el == mi and mbn > 0:
                        ck = True
                        break
                    elif el == mi and mbn < 0:
                        await message.answer("Вы лидер клана, Вы не можете выгнать себя!")
                        mbn = -8
                    else:
                        pass
                if ck and mbn > 0:
                    c.execute(f"UPDATE clan_data SET mb{mbn} = 'None' WHERE leader_id = {message.from_user.id}")
                    await message.answer(f"Пользователь <a href='tg://user?id={mi}'>{un}</a> был исключен из клана <b>{cn}</b>", parse_mode="HTML")
                else:
                    await message.answer("В Вашем клане нету пользователя с указаным ID")
        except:
            pass
    except:
        await message.answer("Выгнать из клана ID")
    db.commit()
    db.close()

@dp.message_handler(text=['Баланс клана', 'Клан баланс', 'баланс клана', 'клан баланс'])
async def vst_v_clan(message: types.Message):
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
            await message.answer("Вы не состоите в клане((")
        else:
            if mbn != 0:
                c.execute(f"SELECT clan_name, clan_prefix, clan_chapchas, clan_freebases FROM clan_data WHERE mb{mbn} = {message.from_user.id}")
            else:
                c.execute(f"SELECT clan_name, clan_prefix, clan_chapchas, clan_freebases FROM clan_data WHERE leader_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                cn = el[0]
                cpr = el[1]
                cch = el[2]
                cf = el[3]
            await message.answer(f"""Баланс клана <b><i>[{cpr}]</i></b> {cn}

<b>Чапчи:</b> {cch}
<b>Фрибасы:</b> {cf}""", parse_mode="HTML")
    except:
        pass
    db.commit()
    db.close()

@dp.message_handler(Text(startswith=['Вложить чапчи', 'Вкинуть чапчи', 'вложить чапчи', 'вкинуть чапчи']))
async def vst_v_clan(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        num = int(message.text[14:])
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
                await message.answer("Вы не состоите в клане((")
            else:
                if mbn != 0:
                    c.execute(f"SELECT clan_name, clan_chapchas FROM clan_data WHERE mb{mbn} = {message.from_user.id}")
                else:
                    c.execute(f"SELECT clan_name, clan_chapchas FROM clan_data WHERE leader_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    cn = el[0]
                    cch = el[1]
                c.execute(f"SELECT user_nick, user_prefix, user_chapchas FROM user_data WHERE user_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    un = el[0]
                    upr = el[1]
                    uch = el[2]
                if num <= uch:
                    if num > 0:
                        price_chapchas = cch + num
                        c.execute(f"UPDATE clan_data SET clan_chapchas = {price_chapchas} WHERE leader_id = {li}")
                        price_fu_chapchas = uch - num
                        c.execute(f"UPDATE user_data SET user_chapchas = {price_fu_chapchas} WHERE user_id = {message.from_user.id}")
                        await message.answer(f"""Пользователь <b><i>[{upr}]</i></b> <a href='tg://user?id={message.from_user.id}'>{un}</a> вложил {num} чапчей на счет клана {cn}!""", parse_mode="HTML")
                    else:
                        await message.answer("Минимальная сумма вложения 1 чапча")
                else:
                    await message.answer("Недостаточно средств")
        except:
            await message.answer("Вложить чапчи Число")
    except:
        pass
    db.commit()
    db.close()

@dp.message_handler(Text(startswith=['Вложить фрибасы', 'Вкинуть фрибасы', 'вложить фрибасы', 'вкинуть фрибасы']))
async def vst_v_clan(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        num = int(message.text[16:])
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
                await message.answer("Вы не состоите в клане((")
            else:
                if mbn != 0:
                    c.execute(f"SELECT clan_name, clan_freebases FROM clan_data WHERE mb{mbn} = {message.from_user.id}")
                else:
                    c.execute(f"SELECT clan_name, clan_freebases FROM clan_data WHERE leader_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    cn = el[0]
                    cf = el[1]
                c.execute(f"SELECT user_nick, user_prefix, user_freebases FROM user_data WHERE user_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    un = el[0]
                    upr = el[1]
                    uf = el[2]
                if num <= uf:
                    if num > 0:
                        price_freebases = cf + num
                        c.execute(f"UPDATE clan_data SET clan_freebases = {price_freebases} WHERE leader_id = {li}")
                        price_fu_freebases = uf - num
                        c.execute(f"UPDATE user_data SET user_freebases = {price_fu_freebases} WHERE user_id = {message.from_user.id}")
                        await message.answer(f"""Пользователь <b><i>[{upr}]</i></b> <a href='tg://user?id={message.from_user.id}'>{un}</a> вложил {num} фрибасов на счет клана {cn}!""", parse_mode="HTML")
                    else:
                        await message.answer("Минимальная сумма вложения 1 фрибас")
                else:
                    await message.answer("Недостаточно средств")
        except:
            await message.answer("Вложить фрибасы Число")
    except:
        pass
    db.commit()
    db.close()