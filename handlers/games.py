from aiogram import types
from dispatcher import bot, dp
from aiogram.dispatcher.filters import Text
from random import randint
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery
import asyncio
import sqlite3
import datetime

@dp.message_handler(commands=['games'])
async def games(message: types.Message):
    await message.answer(f"""<b>Игры:</b>

/clicker - кликер
/farm - фарм
<code>Кубик</code> Число Ставка - кубик
<code>Рулетка</code> Число Ставка - рулетка
<code>Дартс</code> Число Ставка - дартс
<code>Кража</code> ID/@ссылка/рандом - ограбление
<code>Открыть</code> Кейс - открыть кейс
<code>!кнопки</code> - поиск кнопки""", parse_mode="HTML")

#qsclicker
@dp.message_handler(commands=['clicker', 'cl'])
async def clicker(message: types.Message):
    if message.chat.type == 'private':
        button_pc = KeyboardButton('+Очки')
        button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_pc)
        await message.answer("""Игра: <b>Кликер</b>

Нажимай на кнопку, чтобы получить монеты!

<b>Предупреждение:</b> Не кликайте быстро, делайте интервал в 1-2 секунды, если вы были заблокированы по причине спам, напишите разработчику: @Alone228_YT

/ckb - убрать кнопки""", parse_mode="HTML", reply_markup=button)
    else:
        await message.answer("Кликер доступен только в лс Чапчи")

