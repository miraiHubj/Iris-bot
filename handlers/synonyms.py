from aiogram import types
from dispatcher import dp
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery

@dp.message_handler(commands=['synonyms', 'syn'])
async def synonyms(message: types.Message):
    main = InlineKeyboardButton("⚜ Главное", callback_data="synmain")
    rate = InlineKeyboardButton("🏆 Рейтинг", callback_data="synrate")
    nick = InlineKeyboardButton("🏷 Ники", callback_data="synnick")
    pref = InlineKeyboardButton("🔰 Префиксы", callback_data="synpref")
    bal = InlineKeyboardButton("💰 Баланс", callback_data="synbal")
    games = InlineKeyboardButton("🎮 Игры", callback_data="syngames")
    promo = InlineKeyboardButton("🎁 Промокоды", callback_data="synpromo")
    clan = InlineKeyboardButton("⚜ Кланы", callback_data="synclan")
    job = InlineKeyboardButton("💼 Работы", callback_data="synjob")
    chat = InlineKeyboardButton("💬 Чаты", callback_data="synchat")
    stock_market = InlineKeyboardButton("⚖️ Биржа", callback_data="synstock_market")
    mary = InlineKeyboardButton("💝 Браки", callback_data="synmary")
    stat = InlineKeyboardButton("📊 Статистика", callback_data="synstat")
    other = InlineKeyboardButton("ℹ️ Другое", callback_data="synother")
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(main)
    floor.row(rate, nick)
    floor.row(pref, bal)
    floor.row(games, promo)
    floor.row(clan, job)
    floor.row(chat, stock_market)
    floor.row(mary, stat)
    floor.add(other)
    await message.answer("""<b>🗒 Список синонимов:</b>

⚜ | Главное
🏆 | Рейтинг
🏷 | Ники
🔰 | Префиксы
💰 | Баланс
🎮 | Игры
🎁 | Промокоды
⚜ | Кланы
💼 | Работы
💬 | Чаты
⚖️ | Биржа
💝 | Браки
📊 | Статистика
ℹ️ | Другое""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['backtosynlistbtn'])
async def back_to_synonyms(call: types.CallbackQuery):
    main = InlineKeyboardButton("⚜ Главное", callback_data="synmain")
    rate = InlineKeyboardButton("🏆 Рейтинг", callback_data="synrate")
    nick = InlineKeyboardButton("🏷 Ники", callback_data="synnick")
    pref = InlineKeyboardButton("🔰 Префиксы", callback_data="synpref")
    bal = InlineKeyboardButton("💰 Баланс", callback_data="synbal")
    games = InlineKeyboardButton("🎮 Игры", callback_data="syngames")
    promo = InlineKeyboardButton("🎁 Промокоды", callback_data="synpromo")
    clan = InlineKeyboardButton("⚜ Кланы", callback_data="synclan")
    job = InlineKeyboardButton("💼 Работы", callback_data="synjob")
    chat = InlineKeyboardButton("💬 Чаты", callback_data="synchat")
    stock_market = InlineKeyboardButton("⚖️ Биржа", callback_data="synstock_market")
    mary = InlineKeyboardButton("💝 Браки", callback_data="synmary")
    stat = InlineKeyboardButton("📊 Статистика", callback_data="synstat")
    other = InlineKeyboardButton("ℹ️ Другое", callback_data="synother")
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(main)
    floor.row(rate, nick)
    floor.row(pref, bal)
    floor.row(games, promo)
    floor.row(clan, job)
    floor.row(chat, stock_market)
    floor.row(mary, stat)
    floor.add(other)
    await call.message.edit_text("""<b>🗒 Список синонимов:</b>

⚜ | Главное
🏆 | Рейтинг
🏷 | Ники
🔰 | Префиксы
💰 | Баланс
🎮 | Игры
🎁 | Промокоды
⚜ | Кланы
💼 | Работы
💬 | Чаты
⚖️ | Биржа
💝 | Браки
📊 | Статистика
ℹ️ | Другое""", parse_mode="HTML", reply_markup=floor)



@dp.callback_query_handler(text=['synmain'])
async def main_syns(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>⚜ Главное:</b>

/start - перезапустить бота

/help - помощь
/info

/profile - профиль
/prof

/commands - список команд
/comm

/synonyms - список синонимов
/syn

/ckb - очистить клавиатуру""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['synrate'])
async def rate_syns(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>🏆 Рейтинг:</b>

/top - рейтинги
/rate

/clan_top - рейтинги кланов
/clan_rate

/jobtop - рейтинги работ
/worktop
/workertop

/balance_top - рейтинг по балансу
/btop

/point_top - рейтинг по очкам
/ptop

/eclair_top - рейтинг по эклерам
/ectop

/coin_top - рейтинг по монетам
/ctop

/chapcha_top - рейтинг по чапчам
/chtop

/freebas_top - рейтинг по фрибасам
/ftop

/reputation_top - рейтинг по репутации
/rtop

/clan_chapcha_top - рейтинг кланов по чапчам
/clanchtop

/clan_freebas_top - рейтинг кланов по фрибасам
/clanftop

/clan_reputation_top - рейтинг кланов по репутации
/clanrtop

/architect_top - рейтинг по архитекторам
/artop

/bloger_top - рейтинг по блогерам
/bltop

/builder_top - рейтинг по строителям
/butop

/miner_top - рейтинг по шахтерам
/mitop

/developer_top - рейтинг по разработчикам
/devtop

/cybersportsman_top - рейтинг по киберспортсменам
/csportop

/farmer_top - рейтинг по фермерам
/fatop

/killer_top - рейтинг по киллерам
/kitop

/programmer_top - рейтинг по программистам
/progtop

/teacher_top - рейтинг по учителям
/tetop""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['synnick'])
async def nick_syns(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>🏷 Ники:</b>

/nick - ник

/newnick Ник - сменить ник

/mynicks - мешок ников

/getnick Ник - добавить ник в мешок

/delnick Ник - удалить ник из мешка

/auction - аукцион ников
/auc

/sellnick Ник - выставить ник на продажу

/buynick Ник - купить ник

/wfs - снять ник с продажи""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['synpref'])
async def pref_syns(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>🔰 Префиксы:</b>

/prefixes - список префиксов
/pref

/myprefix - префикс
/mypref

/buyprefix Префикс - купить префикс""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['synbal'])
async def bal_syns(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>💰 Баланс:</b>

/balance - баланс
/b

/cv - курс валют

/buyeclairs Число - купить эклеры

/buycoins Число - купить монеты

/buyfreebases Число - купить фрибасы

/buychapchas Число - купить чапчи

/transfer ID Число - перевести эклеры""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['syngames'])
async def games_syns(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>🎮 Игры:</b>

/games - список игр

/clicker - кликер
/cl

/farm - фарм
/farming

<code>Кубик</code> Число Ставка - кубик

<code>Рулетка</code> Число Ставка - рулетка

<code>Дартс</code> Число Ставка - дартс

<code>Кража</code> ID/@ссылка/рандом - ограбление
<code>Ограбление</code> ID/@ссылка/рандом - ограбление

<code>Открыть</code> Кейс - открыть кейс

<code>!Кнопки</code> - поиск кнопки
<code>!Кнопка</code>
<code>Поиск кнопки</code>
<code>Кнопки игра</code>
<code>Игра кнопки</code>
<code>Кнопка игра</code>
<code>Игра кнопка</code>
<code>Найди кнопку</code>
<code>Найти кнопку</code>

/upgrades - улучшения
/ups""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['synpromo'])
async def promo_syns(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>🎁 Промокоды:</b>

/promo - доступные промокоды
/ap Промокод - активировать промокод""", parse_mode="HTML", reply_markup=floor)


