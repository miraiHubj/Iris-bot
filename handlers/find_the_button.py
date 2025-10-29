from aiogram import types
from dispatcher import bot, dp
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher.filters import Text
from random import randint as ran
import asyncio
import sqlite3

@dp.message_handler(text=['!Кнопки', '!Кнопка', 'Поиск кнопки', 'Кнопки игра', 'Игра кнопки', 'Кнопка игра', 'Игра кнопка', 'Найди кнопку', 'Найти кнопку', '!кнопки', '!кнопка', 'поиск кнопки', 'кнопки игра', 'игра кнопки', 'кнопка игра', 'игра кнопка', 'найди кнопку', 'найти кнопку'])
async def process_start_command(message: types.Message):
    ui = message.from_user.id
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        easy = InlineKeyboardButton('😀 Легко | 4x4', callback_data=f'btngame:easy:{ui}')
        normal = InlineKeyboardButton('🙂 Нормально | 5x5', callback_data=f'btngame:normal:{ui}')
        hard = InlineKeyboardButton('😕 Сложно | 6x6', callback_data=f'btngame:hard:{ui}')
        insane = InlineKeyboardButton('😡 Безумно | 7x7', callback_data=f'btngame:insane:{ui}')
        impossible = InlineKeyboardButton('👿 Невозможно | 8x8', callback_data=f'btngame:impossible:{ui}')
        floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).row(easy, normal).row(hard, insane).add(impossible)
        c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {ui}")
        items = c.fetchall()
        for el in items:
            un = el[0]
        await message.answer(f"<b><a href='tg://user?id={ui}'>{un}</a> выберите сложность</b>", parse_mode="HTML", reply_markup=floor)
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()


@dp.callback_query_handler(Text(startswith=['nextbtngame']))
async def process_auction_command(call: types.CallbackQuery):
    ui = int(call.data.split(':')[1])
    if ui == call.from_user.id:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        try:
            easy = InlineKeyboardButton('😀 Легко | 4x4', callback_data=f'btngame:easy:{ui}')
            normal = InlineKeyboardButton('🙂 Нормально | 5x5', callback_data=f'btngame:normal:{ui}')
            hard = InlineKeyboardButton('😕 Сложно | 6x6', callback_data=f'btngame:hard:{ui}')
            insane = InlineKeyboardButton('😡 Безумно | 7x7', callback_data=f'btngame:insane:{ui}')
            impossible = InlineKeyboardButton('👿 Невозможно | 8x8', callback_data=f'btngame:impossible:{ui}')
            floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).row(easy, normal).row(hard, insane).add(impossible)
            c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {ui}")
            items = c.fetchall()
            for el in items:
                un = el[0]
            await call.message.edit_text(f"<b><a href='tg://user?id={ui}'>{un}</a> выберите сложность</b>", parse_mode="HTML", reply_markup=floor)
        except:
            await call.message.edit_text("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
        db.commit()
        db.close()
    else:
        await call.answer("Это не твоя кнопка!")





@dp.callback_query_handler(Text(startswith=['btngame']))
async def process_auction_command(call: types.CallbackQuery):
    ui = int(call.data.split(':')[2])
    diff = call.data.split(':')[1]
    tryes = 0
    if ui == call.from_user.id:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        try:
            c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {ui}")
            items = c.fetchall()
            for el in items:
                un = el[0]
            if diff == 'easy':
                btns = 4
            elif diff == 'normal':
                btns = 5
            elif diff == 'hard':
                btns = 6
            elif diff == 'insane':
                btns = 7
            else:
                btns = 8
            price = btns**4-(tryes*10)
            if price < 1:
                price = 0
            rbtn = ran(1,(btns**2)-1)
            btnl = []
            nums = []
            for i in range(btns**2):
                nums.append(i)
            floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=btns)
            for x in range(btns):
                for y in range(btns):
                    if x*btns+y == rbtn:
                        btn = InlineKeyboardButton('⚪️', callback_data=f'rbtn:{diff}:{ui}:{tryes+1}:{rbtn}')
                    else:
                        btn = InlineKeyboardButton('⚪️', callback_data=f'drbtn:{diff}:{ui}:{tryes+1}:{rbtn}:{nums[0]}')
                        nums.remove(nums[0])
                    btnl.append(btn)
                floor.row(*[button for button in btnl])
                btnl = []
            if diff == 'easy':
                btns = '😀 Легко'
            elif diff == 'normal':
                btns = '🙂 Нормально'
            elif diff == 'hard':
                btns = '😕 Сложно'
            elif diff == 'insane':
                btns = '😡 Безумно'
            else:
                btns = '👿 Невозможно'
            await call.message.edit_text(f"<b><a href='tg://user?id={ui}'>{un}</a> найди правильную кнопку!\nСложность: {btns}\nПопытки: {tryes}\nНаграда: {price} очков</b>", parse_mode="HTML", reply_markup=floor)
        except:
            pass
        db.commit()
        db.close()
    else:
        await call.answer("Позволь человеку сделать выбор!")

