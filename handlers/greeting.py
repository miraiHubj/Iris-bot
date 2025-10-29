from aiogram import types
from dispatcher import dp, bot
import sqlite3

@dp.message_handler(text=['установка приветствия', 'Установка приветствия', 'установка приветствий', 'Установка приветствий'])
async def greeting_installing(message: types.Message):
    await message.answer(f"""Полная инструкция по установке приветствия тут:
https://teletype.in/@chapcha_chat_bot/0j0tYX6ne2Z""")



@dp.message_handler(commands=['приветствие', 'Приветствие'], commands_prefix="+")
async def add_greeting(message: types.Message):
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
            com = message.text[13:]
            img = com.split(' ')[-1]
            lll = len(img) + 1
            text = com[:-lll]
            c.execute(f"UPDATE chat_data SET chat_welcome_text = '{text}', chat_welcome_image = '{img}' WHERE chat_id = {message.chat.id}")
            await message.answer("✅ Приветствие установлено!")
        except:
            await message.answer("+приветствие Текст Число/Ссылка")
        db.commit()
        db.close()
    else:
        await message.answer("Приветствия недоступны в лс Чапчи")

@dp.message_handler(commands=['приветствие', 'Приветствие'], commands_prefix="-")
async def del_greeting(message: types.Message):
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
            c.execute(f"UPDATE chat_data SET chat_welcome_text = 'Отсутствует', chat_welcome_image = '0' WHERE chat_id = {message.chat.id}")
            await message.answer("❎ Приветствие удалено!")
        except:
            pass
        db.commit()
        db.close()
    else:
        await message.answer("Приветствия недоступны в лс Чапчи")

@dp.message_handler(commands=['приветствие', 'Приветствие', ' приветствие', ' Приветствие'], commands_prefix="!./")
async def greeting(message: types.Message):
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
            c.execute(f"SELECT chat_welcome_text, chat_rules, chat_welcome_image FROM chat_data WHERE chat_id = {message.chat.id}")
            items = c.fetchall()
            for el in items:
                cwt = el[0]
                cr = el[1]
                cwi = el[2]
            if cwi == '0' and cwt != "Отсутствует":
                await message.answer(cwt, parse_mode="HTML")
                gc = False
            elif cwi == '1':
                img_url = 'https://img1.ak.crunchyroll.com/i/spire3/cc64cf60916d204eb6cd3ec742ae38b71252551583_full.jpg'
            elif cwi == '2':
                img_url = 'http://s.myniceprofile.com/myspacepic/909/90920.jpg'
            elif cwi == '3':
                img_url = 'https://cdn.freelance.ru/images/att/1579769_900_600.png'
            elif cwi == '4':
                img_url = 'https://ctot.com/wp-content/uploads/2016/01/fotolia_76080180_subscription_monthly_xl.jpg'
            elif cwi == '5':
                img_url = 'http://pm1.narvii.com/7948/d035c3216cb81e31ec4380e4d13ceae1118c7f2cr1-2048-865v2_uhq.jpg'
            elif cwi == '6':
                img_url = 'https://i.ytimg.com/vi/IM7PYAStyjw/maxresdefault.jpg'
            elif cwi == '7':
                img_url = 'https://mir-s3-cdn-cf.behance.net/project_modules/2800_opt_1/96930236573563.57211c38a6841.jpg'
            elif cwi == '8':
                img_url = 'https://4kwallpapers.com/images/wallpapers/welcome-neon-glow-dark-background-glowing-3600x2000-2068.jpg'
            elif cwi == '9':
                img_url = 'https://pbs.twimg.com/profile_banners/4841155222/1453619786/1500x500'
            elif cwi == '10':
                img_url = 'https://s1.hostingkartinok.com/uploads/images/2012/04/ea7e2ee279e16051c463010d1f4ce037.png'
            elif cwi == '11':
                img_url = 'https://ap-portal.my1.ru/_nw/0/47213261.jpg'
            elif cwi == '12':
                img_url = 'https://pa1.narvii.com/6918/3f75fd77e1fbd278f0d9d4d097fd09558ce0a9b2r1-600-365_hq.gif'
            elif cwi == '13':
                img_url = 'https://i.pinimg.com/originals/1b/d4/3f/1bd43f8955527be68a0ada8cd6845523.jpg'
            elif cwi == '14':
                img_url = 'https://pbs.twimg.com/profile_banners/586446592/1454674127/1500x500'
            elif cwi == '15':
                img_url = 'https://sun9-35.userapi.com/impf/Ytem8H75RIunMhVEB5x8r48WGNZu299om5UaeA/0WVrQMMbDpk.jpg?size=1818x606&quality=95&crop=0,0,1500,500&sign=b41e82a1a1b8ce6460b1d3b19a82fefa&type=cover_group'
            else:
                img_url = cwi
            if gc and cwt != "Отсутствует":
                try:
                    await message.answer(f"🗓 Приветствие:<a href='{img_url}'> </a>\n{cwt}", parse_mode="HTML")
                except:
                    await message.answer(f"🗓 Приветствие:\n{cwt}")
            elif gc and cwt == "Отсутствует":
                await message.answer("🗓 Приветствие отсутствует")
        except:
            await message.answer("Пропишите эту команду в группе с ботом")
        db.commit()
        db.close()
    else:
        await message.answer("Приветствия недоступны в лс Чапчи")