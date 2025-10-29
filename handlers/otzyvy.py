from aiogram import types
from dispatcher import bot, dp
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher.filters import Text
import sqlite3

@dp.message_handler(Text(startswith=['Оставить отзыв', '+Отзыв', 'оставить отзыв', '+отзыв']))
async def commands(message: types.Message):
    if message.text.lower().find('оставить отзыв') == 0:
        text = message.text[15:]
    else:
        text = message.text[7:]
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    if text != '':
        if len(text) <= 250:
            try:
                c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    un = el[0]
                    ui = message.from_user.id
                try:
                    c.execute("INSERT INTO otzyvy VALUES (?, ?, ?)",
                              (ui, None, text))
                    await message.answer(f"<b><a href='tg://user?id={ui}'>{un}</a></b> оставил отзыв!", parse_mode="HTML")
                    await bot.send_message(1326911178, f"<b><a href='tg://user?id={ui}'>{un}</a></b> оставил отзыв!\n\n{text}", parse_mode="HTML")
                except:
                    c.execute(f"UPDATE otzyvy SET text_otzyva = '{text}' WHERE user_id = {ui}")
                    await message.answer(f"<b><a href='tg://user?id={ui}'>{un}</a></b> изменил отзыв!", parse_mode="HTML")
                    await bot.send_message(1326911178, f"<b><a href='tg://user?id={ui}'>{un}</a></b> изменил отзыв!\n\n{text}", parse_mode="HTML")
            except:
                await message.answer('Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота')
        else:
            await message.answer("Максимальная длина отзыва 250 символов!")
    else:
        await message.answer("Оставить отзыв Текст")
    db.commit()
    db.close()

