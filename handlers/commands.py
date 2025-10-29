from aiogram import types
from dispatcher import dp
from aiogram.types import InputFile, ContentType, Message, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.callback_query import CallbackQuery

@dp.message_handler(commands=['commands', 'comm'])
async def commands(message: types.Message):
    main = InlineKeyboardButton("⚜ Главное", callback_data="main")
    rate = InlineKeyboardButton("🏆 Рейтинг", callback_data="rate")
    nick = InlineKeyboardButton("🏷 Ники", callback_data="nick")
    pref = InlineKeyboardButton("🔰 Префиксы", callback_data="pref")
    bal = InlineKeyboardButton("💰 Баланс", callback_data="bal")
    games = InlineKeyboardButton("🎮 Игры", callback_data="games")
    promo = InlineKeyboardButton("🎁 Промокоды", callback_data="promo")
    clan = InlineKeyboardButton("⚜ Кланы", callback_data="clan")
    job = InlineKeyboardButton("💼 Работы", callback_data="job")
    chat = InlineKeyboardButton("💬 Чаты", callback_data="chat")
    stock_market = InlineKeyboardButton("⚖️ Биржа", callback_data="stock_market")
    mary = InlineKeyboardButton("💝 Браки", callback_data="mary")
    stat = InlineKeyboardButton("📊 Статистика", callback_data="stat")
    other = InlineKeyboardButton("ℹ️ Другое", callback_data="other")
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(main)
    floor.row(rate, nick)
    floor.row(pref, bal)
    floor.row(games, promo)
    floor.row(clan, job)
    floor.row(chat, stock_market)
    floor.row(mary, stat)
    floor.add(other)
    await message.answer("""<b>🗒 Список команд:</b>

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

@dp.callback_query_handler(text=['backtocommlistbtn'])
async def back_to_commands(call: types.CallbackQuery):
    main = InlineKeyboardButton("⚜ Главное", callback_data="main")
    rate = InlineKeyboardButton("🏆 Рейтинг", callback_data="rate")
    nick = InlineKeyboardButton("🏷 Ники", callback_data="nick")
    pref = InlineKeyboardButton("🔰 Префиксы", callback_data="pref")
    bal = InlineKeyboardButton("💰 Баланс", callback_data="bal")
    games = InlineKeyboardButton("🎮 Игры", callback_data="games")
    promo = InlineKeyboardButton("🎁 Промокоды", callback_data="promo")
    clan = InlineKeyboardButton("⚜ Кланы", callback_data="clan")
    job = InlineKeyboardButton("💼 Работы", callback_data="job")
    chat = InlineKeyboardButton("💬 Чаты", callback_data="chat")
    stock_market = InlineKeyboardButton("⚖️ Биржа", callback_data="stock_market")
    mary = InlineKeyboardButton("💝 Браки", callback_data="mary")
    stat = InlineKeyboardButton("📊 Статистика", callback_data="stat")
    other = InlineKeyboardButton("ℹ️ Другое", callback_data="other")
    floor = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(main)
    floor.row(rate, nick)
    floor.row(pref, bal)
    floor.row(games, promo)
    floor.row(clan, job)
    floor.row(chat, stock_market)
    floor.row(mary, stat)
    floor.add(other)
    await call.message.edit_text("""<b>🗒 Список команд:</b>

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



@dp.callback_query_handler(text=['main'])
async def main_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>⚜ Главное:</b>

/start - перезапустить бота
/help - помощь
/profile - профиль
/commands - список команд
/synonyms - список синонимов
/ckb - очистить клавиатуру""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['rate'])
async def rate_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>🏆 Рейтинг:</b>

/top - рейтинги
/clan_top - рейтинги кланов
/jobtop - рейтинги работ

/balance_top - рейтинг по балансу
/point_top - рейтинг по очкам
/eclair_top - рейтинг по эклерам
/coin_top - рейтинг по монетам
/chapcha_top - рейтинг по чапчам
/freebas_top - рейтинг по фрибасам
/reputation_top - рейтинг по репутации

/clan_chapcha_top - рейтинг кланов по чапчам
/clan_freebas_top - рейтинг кланов по фрибасам
/clan_reputation_top - рейтинг кланов по репутации

/architect_top - рейтинг по архитекторам
/bloger_top - рейтинг по блогерам
/builder_top - рейтинг по строителям
/miner_top - рейтинг по шахтерам
/developer_top - рейтинг по разработчикам
/cybersportsman_top - рейтинг по киберспортсменам
/farmer_top - рейтинг по фермерам
/killer_top - рейтинг по киллерам
/programmer_top - рейтинг по программистам
/teacher_top - рейтинг по учителям""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['nick'])
async def nick_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>🏷 Ники:</b>

/nick - ник
/newnick Ник - сменить ник
/mynicks - мешок ников
/getnick Ник - добавить ник в мешок
/delnick Ник - удалить ник из мешка
/auction - аукцион ников
/sellnick Ник - выставить ник на продажу
/buynick Ник - купить ник
/wfs - снять ник с продажи""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['pref'])
async def pref_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>🔰 Префиксы:</b>

