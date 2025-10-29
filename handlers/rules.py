from aiogram import types
from dispatcher import dp, bot
import sqlite3

@dp.message_handler(commands=['правила', 'Правила'], commands_prefix="+")
async def add_rules(message: types.Message):
    if message.chat.type != 'private':
        try:
            db = sqlite3.connect('chapcha_data_base.db')
            c = db.cursor()
            c.execute("INSERT INTO chat_data VALUES (?, ?, ?, ?, ?)",
                      (message.chat.id, '<b>- {имя} добро пожаловать в чат!</b>', '', '1', 'NO'))
            db.commit()
            db.close()
        except:
            pass
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        try:
            rules = message.text[8:]
            if rules.find(" ") == 0:
                rules = rules[1:]
            c.execute(f"UPDATE chat_data SET chat_rules = '{rules}' WHERE chat_id = {message.chat.id}")
            await message.answer("✅ Правила установлены!")
        except:
            await message.answer("+правила Текст")
        db.commit()
        db.close()
    else:
        await message.answer("Правила недоступны в лс Чапчи")

@dp.message_handler(commands=['правила', 'Правила'], commands_prefix="-")
async def del_rules(message: types.Message):
    if message.chat.type != 'private':
        try:
            db = sqlite3.connect('chapcha_data_base.db')
            c = db.cursor()
            c.execute("INSERT INTO chat_data VALUES (?, ?, ?, ?, ?)",
                      (message.chat.id, '<b>- {имя} добро пожаловать в чат!</b>', '', '1', 'NO'))
            db.commit()
            db.close()
        except:
            pass
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        gc = True
        try:
            c.execute(f"UPDATE chat_data SET chat_rules = '' WHERE chat_id = {message.chat.id}")
            await message.answer("❎ Правила удалены!")
        except:
            pass
        db.commit()
        db.close()
    else:
        await message.answer("Правила недоступны в лс Чапчи")

@dp.message_handler(commands=['правила', 'Правила'], commands_prefix="!")
async def rules(message: types.Message):
    if message.chat.type != 'private':
        try:
            db = sqlite3.connect('chapcha_data_base.db')
            c = db.cursor()
            c.execute("INSERT INTO chat_data VALUES (?, ?, ?, ?, ?)",
                      (message.chat.id, '<b>- {имя} добро пожаловать в чат!</b>', '', '1', 'NO'))
            db.commit()
            db.close()
        except:
            pass
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        gc = True
        try:
            c.execute(f"SELECT chat_rules FROM chat_data WHERE chat_id = {message.chat.id}")
            items = c.fetchall()
            for el in items:
                rules = el[0]
            if rules == '':
                await message.answer("🗓 Правила отсутствуют")
            else:
                await message.answer(f"""<b>🗓 Правила:</b>
    {rules}""", parse_mode="HTML")
        except:
            pass
        db.commit()
        db.close()
    else:
        await message.answer("Правила недоступны в лс Чапчи")