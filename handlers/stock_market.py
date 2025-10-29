from aiogram import types
from dispatcher import bot, dp
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher.filters import Text
import sqlite3

@dp.message_handler(text=['Команды биржи', 'Биржа команды', 'Биржа комы', 'команды биржи', 'биржа команды', 'биржа комы'])
async def process_giveeclairs_command(message: types.Message):
    await message.answer("""<b>Команды биржи:</b>

Биржа - биржа
Продать чапчи Число Цена (за все) - продать чапчи
Купить чапчи ID - купить чапчи
Заказать чапчи Число Цена (за 1 чапчу) - заказать чапчи
Мой заказ - просмотреть заказ
Биржа снять - убрать чапчи с биржи
Заказ снять - удалить заказ""", parse_mode="HTML")






@dp.message_handler(Text(startswith=['Продать чапчи', 'Пополнить биржу', 'Пополнить рынок', 'продать чапчи', 'пополнить биржу', 'пополнить рынок']))
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        chn = int(message.text.split(' ')[2])
        cena = int(message.text.split(' ')[3])
        ui = message.from_user.id
        try:
            c.execute(f"SELECT user_chapchas FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                uch = el[0]
            if uch >= chn:
                if chn > 0:
                    if cena <= 1000000000000000 and cena > 1000000:
                        try:
                            c.execute("INSERT INTO stock_market VALUES (?, ?, ?)",
                                      (message.from_user.id, chn, cena))
                        except:
                            c.execute(f"UPDATE stock_market SET chapchas = {chn}, cena = {cena} WHERE user_id = {message.from_user.id}")
                        c.execute(f"UPDATE user_data SET user_chapchas = {uch - chn} WHERE user_id = {message.from_user.id}")
                        await message.answer("Чапчи выставлены на продажу!")
                        try:
                            scenafo = round(cena/chn)
                            c.execute(f"SELECT * FROM stock_market_zakaz WHERE cena >= {scenafo} ORDER BY cena DESC")
                            items = c.fetchall()
                            noi = 0
                            itemsis = []
                            for el in items:
                                for e in el:
                                    itemsis.append(e)
                                    noi += 1
                            if noi != 0:
                                c.execute(f"SELECT user_prefix, user_nick, user_chapchas, user_freebases FROM user_data WHERE user_id = {ui}")
                                items = c.fetchall()
                                for el in items:
                                    up = el[0]
                                    un = el[1]
                                    uch = el[2]
                                    uf = el[3]
                                price_chapchas_for_buyer = 0
                                price_freebases_for_buyer = 0
                                price_freebases_for_seller = 0
                                price_chapchas_for_market = 0
                                price_cena_for_market = 0
                                stop = False
                                for tovar in itemsis:
                                    if stop:
                                        break
                                    c.execute(f"SELECT * FROM stock_market_zakaz WHERE user_id = {tovar}")
                                    items = c.fetchall()
                                    for el in items:
                                        bi = el[0]
                                        bch = el[1]
                                        bcena = el[2]
                                    c.execute(f"SELECT user_prefix, user_nick, user_chapchas, user_freebases FROM user_data WHERE user_id = {tovar}")
                                    items = c.fetchall()
                                    for el in items:
                                        bpp = el[0]
                                        bnp = el[1]
                                        bchp = el[2]
                                        bfrp = el[3]
                                    scenafo = round(cena/chn)
                                    if bfrp >= scenafo:
                                        if scenafo > cena:
                                            break
                                        for i in range(1,bch+1):
                                            price_chapchas_for_buyer = i
                                            price_freebases_for_buyer += scenafo
                                            price_freebases_for_seller += scenafo
                                            price_chapchas_for_market = i
                                            price_cena_for_market += scenafo
                                            if bfrp - price_freebases_for_buyer < 0 or chn - price_chapchas_for_buyer == 0:
                                                if chn == price_chapchas_for_buyer:
                                                    c.execute(f"DELETE FROM stock_market WHERE user_id = {tovar}")
                                                stop = True
                                                break
                                        c.execute(f"UPDATE user_data SET user_chapchas = {bchp + price_chapchas_for_buyer}, user_freebases = {bfrp - price_freebases_for_buyer} WHERE user_id = {tovar}")
                                        c.execute(f"UPDATE user_data SET user_freebases = {uf + price_freebases_for_seller} WHERE user_id = {ui}")
                                        c.execute(f"UPDATE stock_market SET chapchas = {chn - price_chapchas_for_market}, cena = {round(cena - price_cena_for_market)} WHERE user_id = {ui}")
                                        c.execute(f"UPDATE stock_market_zakaz SET chapchas = {bch - price_chapchas_for_market} WHERE user_id = {tovar}")
                                        await message.answer(f"Пользователь <b><i>[{bpp}]</i> <a href='tg://user?id={tovar}'>{bnp}</a></b> купил {price_chapchas_for_market} чапчей за {price_freebases_for_seller} фрибасов!", parse_mode="HTML")
                                        try:
                                            await bot.send_message(tovar, f"Пользователь <b><i>[{up}]</i> <a href='tg://user?id={ui}'>{un}</a></b> продал {price_chapchas_for_market} чапчей за {price_freebases_for_seller} фрибасов!", parse_mode="HTML")
                                        except:
                                            pass
                                        print(bfrp - (bch * bcena))
                                        if bch == price_chapchas_for_buyer or bfrp - (bch * bcena) < 0:
                                            c.execute(f"DELETE FROM stock_market_zakaz WHERE user_id = {tovar}")
                                        if price_chapchas_for_seller == chn:
                                            c.execute(f"DELETE FROM stock_market WHERE user_id = {ui}")
                                            db.commit()
                                            break
                                        price_chapchas_for_buyer = 0
                                        price_freebases_for_buyer = 0
                                        price_chapchas_for_market = 0
                                        price_cena_for_market = 0
                                        db.commit()
                                    else:
                                        if bch == price_chapchas_for_buyer or bfrp - (bch * bcena) < 0:
                                            c.execute(f"DELETE FROM stock_market_zakaz WHERE user_id = {tovar}")
                        except:
                            pass
                    else:
                        await message.answer("Максимальная цена для чапчей 1 000 000 000 000 000 фрибасов\nМинимальная цена для чапчей 1 000 000 фрибасов")
                else:
                    await message.answer("Минимальная сума продажи 1 чапча")
            else:
                await message.answer("Недостаточно средств")
        except:
            await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    except:
        await message.answer("Продать чапчи Число Цена (за все)")
    db.commit()
    db.close()


@dp.message_handler(Text(startswith=['Купить чапчи', 'Чапчи купить', 'купить чапчи', 'чапчи купить']))
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        si = int(message.text.split(' ')[-1])
        ui = message.from_user.id
        try:
            c.execute(f"SELECT user_prefix, user_nick, user_chapchas, user_freebases FROM user_data WHERE user_id = {ui}")
            items = c.fetchall()
            for el in items:
                up = el[0]
                un = el[1]
                uch = el[2]
                uf = el[3]
            try:
                c.execute(f"SELECT * FROM stock_market WHERE user_id = {si}")
                items = c.fetchall()
                for el in items:
                    chn = el[1]
                    cena = el[2]
                c.execute(f"SELECT user_freebases FROM user_data WHERE user_id = {si}")
                items = c.fetchall()
                for el in items:
                    sf = el[0]
                if uf >= cena:
                    c.execute(f"UPDATE user_data SET user_chapchas = {uch + chn}, user_freebases = {uf - cena} WHERE user_id = {ui}")
                    c.execute(f"UPDATE user_data SET user_freebases = {sf + cena} WHERE user_id = {si}")
                    c.execute(f"DELETE FROM stock_market WHERE user_id = {si}")
                    await message.answer("Чапчи успешно куплены!")
                    try:
                        await bot.send_message(si, f"Пользователь <b><i>[{up}]</i><a href='tg://user?id={ui}'>{un}</a></b> купил Ваши чапчи!")
                    except:
                        pass
                else:
                    await message.answer("Недостаточно средств")
            except:
                await message.answer("Товар не найден")
        except:
            await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    except:
        await message.answer("Купить чапчи ID")
    db.commit()
    db.close()

@dp.message_handler(Text(startswith=['Биржа снять', 'Снять чапчи', 'Чапчи снять', 'Убрать чапчи', 'биржа снять', 'снять чапчи', 'чапчи снять', 'убрать чапчи']))
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT chapchas FROM stock_market WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            chn = el[0]
        c.execute(f"SELECT user_chapchas FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            uch = el[0]
        c.execute(f"UPDATE user_data SET user_chapchas = {uch + chn} WHERE user_id = {message.from_user.id}")
        c.execute(f"DELETE FROM stock_market WHERE user_id = {message.from_user.id}")
        await message.answer("Вы сняли чапчи с биржи!")
    except:
        await message.answer("У Вас нету чапчей на бирже")
    db.commit()
    db.close()



@dp.message_handler(Text(startswith=['Заказать чапчи', 'Биржа заказ', 'Чапчи заказать', 'Заказ биржа', 'Биржа заказать', 'Чапчи заказ', 'Заказ чапчи', 'заказать чапчи', 'биржа заказ', 'чапчи заказать', 'заказ биржа', 'биржа заказать', 'чапчи заказ', 'заказ чапчи']))
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        chn = int(message.text.split(' ')[2])
        cena = int(message.text.split(' ')[3])
        cn = chn * cena
        ui = message.from_user.id
        try:
            c.execute(f"SELECT user_freebases FROM user_data WHERE user_id = {ui}")
            items = c.fetchall()
            for el in items:
                uf = el[0]
            if uf >= cn:
                if chn > 0:
                    if cena >= 1000000 and cena <= 1000000000000:
                        try:
                            c.execute("INSERT INTO stock_market_zakaz VALUES (?, ?, ?)",
                                      (message.from_user.id, chn, cena))
                        except:
                            c.execute(f"UPDATE stock_market_zakaz SET chapchas = {chn}, cena = {cena} WHERE user_id = {ui}")
                        await message.answer("Заказ чапчей принят!")
                        try:
                            c.execute(f"SELECT user_id FROM stock_market WHERE cena <= {cn} ORDER BY cena ASC")
                            items = c.fetchall()
                            itemsis = []
                            noi = 0
                            for el in items:
                                for e in el:
                                    itemsis.append(e)
                                    noi += 1
                            if noi != 0:
                                c.execute(f"SELECT user_prefix, user_nick, user_chapchas, user_freebases FROM user_data WHERE user_id = {ui}")
                                items = c.fetchall()
                                for el in items:
                                    up = el[0]
                                    un = el[1]
                                    uch = el[2]
                                    uf = el[3]
                                price_chapchas_for_buyer = 0
                                price_freebases_for_buyer = 0
                                price_freebases_for_seller = 0
                                price_chapchas_for_market = 0
                                price_cena_for_market = 0
                                stop = False
                                for tovar in itemsis:
                                    if stop:
                                        break
                                    c.execute(f"SELECT * FROM stock_market WHERE user_id = {tovar}")
                                    items = c.fetchall()
                                    for el in items:
                                        si = el[0]
                                        sch = el[1]
                                        scena = el[2]
                                    c.execute(f"SELECT user_prefix, user_nick, user_freebases FROM user_data WHERE user_id = {tovar}")
                                    items = c.fetchall()
                                    for el in items:
                                        sp = el[0]
                                        sn = el[1]
                                        sfr = el[2]
                                    scenafo = round(scena/sch)
                                    if uf >= scenafo:
                                        if scenafo > cena:
                                            break
                                        for i in range(1,sch+1):
                                            price_chapchas_for_buyer = i
                                            price_freebases_for_buyer += scenafo
                                            price_freebases_for_seller += scenafo
                                            price_chapchas_for_market = i
                                            price_cena_for_market += scenafo
                                            if uf - price_freebases_for_buyer < 0 or chn - price_chapchas_for_buyer == 0:
                                                if sch == price_chapchas_for_buyer:
                                                    c.execute(f"DELETE FROM stock_market WHERE user_id = {tovar}")
                                                stop = True
                                                break
                                        c.execute(f"UPDATE user_data SET user_chapchas = {uch + price_chapchas_for_buyer}, user_freebases = {uf - price_freebases_for_buyer} WHERE user_id = {ui}")
                                        c.execute(f"UPDATE user_data SET user_freebases = {sfr + price_freebases_for_seller} WHERE user_id = {tovar}")
                                        c.execute(f"UPDATE stock_market SET chapchas = {sch - price_chapchas_for_market}, cena = {round(scena - price_cena_for_market)} WHERE user_id = {tovar}")
                                        c.execute(f"UPDATE stock_market_zakaz SET chapchas = {chn - price_chapchas_for_market} WHERE user_id = {ui}")
                                        await message.answer(f"Пользователь <b><i>[{sp}]</i> <a href='tg://user?id={tovar}'>{sn}</a></b> продал {price_chapchas_for_market} чапчей за {price_freebases_for_seller} фрибасов!", parse_mode="HTML")
                                        try:
                                            await bot.send_message(tovar, f"Пользователь <b><i>[{up}]</i> <a href='tg://user?id={ui}'>{un}</a></b> купил {price_chapchas_for_market} чапчей за {price_freebases_for_seller} фрибасов!", parse_mode="HTML")
                                        except:
                                            pass
                                        price_freebases_for_seller = 0
                                        price_chapchas_for_market = 0
                                        price_cena_for_market = 0
                                        db.commit()
                                        if sch == price_chapchas_for_buyer or uf - price_cena_for_buyer < 0:
                                            c.execute(f"DELETE FROM stock_market WHERE user_id = {tovar}")
                                        if price_chapchas_for_buyer == chn or uf - cn < 0:
                                            c.execute(f"DELETE FROM stock_market_zakaz WHERE user_id = {ui}")
                                            break
                        except:
                            pass
                    else:
                        await message.answer("Максимальная цена для чапчей 1 000 000 000 000 фрибасов\nМинимальная цена для чапчей 1 000 000 фрибасов")
                else:
                    await message.answer("Минимальная сума заказа 1 чапча")
            else:
                await message.answer("Недостаточно средств")
        except:
            await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    except:
        await message.answer("Заказать чапчи Число Цена (за 1 чапчу)")
    db.commit()
    db.close()

@dp.message_handler(text=['Мой заказ', 'Заказ', 'мой заказ', 'заказ'])
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_prefix, user_nick FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            up = el[0]
            un = el[1]
        try:
            c.execute(f"SELECT * FROM stock_market_zakaz WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                ui = el[0]
                chn = el[1]
                cena = el[2]
            await message.answer(f"""<b>Заказ от <i>[{up}]</i> <a href='tg://user?id={ui}'>{un}</a></b>

Заказ: <b>{chn} чапчей</b>
Цена за 1 чапчу: <b>{cena} фрибасов</b>""", parse_mode="HTML") 
        except:
            await message.answer("У Вас нету заказов")
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    db.commit()
    db.close()

@dp.message_handler(Text(startswith=['Заказ снять', 'Снять заказ', 'Убрать заказ', 'заказ снять', 'снять заказ', 'убрать заказ']))
async def process_giveeclairs_command(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT chapchas FROM stock_market_zakaz WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            zi = True
        if zi:
            c.execute(f"DELETE FROM stock_market_zakaz WHERE user_id = {message.from_user.id}")
            await message.answer("Вы удалили заказ чапчей!")
    except:
        await message.answer("У Вас нету заказов чапчей")
    db.commit()
    db.close()