@dp.callback_query_handler(text=['synclan'])
async def clan_syns(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>⚜ Кланы:</b>

<code>Создать клан</code> Название
Описание - создать клан

<code>Удалить клан</code> - удалить клан

<code>Клан</code> - Просмотреть информацию о клане
<code>Мой клан</code>

<code>Вступить в клан</code> ID - вступить в клан

<code>Покинуть клан</code> ID - покинуть клан

<code>Выгнать из клана</code> ID - выгнать участника из клана

<code>Вложить чапчи</code> Число - вложить чапчи в клан
<code>Вкинуть чапчи</code> Число

<code>Вложить фрибасы</code> Число - вложить фрибасы в клан
<code>Вкинуть фрибасы</code> Число

<code>Клан баланс</code> - баланс клана
<code>Баланс клана</code>

/clan_prefixes - префиксы кланов
/clanpref

/buy_clan_prefix Префикс - купить префикс для клана

/clan_prefix - префикс клана
/my_clan_prefix""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['synjob'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>💼 Работы:</b>

<code>!работы</code> - работы
<code>!ворки</code>
/jobs
/j

<code>+работа</code> Профессия - устроиться на работу
<code>+профессия</code> Профессия
<code>+ворк</code> Профессия

<code>-работа</code> - уволиться
<code>-профессия</code>
<code>-ворк</code>

<code>!работа</code> - рабочая статистика
<code>!профессия</code>
<code>!ворк</code>

<code>!работать</code> - работать
<code>!воркинг</code>
<code>!праця</code>""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['synchat'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>💬 Чаты:</b>

<code>Установка приветствия</code> - инструкция по установке приветствия
<code>Установка приветствий</code>

<code>+приветствие</code> Текст Число/Ссылка - установить приветствие

<code>-приветствие</code> - удалить приветствие

<code>!приветствие</code> - посмотреть приветствие

<code>+правила</code> Текст - установить правила

<code>-правила</code> - удалить правила

<code>!правила</code> - посмотреть правила""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['synother'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>ℹ️ Другое:</b>

/bad_words - ответы на плохие слова

/msg ID Текст - отправить сообщение пользователю через бота

<code>Чапча реши</code> Пример - решение примера
<code>Чапча решай</code> Пример

<code>Чапча выбери</code> Текст или Текст - выбор текста
<code>Чапча выбирай</code> Текст или Текст

<code>Чапча выбери от</code> Число1 до Число2 - выбор числа от Числа1 до Числа2
<code>Чапча выбирай от</code> Число1 до Число2

<code>Чапча анекдот</code> - анекдот
<code>Чапча расскажи анекдот</code>
<code>Чапча пошути</code>
<code>Чапча расскажи шутку</code>

<code>Чапча книга рецептов</code> - книга рецептов
<code>Чапча рецепты</code>

<code>Чапча рецепт</code> Блюда - рецепт блюда
<code>Чапча</code> Блюдо

<code>Чапча действия</code> - список действий
<code>Дейтсвия</code>""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['synstock_market'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>⚖️ Биржа:</b>

<code>Биржа</code> - биржа
<code>Рынок</code>
<code>Чап-биржа</code>
<code>Чап-рынок</code>

<code>Продать чапчи</code> Число Цена (за все) - продать чапчи
<code>Пополнить биржу</code> Число Цена (за все)
<code>Пополнить рынок</code> Число Цена (за все)

<code>Купить чапчи</code> ID - купить чапчи
<code>Чапчи купить</code> ID

<code>Заказать чапчи</code> Число Цена (за 1 чапчу) - заказать чапчи
<code>Биржа заказ</code> Число Цена (за 1 чапчу)
<code>Чапчи заказать</code> Число Цена (за 1 чапчу)
<code>Заказ биржа</code> Число Цена (за 1 чапчу)
<code>Биржа заказать</code> Число Цена (за 1 чапчу)
<code>Чапчи заказ</code> Число Цена (за 1 чапчу)
<code>Заказ чапчи</code> Число Цена (за 1 чапчу)

<code>Мой заказ</code> - просмотреть заказ
<code>Заказ</code>

<code>Биржа снять</code> - убрать чапчи с биржи
<code>Снять чапчи</code>
<code>Чапчи снять</code>
<code>Убрать чапчи</code>

<code>Заказ снять</code> - удалить заказ
<code>Снять заказ</code>
<code>Убрать заказ</code>""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['synmary'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>💝 Браки:</b>

<code>Мой брак</code> - статистика брака
<code>!брак</code>

<code>+Брак</code> <i>(в ответ на сообщение)</i> - вступить в брак

<code>!Развод</code> - подать на развод

<code>Сделать подарок</code> Число <i>(1-100)</i> - сделать подарок""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['synstat'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtosynlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>📊 Статистика:</b>

<code>Реглист</code> - число регистраций
<code>Сколько юзеров у Чапчи</code>

<code>Оценка Чапчи</code> - средняя оценка Чапчи
<code>Стата Чапчи</code>
<code>Средний балл Чапчи</code>

<code>Оставить отзыв</code> Текст <i>(1-250 символов)</i> - оставить отзыв
<code>+отзыв</code>

<code>Оставить оценку</code> - оценить Чапчу
<code>+оценка</code>

<code>Удалить отзыв</code> - удалить отзыв
<code>-отзыв</code>

<code>Удалить оценку</code> - удалить оценку
<code>-оценка</code>

<code>Мой отзыв</code> - отзыв
<code>Моя оценка</code>
<code>!отзыв</code>
<code>!оценка</code>""", parse_mode="HTML", reply_markup=floor)