from aiogram import types
from dispatcher import bot, dp
from .Game_Farm_Timer import Game_Farm_Timer
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery
import sqlite3
import datetime



@dp.message_handler(text=['+Брак', '+брак'])
async def profile(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        pai = message.reply_to_message.from_user.id
        if pai == bot.id:
            await message.answer("Я щас все Alone расскажу!")
        elif pai == message.from_user.id:
            await message.answer("Ты по-моему перепутал")
        else:
            c.execute(f"SELECT user_nick, mary FROM user_data WHERE user_id = {pai}")
            items = c.fetchall()
            for el in items:
                pan = el[0]
                pam = el[1]
            if pam == 0:
                try:
                    c.execute(f"SELECT user_nick, mary FROM user_data WHERE user_id = {message.from_user.id}")
                    items = c.fetchall()
                    for el in items:
                        un = el[0]
                        um = el[1]
                    if um == 0:
                        ac = InlineKeyboardButton('💝 Согласиться', callback_data=f'accept_mary:{message.from_user.id}:{pai}')
                        dec = InlineKeyboardButton('💔 Отказаться', callback_data=f'decline_mary:{message.from_user.id}:{pai}')
                        floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).row(ac, dec)
                        await message.answer(f"<b><a href='tg://user?id={message.from_user.id}'>{un}</a> сделал предложение <a href='tg://user?id={pai}'>{pan}</a></b>!", parse_mode="HTML", reply_markup=floor)
                    else:
                        await message.answer("Вы уже состоите в браке!")
                except:
                    await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
            else:
                await message.answer(f"<b><a href='tg://user?id={pai}>{pan}</a></b> уже состоит в браке!")
    except:
        pass
    db.commit()
    db.close()


@dp.callback_query_handler(Text(startswith="accept_mary"))
async def help_bt(call: types.CallbackQuery):
    ui = int(call.data.split(':')[1])
    pai = int(call.data.split(':')[2])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    if call.from_user.id != pai:
        await call.answer("Не трогай чужую кнопочку!")
    else:
        try:
            c.execute(f"SELECT user_nick, mary FROM user_data WHERE user_id = {ui}")
            items = c.fetchall()
            for el in items:
                un = el[0]
                um = el[1]
            if um == 0:
                c.execute(f"SELECT user_nick, mary FROM user_data WHERE user_id = {pai}")
                items = c.fetchall()
                for el in items:
                    pan = el[0]
                    pam = el[1]
                if pam == 0:
                    date_pre = datetime.datetime.now()
                    date_time = date_pre.strftime('%Y-%m-%d %H:%M:%S')
                    c.execute("INSERT INTO mary VALUES (?, ?, ?, ?, ?)",
                              (ui, pai, date_time, 0, 1))
                    c.execute(f"UPDATE user_data SET mary = {ui} WHERE user_id = {ui} OR user_id = {pai}")
                    await call.message.edit_text(f"<b>С этого прекрасного момента <a href='tg://user?id={ui}'>{un}</a> и <a href='tg://user?id={pai}'>{pan}</a> состоят в браке!</b>", parse_mode="HTML")
                else:
                    await call.message.edit_text(f"<b>Пользователь <a href='tg://user?id={pai}'>{pan}</a> уже состоит в браке!</b>", parse_mode="HTML")
            else:
                await call.message.edit_text(f"<b>Пользователь <a href='tg://user?id={ui}'>{un}</a> уже состоит в браке!</b>", parse_mode="HTML")
        except:
            pass
    db.commit()
    db.close()


@dp.callback_query_handler(Text(startswith="decline_mary"))
async def help_bt(call: types.CallbackQuery):
    ui = int(call.data.split(':')[1])
    pai = int(call.data.split(':')[2])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    if call.from_user.id != pai:
        await call.answer("Не трогай чужую кнопочку!")
    else:
        try:
            c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {ui}")
            items = c.fetchall()
            for el in items:
                un = el[0]
            c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {pai}")
            items = c.fetchall()
            for el in items:
                pan = el[0]
            await call.message.edit_text(f"<b><a href='tg://user?id={ui}'>{un}</a> сожалеем, но <a href='tg://user?id={pai}'>{pan}</a> отвергнул Вас...</b>", parse_mode="HTML")
        except:
            pass
    db.commit()
    db.close()