/prefixes - список префиксов
/myprefix - префикс
/buyprefix Префикс - купить префикс""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['bal'])
async def bal_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>💰 Баланс:</b>

/balance - баланс
/cv - курс валют
/buyeclairs Число - купить эклеры
/buycoins Число - купить монеты
/buyfreebases Число - купить фрибасы
/buychapchas Число - купить чапчи
/transfer ID Число - перевести эклеры""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['games'])
async def games_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>🎮 Игры:</b>

/games - список игр
/clicker - кликер
/farm - фарм
<code>Кубик</code> Число Ставка - кубик
<code>Рулетка</code> Число Ставка - рулетка
<code>Дартс</code> Число Ставка - дартс
<code>Кража</code> ID/@ссылка/рандом - ограбление
<code>Открыть</code> Кейс - открыть кейс
<code>!кнопки</code> - поиск кнопки
/upgrades - улучшения""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['promo'])
async def promo_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>🎁 Промокоды:</b>

/promo - доступные промокоды
/ap Промокод - активировать промокод""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['clan'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>⚜ Кланы:</b>

<code>Создать клан</code> Название
Описание - создать клан
<code>Удалить клан</code> - удалить клан
<code>Клан</code> - Просмотреть информацию о клане
<code>Вступить в клан</code> ID - вступить в клан
<code>Покинуть клан</code> ID - покинуть клан
<code>Выгнать из клана</code> ID - выгнать участника из клана
<code>Вложить чапчи</code> Число - вложить чапчи в клан
<code>Вложить фрибасы</code> Число - вложить фрибасы в клан
<code>Клан баланс</code> - баланс клана
/clan_prefixes - префиксы кланов
/buy_clan_prefix Префикс - купить префикс для клана
/clan_prefix - префикс клана""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['job'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>💼 Работы:</b>

<code>!работы</code> - работы
<code>+работа</code> Профессия - устроиться на работу
<code>-работа</code> - уволиться
<code>!работа</code> - рабочая статистика
<code>!работать</code> - работать""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['chat'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>💬 Чаты:</b>

<code>Установка приветствия</code> - инструкция по установке приветствия
<code>+приветствие</code> Текст Число/Ссылка - установить приветствие
<code>-приветствие</code> - удалить приветствие
<code>!приветствие</code> - посмотреть приветствие
<code>+правила</code> Текст - установить правила
<code>-правила</code> - удалить правила
<code>!правила</code> - посмотреть правила""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['other'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>ℹ️ Другое:</b>

/bad_words - ответы на плохие слова
/msg ID Текст - отправить сообщение пользователю через бота
<code>Чапча реши</code> Пример - решение примера
<code>Чапча выбери</code> Текст или Текст - выбор текста
<code>Чапча выбери от</code> Число1 до Число2 - выбор числа от Числа1 до Числа2
<code>Чапча анекдот</code> - анекдот
<code>Чапча книга рецептов</code> - книга рецептов
<code>Чапча рецепт</code> Блюда - рецепт блюда
<code>Чапча действия</code> - список действий""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['stock_market'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>⚖️ Биржа:</b>

<code>Биржа</code> - биржа
<code>Продать чапчи</code> Число Цена (за все) - продать чапчи
<code>Купить чапчи</code> ID - купить чапчи
<code>Заказать чапчи</code> Число Цена (за 1 чапчу) - заказать чапчи
<code>Мой заказ</code> - просмотреть заказ
<code>Биржа снять</code> - убрать чапчи с биржи
<code>Заказ снять</code> - удалить заказ""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['mary'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>💝 Браки:</b>

<code>Мой брак</code> - статистика брака
<code>+Брак</code> <i>(в ответ на сообщение)</i> - вступить в брак
<code>!Развод</code> - подать на развод
<code>Сделать подарок</code> Число <i>(1-100)</i> - сделать подарок""", parse_mode="HTML", reply_markup=floor)

@dp.callback_query_handler(text=['stat'])
async def clan_comms(call: types.CallbackQuery):
    btclb = InlineKeyboardButton("⬅️ Назад", callback_data="backtocommlistbtn")
    floor = InlineKeyboardMarkup(resize_keyboard=True).add(btclb)
    await call.message.edit_text("""<b>📊 Статистика:</b>

<code>Реглист</code> - число регистраций
<code>Оценка Чапчи</code> - средняя оценка Чапчи
<code>Оставить отзыв</code> Текст <i>(1-250 символов)</i> - оставить отзыв
<code>Оставить оценку</code> - оценить Чапчу
<code>Удалить отзыв</code> - удалить отзыв
<code>Удалить оценку</code> - удалить оценку
<code>Мой отзыв</code> - отзыв""", parse_mode="HTML", reply_markup=floor)