@dp.message_handler(text=['Оставить оценку', '+Оценка', 'Оценить Чапчу', 'Оценить чапчу', 'оставить оценку', '+оценка', 'оценить Чапчу', 'оценить чапчу'])
async def commands(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    if True:
        try:
            c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                un = el[0]
            ui = message.from_user.id
            try:
                floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = InlineKeyboardButton("⭐️", callback_data=f'ocenka:1:{ui}')
                btn2 = InlineKeyboardButton("⭐️⭐️", callback_data=f'ocenka:2:{ui}')
                btn3 = InlineKeyboardButton("⭐️⭐️⭐️", callback_data=f'ocenka:3:{ui}')
                btn4 = InlineKeyboardButton("⭐️⭐️⭐️⭐️", callback_data=f'ocenka:4:{ui}')
                btn5 = InlineKeyboardButton("⭐️⭐️⭐️⭐️⭐️", callback_data=f'ocenka:5:{ui}')
                floor.add(btn5).add(btn4)
                floor.add(btn3).add(btn2)
                floor.add(btn1)
                await message.answer(f"<b><a href='tg://user?id={ui}'>{un}</a></b>, оцените Чапчу, пожалуйста! :3", parse_mode="HTML", reply_markup=floor)
            except:
                print(a)
        except:
            await message.answer('Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота')
    db.commit()
    db.close()

@dp.callback_query_handler(Text(startswith=['ocenka']))
async def back_to_commands(call: types.CallbackQuery):
    ocenka = int(call.data.split(':')[1])
    ci = int(call.data.split(':')[2])
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    if ci == call.from_user.id:
        try:
            c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {ci}")
            items = c.fetchall()
            for el in items:
                un = el[0]
                cc = True
            if cc:
                try:
                    c.execute('INSERT INTO otzyvy VALUES (?, ?, ?)',
                              (ci, ocenka, None))
                except:
                    c.execute(f'UPDATE otzyvy SET ocenka = {ocenka} WHERE user_id = {ci}')
                if ocenka == 1:
                    await call.message.edit_text('<b>Очень жаль</b>, что Вам не понравился бот.\n\n Вы можете <b>оставить отзыв</b> о проблеме.\n\nОставить отзыв Текст - оставить отзыв', parse_mode="HTML")
                elif ocenka == 2:
                    await call.message.edit_text('<b>Очень жаль</b>, что Вам не понравился бот.\n\nВы можете <b>оставить отзыв</b> о проблеме.\n\nОставить отзыв Текст - оставить отзыв', parse_mode="HTML")
                elif ocenka == 3:
                    await call.message.edit_text('<b>Благодарим за оценку!</b>\n\nМы будем рады, если Вы <b>оставите отзыв</b> о проблеме.\n\nОставить отзыв Текст - оставить отзыв', parse_mode="HTML")
                elif ocenka == 4:
                    await call.message.edit_text('<b>Благодарим за оценку!</b>\n\nМы очень рады, что Вам понравился бот, Вы также можете <b>посоветовать Чапчу друзьям</b> или <b>оставить отзыв</b>!\n\nОставить отзыв Текст - оставить отзыв', parse_mode="HTML")
                else:
                    await call.message.edit_text('<b>Благодарим за оценку!</b>\n\nМы очень рады, что Вам понравился бот, Вы также можете <b>посоветовать Чапчу друзьям</b> или <b>оставить отзыв</b>!\n\nОставить отзыв Текст - оставить отзыв', parse_mode="HTML")
                await bot.send_message(1326911178, f"<b><a href='tg://user?id={ci}'>{un}</a></b> оценил бота!\n\n<b>Оценка:</b> {ocenka}", parse_mode="HTML")
        except:
            await call.message.edit_text('Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота')
    else:
        await call.answer("Эта кнопочка не для тебя!")
    db.commit()
    db.close()

@dp.message_handler(text=['Удалить отзыв', '-Отзыв', 'удалить отзыв', '-отзыв'])
async def commands(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            ui = message.from_user.id
        try:
            c.execute(f"UPDATE otzyvy SET text_otzyva = Null WHERE user_id = {message.from_user.id}")
            await message.answer(f"<b><a href='tg://user?id={ui}'>{un}</a></b> удалил отзыв!", parse_mode="HTML")
        except:
            pass
    except:
        await message.answer('Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота')
    db.commit()
    db.close()

@dp.message_handler(text=['Удалить оценку', '-Оценка', 'удалить оценку', '-оценка'])
async def commands(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            ui = message.from_user.id
        try:
            c.execute(f"UPDATE otzyvy SET ocenka = Null WHERE user_id = {message.from_user.id}")
            await message.answer(f"<b><a href='tg://user?id={ui}'>{un}</a></b> удалил оценку!", parse_mode="HTML")
        except:
            pass
    except:
        await message.answer('Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота')
    db.commit()
    db.close()

@dp.message_handler(text=['Мой отзыв', 'Моя оценка', '!Отзыв', '!Оценка', 'мой отзыв', 'моя оценка', '!отзыв', '!оценка'])
async def commands(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            ui = message.from_user.id
        try:
            c.execute(f"SELECT * FROM otzyvy WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                uo = el[1]
                uto = el[2]
            try:
                if uto == '' or uto == None:
                    uto = 'Отсутствует'
            except:
                uto = 'Отсутствует'
            
            
            try:
                if uo == '' or uo == None:
                    uo = 'Отсутствует'
                    uoc = 'Отсутствует'
            except:
                uo = 'Отсутствует'
                uoc = 'Отсутствует'
            try:
                uoc = ''
                for i in range(uo):
                    uoc += '⭐️'
            except:
                uoc = 'Отсутствует'
            await message.answer(f"""<b>Отзыв <a href='tg://user?id={ui}'>{un}</a>:</b>

<b>Оценка:</b> {uoc} | {uo}
<b>Отзыв:</b> {uto}""", parse_mode="HTML")
        except:
            pass
    except:
        await message.answer('Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота')
    db.commit()
    db.close()

@dp.message_handler(text=['Оценка Чапчи', 'Стата Чапчи', 'Оценка чапчи', 'Стата чапчи', 'Средний балл Чапчи', 'Средний балл чапчи', 'оценка Чапчи', 'стата Чапчи', 'оценка чапчи', 'стата чапчи', 'средний балл Чапчи', 'средний балл чапчи'])
async def commands(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute("SELECT ocenka FROM otzyvy")
        items = c.fetchall()
        ocenki = []
        for el in items:
            for e in el:
                ocenki.append(e)
        suma = 0
        for el in ocenki:
            suma += el
        sroc = round(suma/len(ocenki), 2)
        stars = ''
        for i in range(round(sroc)):
            stars += '⭐️'
        await message.answer(f"""<b>Средняя оценка Чапчи:</b>

{sroc} баллов
{stars}""", parse_mode='HTML')
    except:
        pass
    db.commit()
    db.close()