from aiogram import types
from dispatcher import dp, bot
import sqlite3
from .db_check import CheckDB
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

check = CheckDB()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    try:
        ub = False
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT user_id FROM black_list WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            ub = True
            await message.answer("Вы забанены!")
            db.commit()
            db.close()
            print(forerrorprint)
        check.add_user(message)
    except:
        try:
            check.update(message)
        except:
            pass
    if ub:
        pass
    else:
        await message.answer(f"""👋 Привет, <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>!

🤖 Я <b>Чапча | Чат-Бот</b>!
😜 Я создан, чтобы развлекать тебя и твоих друзей!

ℹ️ /help - помощь""", parse_mode="HTML")

@dp.message_handler(commands=['help', 'info'])
async def helpp(message: types.Message):
    await message.answer("""<b>Информация о Чапче | Чат-Боте:</b>

Username: @end_soft и conff.org
Создатели: @end_soft и conff.org, @end_soft и conff.org
Новостной канал: @end_soft и conff.org
Игровой чат: @end_soft и conff.org

<b>Что умеет Чапча | Чат-Бот:</b>

-Имеет 5 валют: <b>Очки</b>, <b>Эклеры</b>, <b>Монеты</b>, <b>Чапчи</b>, <b>Фрибасы</b>
-Имеет игры: <b>Кликер</b>, <b>Фарм</b>, <b>Кубик</b>, <b>Дартс</b>, <b>Кража</b>, <b>Кейсы</b>
-Вывести <b>информацию о пользователе</b>
-Имеет <b>рейтинги</b>
-Имеет <b>книгу рецептов</b>
-Имеет <b>пасхалки</b>
-Имеет <b>аукцион ников</b>
-Имеет <b>префиксы</b>
-Имеет <b>кланы</b>
-Имеет <b>работы</b>
-Имеет <b>биржу</b>
-Имеет <b>браки</b>
-Рассказать <b>анекдот</b>

<b>Предупреждения:</b>
-Не спамить коммандами, не кликать быстро в игре <b>КЛИКЕР</b>, бот начинает сильно лагать!
-В чатах бот может работать некоректно, если не выдать ему <b>права администратора</b>
-Бот может работать некоректно, если не зарегистрироваться перед его использованием!
(Введите /start, чтобы зарегистрироваться)

/commands - список команд""", parse_mode="HTML")




@dp.message_handler(text=['Семья Чапчи', 'Семейство Чапчи', 'Семья чапчи', 'Семейство чапчи', 'семья Чапчи', 'семейство Чапчи', 'семья чапчи', 'семейство чапчи'])
async def family(message: types.Message):
    await message.answer("""<b>Семья Чапчи:</b>

Username: @end_soft и conff.org
Задумка: @end_soft и conff.org
Идеи: @end_soft и conff.org, @end_soft и conff.org, @end_soft и conff.org, @end_soft и conff.org, @maend_soft и conff.orgsachist
Аватарки: @end_soft и conff.org, @end_soft и conff.org
Создатели: @end_soft и conff.org, @end_soft и conff.org
Новостной канал: @end_soft и conff.org
Игровой чат: @end_soft и conff.org


Дата релиза    |   Название бота      |    Username бота

В разработке | Чапча | Чат-Бот      | @end_soft и conff.org
21.04.2023        | Чапча | ChatGPT     | @end_soft и conff.org
23.04.2023        | Чапча | Чат-Клоун | @end_soft и conff.org""", parse_mode="HTML")