@dp.message_handler(text=['!Развод', '!развод', '/Развод', '/развод', '.Развод', '.развод'])
async def profile(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_nick, mary FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            ui = message.from_user.id
            un = el[0]
            um = el[1]
        if um != 0:
            if um == ui:
                c.execute(f"SELECT user2_id FROM mary WHERE user1_id = {ui}")
            else:
                c.execute(f"SELECT user1_id FROM mary WHERE user2_id = {ui}")
            items = c.fetchall()
            for el in items:
                pai = el[0]
            c.execute(f"SELECT user_nick, mary FROM user_data WHERE user_id = {pai}")
            items = c.fetchall()
            for el in items:
                pan = el[0]
                pam = el[1]
            btn1 = InlineKeyboardButton('💔 Развод', callback_data=f'razwod:{ui}:{pai}')
            cncl = InlineKeyboardButton('❤️‍🩹 Отмена', callback_data=f'cnclrazwod:{ui}')
            floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).row(btn1, cncl)
            await message.answer(f"<b>💔 <a href='tg://user?id={ui}'>{un}</a> хочет развестись с <a href='tg://user?id={pai}'>{pan}</a></b>", parse_mode="HTML", reply_markup=floor)
        else:
            await message.answer("Вы не состоите в браке")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()


@dp.callback_query_handler(Text(startswith="razwod"))
async def help_bt(call: types.CallbackQuery):
    ui = int(call.data.split(':')[1])
    pai = int(call.data.split(':')[2])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    if call.from_user.id != ui:
        await call.answer("Не трогай чужую кнопочку!")
    else:
        try:
            c.execute(f"SELECT user_nick, mary FROM user_data WHERE user_id = {ui}")
            items = c.fetchall()
            for el in items:
                un = el[0]
                um = el[1]
            c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {pai}")
            items = c.fetchall()
            for el in items:
                pan = el[0]
            if um == ui:
                c.execute(f"DELETE FROM mary WHERE user1_id = {ui}")
            else:
                c.execute(f"DELETE FROM mary WHERE user2_id = {ui}")
            c.execute(f"UPDATE user_data SET mary = 0 WHERE user_id = {ui} OR user_id = {pai}")
            await call.message.edit_text(f"<b>💔 <a href='tg://user?id={pai}'>{pan}</a>, сожалеем, <a href='tg://user?id={ui}'>{un}</a> подал на развод</b>", parse_mode="HTML")
        except:
            pass
    db.commit()
    db.close()


@dp.callback_query_handler(Text(startswith="cnclrazwod"))
async def help_bt(call: types.CallbackQuery):
    ui = int(call.data.split(':')[1])
    if call.from_user.id != ui:
        await call.answer("Не трогай чужую кнопочку!")
    else:
        await call.message.edit_text("❤️‍🩹 Развод отменен!")



