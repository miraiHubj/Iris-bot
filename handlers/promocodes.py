from aiogram import types
from dispatcher import dp
import sqlite3

@dp.message_handler(commands=['ap'])
async def activate_promo(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_chapchas, user_coins, user_freebases, user_eclairs, user_startpromo, user_promo, user_promo1 FROM user_data WHERE user_id = {message.from_user.id}")
    except:
        await message.answer('Промокод не найден или был активирован\n(Вы не сможете активировать промокод, если вы не запустили бота')
    items = c.fetchall()
    try:
        pc = message.text.split(' ')[1]
        for el in items:
            if pc == "START_PROMO" and el[4] == 'YES':
                price = el[1] + 100
                c.execute(f"UPDATE user_data SET user_coins = {price} WHERE user_id = '{message.from_user.id}'")
                await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>, промокод активирован!", parse_mode="HTML")
                c.execute(f"UPDATE user_data SET user_startpromo = 'NO' WHERE user_id = '{message.from_user.id}'")
                break
            elif pc == "100_USERS_REGISTERED" and el[5] == "YES":
                with open('promo.txt', 'r') as p:
                    promo = int(p.readline())
                if promo > 0:
                    print("promo1 " + str(message.from_user.id))
                    price = el[2] + 1000
                    price_ch = el[0] + 100
                    promo -= 1
                    c.execute(f"UPDATE user_data SET user_freebases = {price}, user_chapchas = {price_ch} WHERE user_id = '{message.from_user.id}'")
                    c.execute(f"UPDATE user_data SET user_promo = 'NO' WHERE user_id = '{message.from_user.id}'")
                    await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>, промокод активирован!", parse_mode="HTML")
                    with open('promo.txt', 'w') as p:
                        p.write(str(promo))
                    break
                else:
                    await message.answer('Промокод не найден или был активирован\n(Вы не сможете активировать промокод, если вы не запустили бота)')
            elif pc == "Jby0g5Lb64mX92XV" and el[6] == "YES":
                with open('promo1.txt', 'r') as p:
                    promo = int(p.readline())
                if promo > 0:
                    c.execute(f"SELECT lvl_ppc, up_ppc FROM game_clicker WHERE user_id = {message.from_user.id}")
                    items2 = c.fetchall()
                    for i in items2:
                        lvl = i[0]
                        up = i[1]
                    print("newpromo " + str(message.from_user.id))
                    price_lvl = lvl + 5
                    price_up = up + 5
                    price_cena = (price_up + 1) * 1000
                    promo -= 1
                    c.execute(f"UPDATE game_clicker SET lvl_ppc = {price_lvl}, up_ppc = {price_up}, cena_ppc = {price_cena} WHERE user_id = '{message.from_user.id}'")
                    c.execute(f"UPDATE user_data SET user_promo1 = 'NO' WHERE user_id = '{message.from_user.id}'")
                    await message.answer(f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>, промокод активирован!", parse_mode="HTML")
                    with open('promo1.txt', 'w') as p:
                        p.write(str(promo))
                    break
                else:
                    await message.answer('Промокод не найден или был активирован\n(Вы не сможете активировать промокод, если вы не запустили бота)')
        else:
            await message.answer('Промокод не найден или был активирован\n(Вы не сможете активировать промокод, если вы не запустили бота)')
    except:
        await message.answer('Промокод не найден или был активирован\n(Вы не сможете активировать промокод, если вы не запустили бота)')
    db.commit()
    db.close()

#qspromo
@dp.message_handler(commands=['promo'])
async def promocodes(message: types.Message):
    await message.answer(f"""<b>Промокоды:</b>

<code>START_PROMO</code>
<code>Jby0g5Lb64mX92XV</code>
<code>100_USERS_REGISTERED</code>

/ap Промокод - ввести промокод

<a href='https://conff.org/'>БОЛЬШЕ ТГ БОТОВ НА CONFF.ORG</a>""", parse_mode="HTML", disable_web_page_preview=True)