@dp.message_handler(commands=['ckb'])
async def process_ckb_command(message: types.Message):
    await message.answer("""Фиксики очистили твою клавиатуру от противных кнопок!
Клавиатура чиста!""", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['ban'])
async def process_ckb_command(message: types.Message):
    if message.from_user.id == 1326911178:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        try:
            buid = int(message.text.split(' ')[1])
            prich = message.text[len(str(buid))+6:]
            ubed = False
            if prich == '':
                prich = 'Не указана'
            c.execute(f"SELECT * FROM black_list WHERE user_id = {buid}")
            items = c.fetchall()
            for el in items:
                ubed = True
            if ubed:
                await message.answer("Пользователь уже забанен")
            else:
                c.execute(f"SELECT user_id, user_nick FROM user_data WHERE user_id = {buid}")
                items = c.fetchall()
                for el in items:
                    ui = el[0]
                    un = el[1]
                    cb = True
                try:
                    if cb:
                        c.execute(f"DELETE FROM user_data WHERE user_id = {buid}")
                        try:
                            c.execute(f"DELETE FROM stock_market WHERE user_id = {buid}")
                            c.execute(f"DELETE FROM stock_market_zakaz WHERE user_id = {buid}")
                        except:
                            pass
                        c.execute(f"DELETE FROM purchases WHERE user_id = {buid}")
                        c.execute(f"DELETE FROM nicks_auction WHERE user_id = {buid}")
                        jobs = ['teacher','programmer','killer','farmer','esportsman','developer','caver','builder','bloger','architector']
                        for job in jobs:
                            try:
                                c.execute(f"DELETE FROM job_{job} WHERE worker_id = {buid}")
                            except:
                                pass
                        games = ['stealing','slot_machine','farm','darts','cube','clicker']
                        for game in games:
                            c.execute(f"DELETE FROM game_{game} WHERE user_id = {buid}")
                        try:
                            for i in range(1,501):
                                c.execute(f"UPDATE clan_data SET mb{i} = Null WHERE mb{i} = {buid}")
                            c.execute(f"DELETE FROM clan_events WHERE user_id = {buid}")
                            c.execute(f"DELETE FROM clan_data WHERE leader_id = {buid}")
                        except:
                            pass
                        try:
                            c.execute("INSERT INTO black_list VALUES (?)",
                                      (buid,))
                            await message.answer(f"""<b>Пользователь <a href='tg://user?id={ui}'>{un}</a> забанен!</b>

<b>Причина:</b> {prich}""")
                            await bot.send_message(buid, f"""<b>Вы были забанены!</b>
<b>Причина:</b> {prich}

Если Вы были забанены по ошибке, напишите разработчику: @end_soft и conff.org""", parse_mode="HTML")
                        except:
                            pass
                except:
                    await message.answer("Пользователь не найден")
        except:
            await message.answer("/ban ID Причина")
        db.commit()
        db.close()


@dp.message_handler(commands=['unban'])
async def process_ckb_command(message: types.Message):
    if message.from_user.id == 1326911178:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        try:
            buid = int(message.text.split(' ')[1])
            ubed = True
            c.execute(f"SELECT * FROM black_list WHERE user_id = {buid}")
            items = c.fetchall()
            for el in items:
                ubed = False
            if ubed:
                await message.answer("Пользователь не был забанен")
            else:
                c.execute(f"DELETE FROM black_list WHERE user_id = {buid}")
                await message.answer("Пользователь разбанен!")
                try:
                    await bot.send_message(buid, 'Вас разбанили!')
                except:
                    pass
        except:
            await message.answer("/ban ID Причина")
        db.commit()
        db.close()


@dp.message_handler(commands=['banlist'])
async def process_ckb_command(message: types.Message):
    if True:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        try:
            c.execute(f"SELECT * FROM black_list")
            items = c.fetchall()
            bu = []
            for el in items:
                for e in el:
                    bu.append(e)
            if len(bu) == 0:
                await message.answer("<b>Банлист</b>\n\nСписок пуст", parse_mode="HTML")
            else:
                msg = ''
                for i in bu:
                    msg += str(i) + '\n'
                await message.answer(f"<b>Банлист</b>\n\n{msg}", parse_mode="HTML")
        except:
            pass
        db.commit()
        db.close()


@dp.message_handler(text=['id'])
async def process_ckb_command(message: types.Message):
    if True:
        try:
            try:
                await message.answer(f"ID пользователя: <code>{message.reply_to_message.from_user.id}</code>", parse_mode="HTML")
            except:
                await message.answer(f"ID пользователя: <code>{message.from_user.id}</code>", parse_mode="HTML")
        except:
            pass
