from aiogram import types
from dispatcher import dp
from random import randint
import sqlite3

@dp.message_handler(text=['+', 'Спасибо', 'Спс', 'Харош', 'Кросс', 'Красава', 'Молодец', 'Лучший', 'Респект', 'Уважение', 'Уважуха', 'Топ', 'спасибо', 'спс', 'харош', 'кросс', 'красава', 'молодец', 'лучший', 'респект', 'уважение', 'уважуха', 'топ'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_nick, user_reputation FROM user_data WHERE user_id = {message.reply_to_message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            ur = el[1]
        if message.from_user.id == message.reply_to_message.from_user.id:
            await message.answer("Ты по-моему перепутал")
            print(forerrorprint)
        price_reputation = ur + 1
        c.execute(f"UPDATE user_data SET user_reputation = {price_reputation} WHERE user_id = {message.reply_to_message.from_user.id}")
        ra = randint(1, 2)
        if ra == 1:
            await message.answer(f"Репутация <a href='tg://user?id={message.reply_to_message.from_user.id}'>{un}</a> защитана!", parse_mode="HTML")
        else:
            await message.answer(f"<a href='tg://user?id={message.reply_to_message.from_user.id}'>{un}</a>, респект!", parse_mode="HTML")
    except:
        pass
    db.commit()
    db.close()

@dp.message_handler(text=['-', 'Фу', 'Бе', 'Плох', 'Кринжанул', 'Кринжанула', 'Кринж', 'фу', 'бе', 'плох', 'кринжанул', 'кринжанула', 'кринж'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_nick, user_reputation FROM user_data WHERE user_id = {message.reply_to_message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            ur = el[1]
        if message.from_user.id == message.reply_to_message.from_user.id:
            await message.answer("Ты по-моему перепутал")
            print(forerrorprint)
        if ur > 0:
            price_reputation = ur - 1
            c.execute(f"UPDATE user_data SET user_reputation = {price_reputation} WHERE user_id = {message.reply_to_message.from_user.id}")
        else:
            await message.answer(f"Репутация <a href='tg://user?id={message.reply_to_message.from_user.id}'>{un}</a> равна 0, репутация не защитана", parse_mode="HTML")
            print(forerrorprint)
        ra = randint(1, 2)
        if message.text.lower() == "кринж" or message.text.lower() == "кринжанул":
            await message.answer(f"<a href='tg://user?id={message.reply_to_message.from_user.id}'>{un}</a> кринжанул(а)...", parse_mode="HTML")
            print(forerrorprint)
        if ra == 1:
            await message.answer(f"Репутация <a href='tg://user?id={message.reply_to_message.from_user.id}'>{un}</a> защитана!", parse_mode="HTML")
        else:
            await message.answer(f"<a href='tg://user?id={message.reply_to_message.from_user.id}'>{un}</a>...", parse_mode="HTML")
    except:
        pass
    db.commit()
    db.close()