@dp.message_handler(text=['Мой брак', '!Брак', 'мой брак', '!брак'])
async def profile(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_nick, mary FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            um = el[1]
        ui = message.from_user.id
        if um != 0:
            c.execute(f"SELECT * FROM mary WHERE user1_id = {um}")
            items = c.fetchall()
            for el in items:
                ui1 = el[0]
                ui2 = el[1]
                date = el[2]
                xp = el[3]
                lvl = el[4]
            c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {ui1}")
            items = c.fetchall()
            for el in items:
                u1n = el[0]
            c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {ui2}")
            items = c.fetchall()
            for el in items:
                u2n = el[0]
            date2 = str(datetime.datetime.now()-datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S'))
            try:
                days = int(date2.split(' ')[0])
            except:
                days = 0
            years = 0
            month = 0
            date1 = ''
            while days > 29:
                month += 1
                days -= 30
            while month > 11:
                years += 1
                month -= 12
            if years != 0:
                date1 += str(years) + ' лет '
            if month != 0:
                date1 += str(month) + ' месяцев '
            if days != 0:
                date1 += str(days) + ' дней '
            secs = date2.split(':')[2].split('.')[0] + ' секунд'
            mins = date2.split(':')[1] + ' минут '
            hours = date2.split(':')[0].split(' ')[-1] + ' часов '
            if hours.find('0') == 0:
                hours = hours[1:]
            if mins.find('0') == 0:
                mins = mins[1:]
            if secs.find('0') == 0:
                secs = secs[1:]
            
            
            
            if hours.split(' ')[0] != '0' and hours.split(' ')[0] != '':
                date1 += hours
            if mins.split(' ')[0] != '0' and mins.split(' ')[0] != '':
                date1 += mins
            if secs.split(' ')[0] != '0' and secs.split(' ')[0] != '':
                date1 += secs
            await message.answer(f"""<b>Брак между <a href='tg://user?id={ui1}'>{u1n}</a> и <a href='tg://user?id={ui2}'>{u2n}</a>:</b>

Дата регистрации: {str(date)}
В браке: {date1}
Уровень: {lvl}
XP: {xp} | {(lvl+1) * 1000}""", parse_mode="HTML")
        else:
            await message.answer("Вы не состоите в браке")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()



@dp.message_handler(Text(startswith='Сделать подарок'))
async def profile(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        xt = int(message.text.split(' ')[2])
        if xt == '':
            xt = 1
    except:
        xt = 1
    if xt < 101:
        try:
            c.execute(f"SELECT user_nick, mary, user_freebases FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                un = el[0]
                um = el[1]
                uf = el[2]
            ui = message.from_user.id
            if um != 0:
                c.execute(f"SELECT * FROM mary WHERE user1_id = {um}")
                items = c.fetchall()
                for el in items:
                    u1i = el[0]
                    u2i = el[1]
                    xp = el[3]
                    lvl = el[4]
                if u1i == ui:
                    c.execute(f"SELECT user_id, user_nick FROM user_data WHERE user_id = {u2i}")
                else:
                    c.execute(f"SELECT user_id, user_nick FROM user_data WHERE user_id = {u1i}")
                items = c.fetchall()
                for el in items:
                    pai = el[0]
                    pan = el[1]
                xp_for_next_lvl = (lvl+1) * 1000
                cena = 100
                if cena <= uf:
                    price_lvl = lvl
                    price_freebases = uf
                    price_xp = xp
                    xt1 = xt
                    while xt1 != 0:
                        price_freebases -= cena
                        price_xp += 10
                        if xp_for_next_lvl <= price_xp:
                            price_lvl += 1
                            price_xp -= xp_for_next_lvl
                            xp_for_next_lvl = (lvl+1) * 1000
                        xt1 -= 1
                    c.execute(f"UPDATE mary SET xp = {price_xp}, lvl = {price_lvl} WHERE user1_id = {um}")
                    c.execute(f"UPDATE user_data SET user_freebases = {price_freebases} WHERE user_id = {ui}")
                    if xt != 1:
                        if price_lvl != lvl:
                            await message.answer(f"""<b><a href='tg://user?id={ui}'>{un}</a> подарил(а) {xt} подарков <a href='tg://user?id={pai}'>{pan}</a>!</b>
<b>Потрачено:</b> {uf-price_freebases} фрибасов
<b>Получено XP:</b> {xt*10}

<b>Брак вырос на {price_lvl - lvl} уровень!</b>
<b>Новый уровень брака:</b> {price_lvl}""", parse_mode="HTML")
                        else:
                            await message.answer(f"""<b><a href='tg://user?id={ui}'>{un}</a> подарил(а) {xt} подарков <a href='tg://user?id={pai}'>{pan}</a>!</b>
<b>Потрачено:</b> {uf-price_freebases} фрибасов
<b>Получено XP:</b> {xt*10}""", parse_mode="HTML")
                    else:
                        if price_lvl != lvl:
                            await message.answer(f"""<b><a href='tg://user?id={ui}'>{un}</a> подарил(а) подарок <a href='tg://user?id={pai}'>{pan}</a>!</b>
<b>Потрачено:</b> {uf-price_freebases} фрибасов
<b>Получено XP:</b> {xt*10}

<b>Брак вырос на {price_lvl - lvl} уровень!</b>
<b>Новый уровень брака:</b> {price_lvl}""", parse_mode="HTML")
                        else:
                            await message.answer(f"""<b><a href='tg://user?id={ui}'>{un}</a> подарил(а) подарок <a href='tg://user?id={pai}'>{pan}</a>!</b>
<b>Потрачено:</b> {uf-price_freebases} фрибасов
<b>Получено XP:</b> {xt*10}""", parse_mode="HTML")
                else:
                    await message.answer("Недостаточно средств!")
            else:
                await message.answer("Вы не состоите в браке")
        except:
            await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    else:
        await message.answer("Максимальное количество подарков за раз 100 подарков")
    db.commit()
    db.close()