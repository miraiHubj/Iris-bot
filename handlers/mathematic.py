from aiogram import types
from dispatcher import dp, bot
from aiogram.dispatcher.filters import Text
import math

@dp.message_handler(Text(startswith=['Чапча реши', 'Чапча решай', 'чапча реши', 'чапча решай']))
async def chapcha_expression(message: types.Message):
    if message.text.find('решай') != -1:
        try:
            sexpr = message.text[12:]
            try:
                expr = sexpr
                cr = True
                while expr.find('^') != -1:
                    expr2 = expr[expr.find('^') + 1:]
                    op = '**'
                    expr1 = expr[:expr.find('^')]
                    expr = expr1 + op + expr2
                while expr.find(':') != -1:
                    expr2 = expr[expr.find(':') + 1:]
                    op = '/'
                    expr1 = expr[:expr.find(':')]
                    expr = expr1 + op + expr2
                while expr.find('÷') != -1:
                    expr2 = expr[expr.find('÷') + 1:]
                    op = '/'
                    expr1 = expr[:expr.find('÷')]
                    expr = expr1 + op + expr2
                while expr.find('×') != -1:
                    expr2 = expr[expr.find('×') + 1:]
                    op = '*'
                    expr1 = expr[:expr.find('×')]
                    expr = expr1 + op + expr2
                while expr.find(',') != -1:
                    expr2 = expr[expr.find(',') + 1:]
                    op = '.'
                    expr1 = expr[:expr.find(',')]
                    expr = expr1 + op + expr2
                while expr.find('!') != -1:
                    num = 0
                    if expr.find(')') == expr.find('!')-1:
                        oper = ''
                        numsk = 0
                        while oper != '(':
                            oper = expr[expr.find('!')-numsk-1:expr.find('!')-numsk]
                            numsk += 1
                        expr = str(expr[:expr.find('!')-numsk]) + str(eval(expr[expr.find('!')-numsk+1:expr.find('!')-1])) + str(expr[expr.find('!'):])
                    while True:
                        try:
                            fact = int(expr[expr.find('!')-num-1:expr.find('!')-num])
                            num += 1
                        except:
                            break
                    if num == 0:
                        await message.answer('Вы неправильно ввели факториал числа')
                        cr = False
                        break
                    else:
                        expr1 = expr[:expr.find('!')-num]
                        fact = int(expr[expr.find('!')-num:expr.find('!')])
                        op = math.factorial(fact)
                        expr2 = expr[expr.find('!')+1:]
                        expr = str(expr1) + str(op) + str(expr2)
                if cr:
                    await message.answer(f"<b>Я решил!</b>\n\n{sexpr} = <b>{eval(expr)}</b>", parse_mode="HTML")
            except:
                await message.answer("Я не понял пример((")
        except:
            await message.answer("Чапча реши Пример")
    else:
        try:
            sexpr = message.text[11:]
            try:
                expr = sexpr
                cr = True
                while expr.find('^') != -1:
                    expr2 = expr[expr.find('^') + 1:]
                    op = '**'
                    expr1 = expr[:expr.find('^')]
                    expr = expr1 + op + expr2
                while expr.find(':') != -1:
                    expr2 = expr[expr.find(':') + 1:]
                    op = '/'
                    expr1 = expr[:expr.find(':')]
                    expr = expr1 + op + expr2
                while expr.find('÷') != -1:
                    expr2 = expr[expr.find('÷') + 1:]
                    op = '/'
                    expr1 = expr[:expr.find('÷')]
                    expr = expr1 + op + expr2
                while expr.find('×') != -1:
                    expr2 = expr[expr.find('×') + 1:]
                    op = '*'
                    expr1 = expr[:expr.find('×')]
                    expr = expr1 + op + expr2
                while expr.find(',') != -1:
                    expr2 = expr[expr.find(',') + 1:]
                    op = '.'
                    expr1 = expr[:expr.find(',')]
                    expr = expr1 + op + expr2
                while expr.find('!') != -1:
                    num = 0
                    if expr.find(')') == expr.find('!')-1:
                        oper = ''
                        numsk = 0
                        while oper != '(':
                            oper = expr[expr.find('!')-numsk-1:expr.find('!')-numsk]
                            numsk += 1
                        expr = str(expr[:expr.find('!')-numsk]) + str(eval(expr[expr.find('!')-numsk+1:expr.find('!')-1])) + str(expr[expr.find('!'):])
                    while True:
                        try:
                            fact = int(expr[expr.find('!')-num-1:expr.find('!')-num])
                            num += 1
                        except:
                            break
                    if num == 0:
                        await message.answer('Вы неправильно ввели факториал числа')
                        cr = False
                        break
                    else:
                        expr1 = expr[:expr.find('!')-num]
                        fact = int(expr[expr.find('!')-num:expr.find('!')])
                        op = math.factorial(fact)
                        expr2 = expr[expr.find('!')+1:]
                        expr = str(expr1) + str(op) + str(expr2)
                if cr:
                    await message.answer(f"<b>Я решил!</b>\n\n{sexpr} = <b>{eval(expr)}</b>", parse_mode="HTML")
            except:
                await message.answer("Я не понял пример((")
        except:
            await message.answer("Чапча решай Пример")


@dp.message_handler(Text(startswith=['Чапча число пи', 'Число пи', 'чапча число пи', 'число пи']))
async def chapcha_expression(message: types.Message):
    pi = "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
    print(len(pi)-2)
    try:
        if len(message.text) != 14 and len(message.text) != 8:
            num = int(message.text.split(' ')[-1]) + 2
            if num - 2 > 0:
                if num - 2 > 200:
                    await message.answer(f"Вот <b>200 цифр</b> после запятой числа пи:\n\n{pi}", parse_mode="HTML")
                else:
                    await message.answer(f"Вот <b>{num - 2} цифр</b> после запятой числа пи:\n\n{pi[:num]}", parse_mode="HTML")
            else:
                await message.answer("Число пи без цифр после запятой:\n\n3")
        else:
            await message.answer(f"Вот <b>200 цифр</b> после запятой числа пи:\n\n{pi}", parse_mode="HTML")
    except:
        await message.answer("Чапча число пи Число")