#qspluspoints
@dp.message_handler(text=['+Очки'])
async def plus_points(message: types.Message):
    if message.chat.type == 'private':
        if True:
            print("клик " + str(message.from_user.username))
            try:
                db = sqlite3.connect('chapcha_data_base.db')
                c = db.cursor()
                c.execute(f"SELECT user_points FROM user_data WHERE user_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    up = el[0]
                c.execute(f"SELECT up_ppc, up_dp FROM game_clicker WHERE user_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    ppc = el[0]
                    dp = el[1]
                dpn = randint(1, 100)
                try:
                    if dpn <= dp:
                        price = up + (ppc * 2)
                    else:
                        price = up + ppc
                    c.execute(f"UPDATE user_data SET user_points = {price} WHERE user_id = {message.from_user.id}")
                    try:
                        await message.delete()
                    except:
                        pass
                    if dpn <= dp:
                        await message.answer(f"+{ppc * 2} очков")
                    else:
                        await message.answer(f"+{ppc} очков")
                except:
                    try:
                        await message.delete()
                    except:
                        pass
                    await message.answer('Ой-ой, не так быстро!')
                    print("2. " + str(message.from_user.id))
            except:
                try:
                    await massage.delete()
                except:
                    pass
                await message.answer('Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота')
            c.execute(f"SELECT user_coins FROM user_data WHERE user_id = {message.from_user.id}")
            db.commit()
            db.close()
    else:
        pass




#qsfarming
@dp.message_handler(commands=['farm', 'farming'])
async def farm(message: types.Message):
    try:
        db = sqlite3.connect('chapcha_data_base.db')
        c = db.cursor()
        c.execute(f"SELECT up_farm, up_ft FROM game_farm WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            up_farm = el[0]
            ft = el[1]
        c.execute(f"SELECT user_nick, user_points, user_for_farm FROM user_data WHERE user_id = {message.from_user.id}")
        items = c.fetchall()
        for el in items:
            un = el[0]
            up = el[1]
            ulf = el[2]
        ulf = datetime.datetime.strptime(str(ulf), '%Y-%m-%d %H:%M:%S')
        date_now = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        date_now = datetime.datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S')
        if date_now >= ulf:
            farm = randint(5, up_farm)
            price_points = up + farm
            date_change = datetime.timedelta(hours=ft)
            date_new = date_now + date_change
            c.execute(f"UPDATE user_data SET user_points = {price_points}, user_for_farm = '{date_new}' WHERE user_id = {message.from_user.id}")
            await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{un}</a> нафармил {farm} очков!\nСледующая возможность фарма появится через {ft} часов!", parse_mode="HTML")
        else:
            date2 = str(datetime.datetime.strptime(str(ulf), '%Y-%m-%d %H:%M:%S')-datetime.datetime.now())
            secs = date2.split(':')[2].split('.')[0] + ' секунд'
            mins = date2.split(':')[1] + ' минут '
            hours = date2.split(':')[0].split(' ')[-1] + ' часов '
            if hours.find('0') == 0:
                hours = hours[1:]
            if mins.find('0') == 0:
                mins = mins[1:]
            if secs.find('0') == 0:
                secs = secs[1:]
            date1 = ''
            if hours.split(' ')[0] != '0' and hours.split(' ')[0] != '':
                date1 += hours
            if mins.split(' ')[0] != '0' and mins.split(' ')[0] != '':
                date1 += mins
            if secs.split(' ')[0] != '0' and secs.split(' ')[0] != '':
                date1 += secs
            await message.answer(f"Следующая попытка фарма появится через {date1}!")
        db.commit()
        db.close()
    except:
        await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")



@dp.message_handler(Text(startswith=['Кубик', 'кубик']))
async def cube(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        comm = message.text[6:]
        num = round(float(comm.split(' ')[0]))
        st = round(float(comm.split(' ')[1]))
        if num > 0 and num < 7:
            try:
                c.execute(f"SELECT up_x FROM game_cube WHERE user_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    x = el[0]
                c.execute(f"SELECT user_nick, user_points FROM user_data WHERE user_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    un = el[0]
                    up = el[1]
                if up >= st:
                    if st >= 10:
                        price_points = up - st
                        c.execute(f"UPDATE user_data SET user_points = {price_points} WHERE user_id = {message.from_user.id}")
                        msg = await message.answer_dice()
                        if msg.dice.value == num:
                            price_points = (up - st) + round(st * x)
                            c.execute(f"UPDATE user_data SET user_points = {price_points} WHERE user_id = {message.from_user.id}")
                            pp = round(st * x)
                            task = asyncio.create_task(wait_for_res_cube(message, True, msg.dice.value, message.from_user.id, un, pp, st))
                        else:
                            task = asyncio.create_task(wait_for_res_cube(message, False, msg.dice.value, message.from_user.id, un, 0, st))
                    else:
                        await message.answer("Минимальная сумма ставки 10 очков!")
                else:
                    await message.answer("Ставка слишком большая, недостаточно средств!")
            except:
                await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
        else:
            await message.answer("Выберите число от 1 до 6")
    except:
        await message.answer("Кубик Число Ставка")
    db.commit()
    db.close()


async def wait_for_res_cube(message, tof, dv, mfui, un, pp, st):
    await asyncio.sleep(4)
    if tof:
        await message.answer(f"На кубике число {dv}, <a href='tg://user?id={mfui}'>{un}</a> выиграл {pp} очков!", parse_mode="HTML")
    else:
        await message.answer(f"На кубике число {dv}, <a href='tg://user?id={mfui}'>{un}</a> проиграл {st} очков!", parse_mode="HTML")






@dp.message_handler(Text(startswith=['Рулетка', 'рулетка']))
async def slot_machine(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        comm = message.text[8:]
        num = round(float(comm.split(' ')[0]))
        st = round(float(comm.split(' ')[1]))
        if num > 0 and num < 65:
            try:
                c.execute(f"SELECT up_x FROM game_slot_machine WHERE user_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    x = el[0]
                c.execute(f"SELECT user_nick, user_points FROM user_data WHERE user_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    un = el[0]
                    up = el[1]
                if up >= st:
                    if st >= 10:
                        price_points = up - st
                        c.execute(f"UPDATE user_data SET user_points = {price_points} WHERE user_id = {message.from_user.id}")
                        slot_machine1 = await message.answer_dice(emoji="🎰")
                        slot_machine = slot_machine1.dice.value
                        if slot_machine > num - 5 and slot_machine < num + 5:
                            if slot_machine == num:
                                price_points = (up - st) + round(st * x * 2)
                                c.execute(f"UPDATE user_data SET user_points = {price_points} WHERE user_id = {message.from_user.id}")
                                pp = round(st * x * 2)
                                task = asyncio.create_task(wait_for_res_slot_machine(message, True, slot_machine, message.from_user.id, un, pp, st))
                                
                            else:
                                price_points = (up - st) + round(st * x)
                                c.execute(f"UPDATE user_data SET user_points = {price_points} WHERE user_id = {message.from_user.id}")
                                pp = round(st * x)
                                task = asyncio.create_task(wait_for_res_slot_machine(message, True, slot_machine, message.from_user.id, un, pp, st))
                        else:
                            task = asyncio.create_task(wait_for_res_slot_machine(message, False, slot_machine, message.from_user.id, un, 0, st))
                    else:
                        await message.answer("Минимальная сумма ставки 10 очков!")
                else:
                    await message.answer("Ставка слишком большая, недостаточно средств!")
            except:
                await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
        else:
            await message.answer("Выберите число от 1 до 64")
    except:
        await message.answer("Рулетка Число Ставка")
    db.commit()
    db.close()


async def wait_for_res_slot_machine(message, tof, dv, mfui, un, pp, st):
    await asyncio.sleep(3)
    if tof:
        await message.answer(f"Рулетка выдала число {dv}, <a href='tg://user?id={mfui}'>{un}</a> выиграл {pp} очков!", parse_mode="HTML")
    else:
        await message.answer(f"Рулетка выдала число {dv}, <a href='tg://user?id={mfui}'>{un}</a> проиграл {st} очков!", parse_mode="HTML")






@dp.message_handler(Text(startswith=['Дартс', 'дартс']))
async def darts(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        comm = message.text[6:]
        num = round(float(comm.split(' ')[0]))
        st = round(float(comm.split(' ')[1]))
        if num > 0 and num < 7:
            try:
                c.execute(f"SELECT up_x FROM game_darts WHERE user_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    x = el[0]
                c.execute(f"SELECT user_nick, user_points FROM user_data WHERE user_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    un = el[0]
                    up = el[1]
                if up >= st:
                    if st >= 10:
                        price_points = up - st
                        c.execute(f"UPDATE user_data SET user_points = {price_points} WHERE user_id = {message.from_user.id}")
                        darts1 = await message.answer_dice(emoji="🎯")
                        darts = darts1.dice.value
                        if darts == num:
                            price_points = (up - st) + round(st * x)
                            c.execute(f"UPDATE user_data SET user_points = {price_points} WHERE user_id = {message.from_user.id}")
                            pp = round(st * x)
                            task = asyncio.create_task(wait_for_res_darts(message, True, darts, message.from_user.id, un, pp, st))
                        else:
                            task = asyncio.create_task(wait_for_res_darts(message, False, darts, message.from_user.id, un, 0, st))
                    else:
                        await message.answer("Минимальная сумма ставки 10 очков!")
                else:
                    await message.answer("Ставка слишком большая, недостаточно средств!")
            except:
                await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
        else:
            await message.answer("Выберите число от 1 до 6")
    except:
        await message.answer("Дартс Число Ставка")
    db.commit()
    db.close()


async def wait_for_res_darts(message, tof, dv, mfui, un, pp, st):
    await asyncio.sleep(3)
    if tof:
        await message.answer(f"Попадание в число {dv}, <a href='tg://user?id={mfui}'>{un}</a> выиграл {pp} очков!", parse_mode="HTML")
    else:
        await message.answer(f"Попадание в число {dv}, <a href='tg://user?id={mfui}'>{un}</a> проиграл {st} очков!", parse_mode="HTML")






@dp.message_handler(text=['Кража рандом', 'Ограбление рандом', 'кража рандом', 'ограбление рандом'])
async def darts(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute("SELECT user_id FROM user_data")
        items = c.fetchall()
        uslist = []
        for el in items:
            for e in el:
                uslist.append(e)
        ru = randint(1,len(uslist))
        zhi = uslist[ru]
        try:
            c.execute(f"SELECT up_bag, up_st FROM game_stealing WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                ub = el[0]
                ust = el[1]
            c.execute(f"SELECT user_nick, user_coins FROM user_data WHERE user_id = {message.from_user.id}")
            items = c.fetchall()
            for el in items:
                un = el[0]
                uc = el[1]
            try:
                c.execute(f"SELECT up_s FROM game_stealing WHERE user_id = {zhi}")
                items = c.fetchall()
                for el in items:
                    zhs = el[0]
                c.execute(f"SELECT user_nick, user_coins FROM user_data WHERE user_id = {zhi}")
                items = c.fetchall()
                for el in items:
                    zhn = el[0]
                    zhc = el[1]
                cs = randint(1,100)
                if cs <= ust:
                    cs = randint(1,100)
                    if cs >= zhs:
                        sp = randint(0, ub)
                        if sp == 0:
                            await message.answer(f"Попытка ограбить <a href='tg://user?id={zhi}'><b>{zhn}</b></a> оборвалась!\nУ Вас не получилось достать денег из кошелька жертвы!")
                        else:
                            if zhc == 0:
                                await message.answer(f"Попытка ограбить <a href='tg://user?id={zhi}'><b>{zhn}</b></a> оборвалась!\nУ Вашей жертвы нету монет!")
                            else:
                                if zhc <= sp:
                                    c.execute(f"UPDATE user_data SET user_coins = {uc+zhc} WHERE user_id = {message.from_user.id}")
                                    c.execute(f"UPDATE user_data SET user_coins = 0 WHERE user_id = {zhi}")
                                    await message.answer(f"Вы ограбили <a href='tg://user?id={zhi}'><b>{zhn}</b></a>!\nВы достали {zhc} монет из кошелька жертвы!\nИнтересно, какая у <a href='tg://user?id={zhi}'><b>{zhn}</b></a> будет реакция, когда он(а) заметит, что его(ее) кошелек полностью опустел?")
                                else:
                                    c.execute(f"UPDATE user_data SET user_coins = {uc+sp} WHERE user_id = {message.from_user.id}")
                                    c.execute(f"UPDATE user_data SET user_coins = {zhc-sp} WHERE user_id = {zhi}")
                                    await message.answer(f"Вы ограбили <a href='tg://user?id={zhi}'><b>{zhn}</b></a>!\nВы достали {sp} монет из кошелька жертвы!")
                    else:
                        await message.answer(f"Попытка ограбить <a href='tg://user?id={zhi}'><b>{zhn}</b></a> оборвалась!\nК счастью Вас никто не заметил!")
                else:
                    if uc > 5000:
                        shtr = randint(5000, uc)
                    else:
                        shtr = uc
                    c.execute(f"UPDATE user_data SET user_coins = {uc - shtr} WHERE user_id = {message.from_user.id}")
                    if uc == 0:
                        await message.answer(f"<b>Вы спалились!</b>\n<a href='tg://user?id={zhi}'><b>{zhn}</b></a> вызвал(а) полицию. Вас простили, так как у вас нету монет!", parse_mode="HTML")
                    else:
                        await message.answer(f"<b>Вы спалились!</b>\n<a href='tg://user?id={zhi}'><b>{zhn}</b></a> вызвал(а) полицию. Вы получили штраф в {shtr} монет!", parse_mode="HTML")
                    try:
                        if uc == 0:
                            await bot.send_message(zhi, f"Вас пытался(ась) ограбить <a href='tg://user?id={message.from_user.id}'><b>{un}</b></a>!\nПопытка ограбления была провалена, грабитель спалился но не получил штраф!")
                        else:
                            await bot.send_message(zhi, f"Вас пытался(ась) ограбить <a href='tg://user?id={message.from_user.id}'><b>{un}</b></a>!\nПопытка ограбления была провалена, грабитель спалился и получил штраф в {shtr} монет!")
                    except:
                        pass
            except:
                await message.answer("Пользователь не найден")
        except:
            await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
    except:
        pass
    db.commit()
    db.close()



@dp.message_handler(Text(startswith=['Кража', 'Ограбление', 'кража', 'ограбление']))
async def darts(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        if message.text.lower().find("кража") != -1:
            comm = message.text[6:]
        else:
            comm = message.text[11:]
        if comm.find('@') != -1:
            try:
                zhun = comm[1:]
                try:
                    c.execute(f"SELECT up_bag, up_st FROM game_stealing WHERE user_id = {message.from_user.id}")
                    items = c.fetchall()
                    for el in items:
                        ub = el[0]
                        ust = el[1]
                    c.execute(f"SELECT user_nick, user_coins FROM user_data WHERE user_id = {message.from_user.id}")
                    items = c.fetchall()
                    for el in items:
                        un = el[0]
                        uc = el[1]
                    try:
                        c.execute(f"SELECT user_id FROM user_data WHERE user_username = '{zhun}'")
                        items = c.fetchall()
                        for el in items:
                            zhi = el[0]
                        c.execute(f"SELECT up_s FROM game_stealing WHERE user_id = {zhi}")
                        items = c.fetchall()
                        for el in items:
                            zhs = el[0]
                        c.execute(f"SELECT user_nick, user_coins FROM user_data WHERE user_id = {zhi}")
                        items = c.fetchall()
                        for el in items:
                            zhn = el[0]
                            zhc = el[1]
                        cs = randint(1,100)
                        if cs <= ust:
                            cs = randint(1,100)
                            if cs >= zhs:
                                sp = randint(0, ub)
                                if sp == 0:
                                    await message.answer(f"Попытка ограбить <a href='tg://user?id={zhi}'><b>{zhn}</b></a> оборвалась!\nУ Вас не получилось достать денег из кошелька жертвы!")
                                else:
                                    if zhc == 0:
                                        await message.answer(f"Попытка ограбить <a href='tg://user?id={zhi}'><b>{zhn}</b></a> оборвалась!\nУ Вашей жертвы нету монет!")
                                    else:
                                        if zhc <= sp:
                                            c.execute(f"UPDATE user_data SET user_coins = {uc+zhc} WHERE user_id = {message.from_user.id}")
                                            c.execute(f"UPDATE user_data SET user_coins = 0 WHERE user_id = {zhi}")
                                            await message.answer(f"Вы ограбили <a href='tg://user?id={zhi}'><b>{zhn}</b></a>!\nВы достали {zhc} монет из кошелька жертвы!\nИнтересно, какая у <a href='tg://user?id={zhi}'><b>{zhn}</b></a> будет реакция, когда он(а) заметит, что его(ее) кошелек полностью опустел?")
                                        else:
                                            c.execute(f"UPDATE user_data SET user_coins = {uc+sp} WHERE user_id = {message.from_user.id}")
                                            c.execute(f"UPDATE user_data SET user_coins = {zhc-sp} WHERE user_id = {zhi}")
                                            await message.answer(f"Вы ограбили <a href='tg://user?id={zhi}'><b>{zhn}</b></a>!\nВы достали {sp} монет из кошелька жертвы!")
                            else:
                                await message.answer(f"Попытка ограбить <a href='tg://user?id={zhi}'><b>{zhn}</b></a> оборвалась!\nК счастью Вас никто не заметил!")
                        else:
                            if uc > 5000:
                                shtr = randint(5000, uc)
                            else:
                                shtr = uc
                            c.execute(f"UPDATE user_data SET user_coins = {uc - shtr} WHERE user_id = {message.from_user.id}")
                            if uc == 0:
                                await message.answer(f"<b>Вы спалились!</b>\n<a href='tg://user?id={zhi}'><b>{zhn}</b></a> вызвал(а) полицию. Вас простили, так как у вас нету монет!", parse_mode="HTML")
                            else:
                                await message.answer(f"<b>Вы спалились!</b>\n<a href='tg://user?id={zhi}'><b>{zhn}</b></a> вызвал(а) полицию. Вы получили штраф в {shtr} монет!", parse_mode="HTML")
                            try:
                                if uc == 0:
                                    await bot.send_message(zhi, f"Вас пытался(ась) ограбить <a href='tg://user?id={message.from_user.id}'><b>{un}</b></a>!\nПопытка ограбления была провалена, грабитель спалился но не получил штраф!")
                                else:
                                    await bot.send_message(zhi, f"Вас пытался(ась) ограбить <a href='tg://user?id={message.from_user.id}'><b>{un}</b></a>!\nПопытка ограбления была провалена, грабитель спалился и получил штраф в {shtr} монет!")
                            except:
                                pass
                    except:
                        await message.answer("Пользователь не найден")
                except:
                    await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
            except:
                await message.answer("Кража ID/@ссылка")
        else:
            try:
                zhi = int(comm)
                try:
                    c.execute(f"SELECT up_bag, up_st FROM game_stealing WHERE user_id = {message.from_user.id}")
                    items = c.fetchall()
                    for el in items:
                        ub = el[0]
                        ust = el[1]
                    c.execute(f"SELECT user_nick, user_coins FROM user_data WHERE user_id = {message.from_user.id}")
                    items = c.fetchall()
                    for el in items:
                        un = el[0]
                        uc = el[1]
                    try:
                        c.execute(f"SELECT up_s FROM game_stealing WHERE user_id = {zhi}")
                        items = c.fetchall()
                        for el in items:
                            zhs = el[0]
                        c.execute(f"SELECT user_nick, user_coins FROM user_data WHERE user_id = {zhi}")
                        items = c.fetchall()
                        for el in items:
                            zhn = el[0]
                            zhc = el[1]
                        cs = randint(1,100)
                        if cs <= ust:
                            cs = randint(1,100)
                            if cs >= zhs:
                                sp = randint(0, ub)
                                if sp == 0:
                                    await message.answer(f"Попытка ограбить <a href='tg://user?id={zhi}'><b>{zhn}</b></a> оборвалась!\nУ Вас не получилось достать денег из кошелька жертвы!")
                                else:
                                    if zhc == 0:
                                        await message.answer(f"Попытка ограбить <a href='tg://user?id={zhi}'><b>{zhn}</b></a> оборвалась!\nУ Вашей жертвы нету монет!")
                                    else:
                                        if zhc <= sp:
                                            c.execute(f"UPDATE user_data SET user_coins = {uc+zhc} WHERE user_id = {message.from_user.id}")
                                            c.execute(f"UPDATE user_data SET user_coins = 0 WHERE user_id = {zhi}")
                                            await message.answer(f"Вы ограбили <a href='tg://user?id={zhi}'><b>{zhn}</b></a>!\nВы достали {zhc} монет из кошелька жертвы!\nИнтересно, какая у <a href='tg://user?id={zhi}'><b>{zhn}</b></a> будет реакция, когда он(а) заметит, что его(ее) кошелек полностью опустел?")
                                        else:
                                            c.execute(f"UPDATE user_data SET user_coins = {uc+sp} WHERE user_id = {message.from_user.id}")
                                            c.execute(f"UPDATE user_data SET user_coins = {zhc-sp} WHERE user_id = {zhi}")
                                            await message.answer(f"Вы ограбили <a href='tg://user?id={zhi}'><b>{zhn}</b></a>!\nВы достали {sp} монет из кошелька жертвы!")
                            else:
                                await message.answer(f"Попытка ограбить <a href='tg://user?id={zhi}'><b>{zhn}</b></a> оборвалась!\nК счастью Вас никто не заметил!")
                        else:
                            if uc > 5000:
                                shtr = randint(5000, uc)
                            else:
                                shtr = uc
                            c.execute(f"UPDATE user_data SET user_coins = {uc - shtr} WHERE user_id = {message.from_user.id}")
                            if uc == 0:
                                await message.answer(f"<b>Вы спалились!</b>\n<a href='tg://user?id={zhi}'><b>{zhn}</b></a> вызвал(а) полицию. Вас простили, так как у вас нету монет!", parse_mode="HTML")
                            else:
                                await message.answer(f"<b>Вы спалились!</b>\n<a href='tg://user?id={zhi}'><b>{zhn}</b></a> вызвал(а) полицию. Вы получили штраф в {shtr} монет!", parse_mode="HTML")
                            try:
                                if uc == 0:
                                    await bot.send_message(zhi, f"Вас пытался(ась) ограбить <a href='tg://user?id={message.from_user.id}'><b>{un}</b></a>!\nПопытка ограбления была провалена, грабитель спалился но не получил штраф!")
                                else:
                                    await bot.send_message(zhi, f"Вас пытался(ась) ограбить <a href='tg://user?id={message.from_user.id}'><b>{un}</b></a>!\nПопытка ограбления была провалена, грабитель спалился и получил штраф в {shtr} монет!")
                            except:
                                pass
                    except:
                        await message.answer("Пользователь не найден")
                except:
                    await message.answer("Запустите бота, чтобы начать им пользоваться!\n/start - запустить бота")
            except:
                await message.answer("Кража ID/@ссылка/рандом")
    except:
        await message.answer("Кража ID/@ссылка/рандом")
    db.commit()
    db.close()