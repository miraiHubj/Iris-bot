from aiogram import types
from dispatcher import dp
import sqlite3

@dp.message_handler(commands=['nick'])
async def nick(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    c.execute(f"SELECT user_nick FROM user_data WHERE user_id = {message.from_user.id}")
    items = c.fetchall()
    for el in items:
        await message.answer(f'Ник пользователя: "<b>{el[0]}</b>"', parse_mode="HTML")
    db.commit()
    db.close()

#qsnewnick
@dp.message_handler(commands=['newnick'])
async def newnick(message: types.Message):
    db = sqlite3.connect('chapcha_data_base.db')
    c = db.cursor()
    try:
        c.execute(f"SELECT user_nick FROM user_data WHERE user_id <> {message.from_user.id}")
        unsll = c.fetchall()
        unsl = []
        for n in unsll:
            unsl.append(n[0])
        uns = []
        for n in unsl:
            if n == '' or n == None:
                pass
            else:
                uns.append(n)
        nick = message.text[9:]
        while nick.find(' ') == 0:
            nick = nick[1:]
        while nick.find(' ') == len(nick) - 1:
            nick = nick[:-1]
        while nick.find('ㅤ') == 0:
            nick = nick[1:]
        while nick.find('ㅤ') == len(nick) - 1:
            nick = nick[:-1]
        while nick.find('у') != -1:
            nick1 = nick[:nick.find('у')]
            nick2 = nick[nick.find('у')+1:]
            nick = nick1 + 'y' + nick2
        while nick.find('е') != -1:
            nick1 = nick[:nick.find('е')]
            nick2 = nick[nick.find('е')+1:]
            nick = nick1 + 'e' + nick2
        while nick.find('х') != -1:
            nick1 = nick[:nick.find('х')]
            nick2 = nick[nick.find('х')+1:]
            nick = nick1 + 'x' + nick2
        while nick.find('а') != -1:
            nick1 = nick[:nick.find('а')]
            nick2 = nick[nick.find('а')+1:]
            nick = nick1 + 'a' + nick2
        while nick.find('р') != -1:
            nick1 = nick[:nick.find('р')]
            nick2 = nick[nick.find('р')+1:]
            nick = nick1 + 'p' + nick2
        while nick.find('о') != -1:
            nick1 = nick[:nick.find('о')]
            nick2 = nick[nick.find('о')+1:]
            nick = nick1 + 'o' + nick2
        while nick.find('с') != -1:
            nick1 = nick[:nick.find('с')]
            nick2 = nick[nick.find('с')+1:]
            nick = nick1 + 'c' + nick2
        while nick.find('К') != -1:
            nick1 = nick[:nick.find('К')]
            nick2 = nick[nick.find('К')+1:]
            nick = nick1 + 'K' + nick2
        while nick.find('Е') != -1:
            nick1 = nick[:nick.find('Е')]
            nick2 = nick[nick.find('Е')+1:]
            nick = nick1 + 'E' + nick2
        while nick.find('Н') != -1:
            nick1 = nick[:nick.find('Н')]
            nick2 = nick[nick.find('Н')+1:]
            nick = nick1 + 'H' + nick2
        while nick.find('Х') != -1:
            nick1 = nick[:nick.find('Х')]
            nick2 = nick[nick.find('Х')+1:]
            nick = nick1 + 'X' + nick2
        while nick.find('В') != -1:
            nick1 = nick[:nick.find('В')]
            nick2 = nick[nick.find('В')+1:]
            nick = nick1 + 'B' + nick2
        while nick.find('А') != -1:
            nick1 = nick[:nick.find('А')]
            nick2 = nick[nick.find('А')+1:]
            nick = nick1 + 'A' + nick2
        while nick.find('Р') != -1:
            nick1 = nick[:nick.find('Р')]
            nick2 = nick[nick.find('Р')+1:]
            nick = nick1 + 'P' + nick2
        while nick.find('О') != -1:
            nick1 = nick[:nick.find('О')]
            nick2 = nick[nick.find('О')+1:]
            nick = nick1 + 'O' + nick2
        while nick.find('С') != -1:
            nick1 = nick[:nick.find('С')]
            nick2 = nick[nick.find('С')+1:]
            nick = nick1 + 'C' + nick2
        while nick.find('М') != -1:
            nick1 = nick[:nick.find('М')]
            nick2 = nick[nick.find('М')+1:]
            nick = nick1 + 'M' + nick2
        while nick.find('Т') != -1:
            nick1 = nick[:nick.find('Т')]
            nick2 = nick[nick.find('Т')+1:]
            nick = nick1 + 'T' + nick2
        l = len(nick)
        if nick == "":
            await message.answer(f'/newnick Новый Ник')
        elif l > 20:
            await message.answer('Максимальная длина ника 20 символов')
        else:
            try:
                c.execute(f"SELECT user_job FROM user_data WHERE user_id = {message.from_user.id}")
                items = c.fetchall()
                for el in items:
                    work = el[0]
                if work.lower() == 'архитектор':
                    work1 = 'architector'
                elif work.lower() == 'блогер':
                    work1 = 'bloger'
                elif work.lower() == 'строитель':
                    work1 = 'builder'
                elif work.lower() == 'шахтер':
                    work1 = 'caver'
                elif work.lower() == 'разработчик':
                    work1 = 'developer'
                elif work.lower() == 'киберспортсмен':
                    work1 = 'esportsman'
                elif work.lower() == 'фермер':
                    work1 = 'farmer'
                elif work.lower() == 'киллер':
                    work1 = 'killer'
                elif work.lower() == 'программист':
                    work1 = 'programmer'
                elif work.lower() == 'учитель':
                    work1 = 'teacher'
                else:
                    work1 = 'Нету'
                if work1 != 'Нету':
                    c.execute(f"UPDATE job_{work1} SET worker_nick = '{nick}' WHERE worker_id = {message.from_user.id}")
                c.execute(f"SELECT nick_1, nick_2, nick_3, nick_4, nick_5 FROM nicks_auction WHERE user_id <> {message.from_user.id}")
                items = c.fetchall()
                nll = []
                for n in items:
                    nll.append(n[0])
                    nll.append(n[1])
                    nll.append(n[2])
                    nll.append(n[3])
                    nll.append(n[4])
                nl = []
                for n in nll:
                    if n == '' or n == None:
                        pass
                    else:
                        nl.append(n)
                c.execute(f"SELECT item FROM nicks_auction")
                noall = c.fetchall()
                noal = []
                for n in noall:
                    noal.append(n[0])
                noa = []
                for n in noal:
                    if n == '' or n == None:
                        pass
                    else:
                        noa.append(n)
                for n in uns:
                    if n == nick:
                        print(forerrorprint)
                        break
                for n in nl:
                    if n == nick:
                        print(forerrorprint)
                        break
                for n in noa:
                    if n == nick:
                        print(forerrorprint)
                        break
                c.execute(f"UPDATE user_data SET user_nick = '{nick}' WHERE user_id = '{message.from_user.id}'")
                c.execute(f"UPDATE nicks_auction SET user_nick = '{nick}' WHERE user_id = '{message.from_user.id}'")
                await message.answer(f'Ник успешно изменен на "<b>{nick}</b>"', parse_mode="HTML")
            except:
                noan = 0
                for n in noa:
                    if n == nick:
                        noan += 1
                        break
                if noan > 0:
                    await message.answer(f'Ник "<b>{nick}</b>" выставлен на продажу на аукционе', parse_mode="HTML")
                else:
                    await message.answer(f'Ник "<b>{nick}</b>" уже занят', parse_mode="HTML")
    except:
        await message.answer(f'/newnick Новый Ник')
    db.commit()
    db.close()