from aiogram import types
from dispatcher import dp
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery
import sqlite3

@dp.message_handler(commands=['bad_words'])
async def process_giveeclairs_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT chat_bad_words FROM chat_data WHERE chat_id = {message.chat.id}")
        items = c.fetchall()
        for el in items:
            bw = el[0]
        if bw == 'NO':
            turn = InlineKeyboardButton("✅ Включить", callback_data='turnonbadwords')
            floor = InlineKeyboardMarkup().add(turn)
            await message.answer("🤬 Ответы на плохие слова: <b>❎ Отключено</b>", parse_mode="HTML", reply_markup=floor)
        else:
            turn = InlineKeyboardButton("❎ Выключить", callback_data='turnoffbadwords')
            floor = InlineKeyboardMarkup().add(turn)
            await message.answer("🤬 Ответы на плохие слова: <b>✅ Включено</b>", parse_mode="HTML", reply_markup=floor)
    except:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute("INSERT INTO chat_data VALUES (?, ?, ?, ?, ?)",
                  (message.chat.id, '<b>- {имя} добро пожаловать в чат!</b>', '', '1', 'NO'))
        db.commit()
        db.close()

@dp.callback_query_handler(text=['turnonbadwords'])
async def turn_on_bad_words(call: types.CallbackQuery):
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"UPDATE chat_data SET chat_bad_words = 'YES' WHERE chat_id = {call.message.chat.id}")
        db.commit()
        db.close()
        turn = InlineKeyboardButton("❎Выключить", callback_data='turnoffbadwords')
        floor = InlineKeyboardMarkup().add(turn)
        await call.message.edit_text("🤬 Ответы на плохие слова: <b>✅ Включено</b>", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['turnoffbadwords'])
async def turn_on_bad_words(call: types.CallbackQuery):
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"UPDATE chat_data SET chat_bad_words = 'NO' WHERE chat_id = {call.message.chat.id}")
        db.commit()
        db.close()
        turn = InlineKeyboardButton("✅ Включить", callback_data='turnonbadwords')
        floor = InlineKeyboardMarkup().add(turn)
        await call.message.edit_text("🤬 Ответы на плохие слова: <b>❎Отключено</b>", parse_mode="HTML", reply_markup=floor)



@dp.message_handler(text=['Иди нахуй', 'Иди нaхуй', 'Иди наxуй', 'Иди нахyй', 'Иди нaxуй', 'Иди нaхyй', 'Иди нaxyй', 'Иди наxyй', 'Иди нахцй', 'иди нахуй', 'иди нaхуй', 'иди наxуй', 'иди нахyй', 'иди нaxуй', 'иди нaхyй', 'иди наxyй', 'иди нaxyй', 'иди нахцй'])
async def process_giveeclairs_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT chat_bad_words FROM chat_data WHERE chat_id = {message.chat.id}")
        items = c.fetchall()
        for el in items:
            allow_bad_words = el[0]
        if allow_bad_words == 'YES':
            await message.answer("Иди нахуй, ебанашка обоссаная")
        db.commit()
        db.close()
    except:
        pass

@dp.message_handler(text=['Стрелочник', 'стрелочник'])
async def process_giveeclairs_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT chat_bad_words FROM chat_data WHERE chat_id = {message.chat.id}")
        items = c.fetchall()
        for el in items:
            allow_bad_words = el[0]
        if allow_bad_words == 'YES':
            await message.answer("Стрелочник с твоей мамкой в канаве балуется")
        db.commit()
        db.close()
    except:
        pass

@dp.message_handler(text=['Слитый бот', 'слитый бот'])
async def process_giveeclairs_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT chat_bad_words FROM chat_data WHERE chat_id = {message.chat.id}")
        items = c.fetchall()
        for el in items:
            allow_bad_words = el[0]
        if allow_bad_words == 'YES':
            await message.answer("Сказала смытая коженка")
        db.commit()
        db.close()
    except:
        pass

@dp.message_handler(text=['Хуесос', 'хуесос'])
async def process_giveeclairs_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT chat_bad_words FROM chat_data WHERE chat_id = {message.chat.id}")
        items = c.fetchall()
        for el in items:
            allow_bad_words = el[0]
        if allow_bad_words == 'YES':
            await message.answer("Хуесос твоей мамы сын")
        db.commit()
        db.close()
    except:
        pass

@dp.message_handler(text=['Пидор', 'пидор'])
async def process_giveeclairs_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT chat_bad_words FROM chat_data WHERE chat_id = {message.chat.id}")
        items = c.fetchall()
        for el in items:
            allow_bad_words = el[0]
        if allow_bad_words == 'YES':
            await message.answer("Пидор твой отчим, который шпехает тебя во все щели каждую ночь")
        db.commit()
        db.close()
    except:
        pass

@dp.message_handler(text=['Бот говно', 'Чапча говно', 'бот говно', 'чапча говно', 'Бот хуйня', 'Чапча хуйня', 'бот хуйня', 'чапча хуйня'])
async def process_giveeclairs_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT chat_bad_words FROM chat_data WHERE chat_id = {message.chat.id}")
        items = c.fetchall()
        for el in items:
            allow_bad_words = el[0]
        if allow_bad_words == 'YES':
            await message.answer("Сказал обосраный чмошник")
        db.commit()
        db.close()
    except:
        pass

@dp.message_handler(text=['Чмо', 'Чмошник', 'чмо', 'чмошник'])
async def process_giveeclairs_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT chat_bad_words FROM chat_data WHERE chat_id = {message.chat.id}")
        items = c.fetchall()
        for el in items:
            allow_bad_words = el[0]
        if allow_bad_words == 'YES':
            await message.answer(f'"Я ебаное чмо" - последние слова <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>', parse_mode="HTML")
        db.commit()
        db.close()
    except:
        pass

@dp.message_handler(text=['Пизда', 'пизда', 'Пиз', 'пиз'])
async def process_giveeclairs_command(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT chat_bad_words FROM chat_data WHERE chat_id = {message.chat.id}")
        items = c.fetchall()
        for el in items:
            allow_bad_words = el[0]
        if allow_bad_words == 'YES':
            await message.answer(f'Твоей матери')
        db.commit()
        db.close()
    except:
        pass

@dp.message_handler(text=['Заебал', 'заебал'])
async def process_giveeclairs_command(message: types.Message):
    await message.answer("Какие-то проблемы?")

@dp.message_handler(text=['Чапча урыл', 'Чапча урил', 'чапча урыл', 'чапча урил'])
async def process_giveeclairs_command(message: types.Message):
    await message.answer("Да, я такой")

@dp.message_handler(text=['Урыл', 'Урил', 'урыл', 'урил'])
async def process_giveeclairs_command(message: types.Message):
    await message.answer("Еще как")