@dp.callback_query_handler(Text(startswith=['rbtn']))
async def process_auction_command(call: types.CallbackQuery):
    ui = int(call.data.split(':')[2])
    diff = call.data.split(':')[1]
    tryes = int(call.data.split(':')[3])
    rbtn = int(call.data.split(':')[4])
    if ui == call.from_user.id:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        try:
            c.execute(f"SELECT user_nick, user_points FROM user_data WHERE user_id = {ui}")
            items = c.fetchall()
            for el in items:
                un = el[0]
                up = el[1]
            if diff == 'easy':
                btns = 4
            elif diff == 'normal':
                btns = 5
            elif diff == 'hard':
                btns = 6
            elif diff == 'insane':
                btns = 7
            else:
                btns = 8
            price = btns**4-(tryes*10)
            if price < 1:
                price = 0
            btnl = []
            floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=btns)
            for x in range(btns):
                for y in range(btns):
                    if x*btns+y == rbtn:
                        btn = InlineKeyboardButton('🟢', callback_data=f'pusto')
                    else:
                        btn = InlineKeyboardButton('⚪️', callback_data=f'pusto')
                    btnl.append(btn)
                floor.row(*[button for button in btnl])
                btnl = []
            if diff == 'easy':
                btns = '😀 Легко'
            elif diff == 'normal':
                btns = '🙂 Нормально'
            elif diff == 'hard':
                btns = '😕 Сложно'
            elif diff == 'insane':
                btns = '😡 Безумно'
            else:
                btns = '👿 Невозможно'
            price_points = up + price
            c.execute(f"UPDATE user_data SET user_points = {price_points} WHERE user_id = {ui}")
            db.commit()
            db.close()
            nextgame = InlineKeyboardButton('Следующая игра', callback_data=f'nextbtngame:{ui}')
            await call.message.edit_text(f"<b><a href='tg://user?id={ui}'>{un}</a> нашел правильную кнопку!\nСложность: {btns}\nПопытки: {tryes}\nНаграда: {price} очков</b>", parse_mode="HTML", reply_markup=floor)
            await asyncio.sleep(10)
            floor = InlineKeyboardMarkup(resize_keyboard=True).add(nextgame)
            await call.message.edit_text(f"<b><a href='tg://user?id={ui}'>{un}</a> нашел правильную кнопку!\nСложность: {btns}\nПопытки: {tryes}\nНаграда: {price} очков</b>", parse_mode="HTML", reply_markup=floor)
        except:
            pass
        try:
            db.commit()
            db.close()
        except:
            pass
    else:
        await call.answer("Не трогай чужие кнопки!")

@dp.callback_query_handler(Text(startswith=['drbtn']))
async def process_auction_command(call: types.CallbackQuery):
    ui = int(call.data.split(':')[2])
    diff = call.data.split(':')[1]
    tryes = int(call.data.split(':')[3])
    rbtn = int(call.data.split(':')[4])
    if ui == call.from_user.id:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        try:
            c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {ui}")
            items = c.fetchall()
            for el in items:
                un = el[0]
            if diff == 'easy':
                btns = 4
            elif diff == 'normal':
                btns = 5
            elif diff == 'hard':
                btns = 6
            elif diff == 'insane':
                btns = 7
            else:
                btns = 8
            price = btns**4-(tryes*10)
            if price < 1:
                price = 0
            btnl = []
            nums = []
            for i in range(btns**2):
                nums.append(i)
            floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=btns)
            for x in range(btns):
                for y in range(btns):
                    if x*btns+y == rbtn:
                        btn = InlineKeyboardButton('⚪️', callback_data=f'rbtn:{diff}:{ui}:{tryes+1}:{rbtn}')
                    else:
                        btn = InlineKeyboardButton('⚪️', callback_data=f'drbtn:{diff}:{ui}:{tryes+1}:{rbtn}:{nums[0]}')
                        nums.remove(nums[0])
                    btnl.append(btn)
                floor.row(*[button for button in btnl])
                btnl = []
            if diff == 'easy':
                btns = '😀 Легко'
            elif diff == 'normal':
                btns = '🙂 Нормально'
            elif diff == 'hard':
                btns = '😕 Сложно'
            elif diff == 'insane':
                btns = '😡 Безумно'
            else:
                btns = '👿 Невозможно'
            await call.message.edit_text(f"<b><a href='tg://user?id={ui}'>{un}</a> найди правильную кнопку!\nСложность: {btns}\nПопытки: {tryes}\nНаграда: {price} очков</b>", parse_mode="HTML", reply_markup=floor)
        except:
            pass
        db.commit()
        db.close()
    else:
        await call.answer("Не трогай чужие кнопки!")