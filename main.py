from aiogram import Bot, Dispatcher, executor, types
import markups as nav
#import kurs as cur

# '5068390376:AAG9AsljUmaSPJY9MQKowODilmZiVYfTUTY'
#TOKEN = '5090944343:AAHgzeqLCwyQhhfD_j1Hh9Xv0PSBZ09eKUg' original
TOKEN = '5090944343:AAHgzeqLCwyQhhfD_j1Hh9Xv0PSBZ09eKUg'

bot=Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вас приветствует АО "БАНК ОРЕНБУРГ"💙 в нашем боте-консультаньте, Вы можете:\n\n 🔹 Узнать об актуальных продуктах Банка;\n\n 🔹 Получить информацию о новых акциях Банка;\n\n 🔹 Узнать контакты для дополнительной связи и режим работы офисов \n\n Быстро. Просто. Доступно. \n\n Выберите интересующий Вас продукт в МЕНЮ 🔽🔽🔽 \n В Web-версии для открытия меню необходимо навести на иконку слева от 📎'.format(message.from_user),reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    #ВЕТКА КРЕДИТОВ
    if message.text == '🚩Кредиты':
        await bot.send_message(message.from_user.id, '🚩Выберите вид кредитного продукта, в завивисмости от вашей цели:\n➖➖➖➖\n🔻🔻🔻⤵️', reply_markup=nav.OtherMenu)

    #Потребительские кредиты блок
    elif message.text == '💎Потребительские кредиты':
        await bot.send_message(message.from_user.id,'🔥ПОТРЕБИТЕЛЬСКИЙ КРЕДИТ ОТ 7.00%\n➖➖➖➖➖\n🔵Выберите категорию потребительского кредита:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup= nav.OtherMenu_1)
    elif message.text == '👷‍♂️Кредит для работающих':
        await bot.send_message(message.from_user.id,'👷‍♂️ПОТРЕБИТЕЛЬСКИЙ КРЕДИТ ДЛЯ РАБОТАЮЩИХ\n\n 🎯 Цель - на любые цели\n\n 📍 Ставка от 7,00% до 16,75%\n\n 🕑 Срок от 6 до 120 месяцев\n\n❌ БЕЗ СТРАХОВОК И КОМИССИЙ!\n\n🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документ, подтверждающий доход (2-НДФЛ/СЗИ-ИЛС/Выписка по зарплатному счёту).\n\n📲 ПОДАТЬ ОНЛАЙН-ЗАЯВКУ НА КРЕДИТ ПРОЩЕ И БЫСТРЕЕ НА САЙТЕ ➡️ https://orbank.ru/#credit-online \n\n Доверяй своим!💙')
    elif message.text == '👨Кредит для пенсионеров':
        await bot.send_message(message.from_user.id,'👨ПОТРЕБИТЕЛЬСКИЙ КРЕДИТ ДЛЯ ПЕНСИОНЕРОВ\n\n 🎯 Цель - на любые цели\n\n 📍 Ставка от 11,65% до 14,65%\n\n 🕑 Срок от 6 до 60 месяцев\n\n❌ БЕЗ СТРАХОВОК И КОМИССИЙ!\n\n🔹Документы для подачи заявки:\n\n▫️ Паспорт;\n▫️ СНИЛС;\n▫️️️Документ, подтверждающий доход (Справка ПФР/СЗИ-ИЛС/Выписка по зарплатному счёту).\n\n📲 ПОДАТЬ ОНЛАЙН-ЗАЯВКУ НА КРЕДИТ ПРОЩЕ И БЫСТРЕЕ НА САЙТЕ ➡️ https://orbank.ru/#credit-online \n\n Доверяй своим!💙')
    elif message.text == '🔖Акция! Честный процент':
        await bot.send_message(message.from_user.id,'🔖АКЦИЯ "Честный процент"\n\n 🎯 Цель - на любые цели и рефинансирование\n\n 📍 Ставка 13,50%\n\n 🕑 Срок от 6 до 60 месяцев\n\n❌ БЕЗ СТРАХОВОК И КОМИССИЙ!\n\n🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документ, подтверждающий доход (2-НДФЛ/СЗИ-ИЛС/Выписка по зарплатному счёту/Справка ПФР).\n\n📲 ПОДАТЬ ОНЛАЙН-ЗАЯВКУ НА КРЕДИТ ПРОЩЕ И БЫСТРЕЕ НА САЙТЕ ➡️ https://orbank.ru/#credit-online \n\n Доверяй своим!💙')
    elif message.text == '💳Кредитная карта':
        await bot.send_message(message.from_user.id,'💳Кредитная карта\n\n 🎯 Цель - на любые цели\n\n 📍 Ставка от 15,9% до 17,9%\n\n Срок до 730 дней\n\n📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://orbank.ru/#credit-online \n\n Доверяй своим!💙')
    elif message.text == 'Вернуться в меню "🚩Кредиты"':
        await bot.send_message(message.from_user.id, 'Вы вернулись в меню 🚩Кредиты ', reply_markup=nav.OtherMenu)

    #Рефинансирование_блок

    elif message.text == '🔄Рефинансирование кредитов':
        await bot.send_message(message.from_user.id,'🔹РЕФИНАНСИРОВАНИЕ КРЕДИТОВ ОТ 7,00%\n➖➖➖➖➖\n🔵Выберите категорию рефинансирования:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup= nav.OtherMenu_ref)
    elif message.text == '👷‍♂Рефинансирование кредитов работающим клиентам':
        await bot.send_message(message.from_user.id,'👨Рефинансирование кредитов для РАБОТАЮЩИХ КЛИЕНТОВ\n\n 🎯 Цель - Рефинансирование кредитов\n\n 📍 Ставка от 7,00% до 15,95%\n\n 🕑 Срок от 6 до 60 месяцев\n\n❌ БЕЗ СТРАХОВОК И КОМИССИЙ!\n\n🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документ, подтверждающий доход (2-НДФЛ/СЗИ-ИЛС/Выписка по зарплатному счёту).\n ▫️ Справка об остатке долга по рефинансируемому кредиту\n\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://orbank.ru/#credit-online \n\n Доверяй своим!💙')
    elif message.text == '👨Рефинансирование кредитов пенсионерам':
        await bot.send_message(message.from_user.id,'👨Рефинансирование кредитов для ПЕНСИОНЕРОВ\n\n 🎯 Цель - Рефинансирование кредитов\n\n 📍 Ставка от 11,55% до 14,55%\n\n 🕑 Срок от 6 до 60 месяцев\n\n❌ БЕЗ СТРАХОВОК И КОМИССИЙ!\n\n🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документ, подтверждающий доход (Справка ПФР/СЗИ-ИЛС/Выписка по зарплатному счёту).\n ▫️ Справка об остатке долга по рефинансируемому кредиту\n\n📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://orbank.ru/#credit-online \n\n Доверяй своим!💙')

    #Ипотека

    elif message.text == '🏡Ипотека':
        await bot.send_message(message.from_user.id,'🔹ИПОТЕКА ОТ 4,4%\n➖➖➖➖➖\n🔵Выберите ипотечный продукт:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup=nav.OtherMenu_mort)
    elif message.text == 'Покупка квартиры':
        await bot.send_message(message.from_user.id,'🏙 Покупка квартиры \n\n 🎯 Цель - Покупка кватиры на первичном или вторичном рынке \n\n 📍 Ставка от 6,5% до 11,60% \n\n 🕑 Срок от 3 до 30 лет \n\n 🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документы, подтверждающие доход (2-НДФЛ/СЗИ-ИЛС/Выписка по зарплатному счёту);\n ▫️ иные документы при запросе менеджера.\n\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://orbank.ru/#ipoteka-online')
    elif message.text == 'Рефинансирование ипотеки':
        await bot.send_message(message.from_user.id,'♻️ Рефинансирование ранее оформленной ипотеки \n\n 🎯 Цель - Рефинансирование ипотечного кредита \n\n 📍 Ставка от 6,55% до 12,05% \n\n 🕑 Срок от 3 до 30 лет \n\n 🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документы, подтверждающие доход (2-НДФЛ/СЗИ-ИЛС/Выписка по зарплатному счёту);\n ▫️ Документу о рефинансируемом кредите(справка об остатке ссудной задолженности, кредитный договор,график платежей);\n ▫️ иные документы при запросе менеджера.\n\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://orbank.ru/#ipoteka-online')
    elif message.text == 'Покупка/строительство дома':
        await bot.send_message(message.from_user.id,'🏡 Кредит на покупку/строительства дома \n\n 🎯 Цель - Покупка/строительство дома\n\n 📍 Ставка от 7,50% до 12,15% \n\n 🕑 Срок от 3 до 30 лет \n\n 🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документы, подтверждающие доход (2-НДФЛ/СЗИ-ИЛС/Выписка по зарплатному счёту)\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://orbank.ru/#ipoteka-online')
    elif message.text == 'Ипотека с гос.поддержкой':
        await bot.send_message(message.from_user.id,'🇷🇺 Ипотека с гос.поддержкой \n\n 🎯 Цель - Приоберитение у юридического лица/ИП квартиры/дома/ОНС\n\n 📍 Ставка от 6,95% до 7,95% \n\n 🕑 Срок от 3 до 30 лет \n\n 🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документы, подтверждающие доход (2-НДФЛ)\n\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://orbank.ru/#ipoteka-online')
    elif message.text == 'Семейная ипотека':
        await bot.send_message(message.from_user.id,'👪 Семейная ипотека \n\n 🎯 Цель - Приобретение у юридического лица недвижимости или рефинансирование ипотечного кредита, ранее взятого на аналогичные цели\n\n 📍 Ставка 4,95% \n\n 🕑 Срок от 3 до 30 лет \n\n 🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документы, подтверждающие доход (2-НДФЛ)\n\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://orbank.ru/#ipoteka-online')
    elif message.text == 'IT Ипотека':
        await bot.send_message(message.from_user.id,'💻 IT Ипотека\n\n 🎯 Цель - Приобретение у юридического лица недвижимости физическими лицами  основным местом работы которых является организация,которая осуществляет деятельность в области информационных технологий и имеет аккредитацию Минцифры России\n\n 📍 Ставка 4,40% \n\n 🕑 Срок от 3 до 30 лет \n\n 📈 Максимальная сумма кредита - 18 млн руб. \n\n🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документы, подтверждающие доход\n\n 📲 ПОДАТЬ ОНЛАЙН-ЗАЯВКУ НА КРЕДИТ ПРОЩЕ И БЫСТРЕЕ НА САЙТЕ ➡️ https://orbank.ru/#ipoteka-online')

    #Кредит для самозанятых

    elif message.text == '👨‍💻Кредит самозанятым':
        await bot.send_message(message.from_user.id,'👨‍💻 Кредит "Старт" для самозанятых \n\n 🎯 Цель - на любые цели или рефинансирование, имеющихся кредитов\n\n📍 Ставка от 17,45% до 18,95%\n\n 🕑 Срок от6 до 60 месяцев\n\n 📲 ПОДАТЬ ОНЛАЙН-ЗАЯВКУ НА КРЕДИТ ПРОЩЕ И БЫСТРЕЕ НА САЙТЕ ➡️ https://orbank.ru/#credit-online')

    # Вклад

    elif message.text == '🛡Вклады':
        await bot.send_message(message.from_user.id, '✨Вклады с доходностью до 8,50%\n➖➖➖➖➖\n🔹Выберите интересующий вас сберегательный продукт:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup=nav.OffOnMenu)

    elif message.text == '☕️Вклады в офисах Банка':
        await bot.send_message(message.from_user.id,'🔥Ставка по вкладу до 8.50%\n➖➖➖➖➖\n🔵Выберите интересующий Вас продукт:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup = nav.Offline_deposit)
    elif message.text == '🤝Правильный выбор':
        await bot.send_message(message.from_user.id,'🔑Вклад "Правильный выбор"\n\n▫️Доходность до 5,5%\n\n▫️Срок вклада 837 дней\n\n▫️Пополняемый с 94 дня')
    elif message.text == '🌄Новый горизонт':
        await bot.send_message(message.from_user.id,'🔑Вклад "Доходный"▫️Доходность до 5,10%\n\n️▫️️Срок вклада 1 080 дней\n\n️▫️️Сумма от 10 000 руб.\n\n▫️Пополняймый в течении 180 дней')
    elif message.text == '👨Пенсионный':
        await bot.send_message(message.from_user.id, '🔑Вклад "Пенсионный"▫️Доходность до 5,25%\n\n️▫️️Срок вклада 1 140 дней\n\n️▫️️Сумма от 5 000 руб.\n\n▫Пополняемый в течении 180 дней')
    elif message.text == '⛰Олимп':
        await bot.send_message(message.from_user.id, '🔑Вклад "Олимп"▫️Доходность до 8,50%\n\n️▫️️Срок вклада 1 170 дней\n\n️▫️️Сумма от 3 000 000 руб.\n\n▫Пополняемый в течении 390 дней')
    elif message.text == 'Вернуться в меню "🛡Вклады"':
        await bot.send_message(message.from_user.id, 'Вы вернулись в меню вклады 🛡Вклады', reply_markup=nav.OffOnMenu)

    elif message.text == '📲Вклады онлайн':
        await bot.send_message(message.from_user.id,'🔥Ставка по вкладу до 8.00%\n➖➖➖➖➖\n🔵Выберите интересующий Вас продукт:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup= nav.Online_deposit)
    elif message.text == '📲Правильный выбор онлайн':
        await bot.send_message(message.from_user.id,'🔑Вклад "Правильный выбор ОНЛАЙН"\n\n▫️Доходность до 6%\n\n️▫️️Срок вклада 837 дней\n\n️▫️️Сумма от 10 000 руб.\n\n▫️Пополняемый с 94 дня\n\n🔹ОТКРЫТЬ ВКЛАД МОЖНО В ПРИЛОЖЕНИИ БАНКА')
    elif message.text == '🚀Онл@йн':
        await bot.send_message(message.from_user.id,'🔑Вклад "Онл@йн"▫️Доходность до 5,50%\n\n️▫️️Срок вклада 370 дней\n\n️▫️️Сумма от 5 000 руб.\n\n▫️Пополняемый в течении 180 дней\n\n🔹ОТКРЫТЬ ВКЛАД МОЖНО В ПРИЛОЖЕНИИ БАНКА')

    elif message.text == '🗄 Счета':
        await bot.send_message(message.from_user.id,'🔥Ставка по счёту "Накопительный" до 7.00%\n➖➖➖➖➖\n🔵Выберите интересующий Вас продукт:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup= nav.money_box_menu)
    elif message.text == '🗄 Накопительный счёт':
        await bot.send_message(message.from_user.id,'🔑Счёт "Накопительный" до 7.00%\n➖➖➖➖➖\n 📍 Пополняемый без ограничений :\n➖ Открыть можно в офисе Банка\n➖ Открыть можно онлайн 🔻🔻🔻⤵️\n', reply_markup= nav.money_box_menu)

# Банковские карты
    elif message.text == '💳Карты':
        await bot.send_message(message.from_user.id, '💳Карты АО "БАНК ОРЕНБУРГ" позволяют комфортно и оперативно осущеставлять банковские операции\n➖➖➖➖➖\n🔹Выберите интересующий карточные продукты:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup=nav.Other_Menu_card)
    elif message.text == '🏞Карты МИР':
        await bot.send_message(message.from_user.id, '🌍Платёжная система «Мир» создана при поддержке государства с учетом особенностей российского финансового рынка и нацелена на обеспечение финансовой безопасности страны.\n➖➖➖➖➖\n🔹Выберите карту ПС МИР️:\n➖➖➖➖➖\n🔻🔻🔻⤵️',reply_markup= nav.OtherMenu_cardmir)
    elif message.text == 'Классическая карта МИР':
        await bot.send_message(message.from_user.id, '🌷Классическая карта МИР\n▫️ Карта позволяет без ограничений получать наличные, рассчитываться за товары и услуги, а также оплачивать покупки в Интернете.\n▫️ Срок действия - 5 лет \n▫️ CASHBACK ДО 10% ')
    elif message.text == 'Вернуться в меню 💳Карты':
        await bot.send_message(message.from_user.id, 'Вы вернулись в меню "💳Карты"', reply_markup = nav.Other_Menu_card)
    elif message.text == '🌇Карта Оренбуржца':
        await bot.send_message(message.from_user.id, '🔹 Карта Оренбуржца не ограничивает функционал услуг банка. Совершайте операции в банкоматах и пунктах выдачи наличных, оплачивайте товары и услуги, в том числе дистанционно.\n\n ⤴Приемущества карты:\n\n➖Многофункциональность: \n УКО включает в себя такие инструменты, как банковская, транспортная, социальная и скидочная карты, полис обязательного медицинского страхования, квалифицированная электронная подпись (КЭП), карта контрольно-пропускного пункта и пр.\n\n ➖ Безопасность\nПрименяются ключи безопасности, шифрующие персональные данные. Предусмотрен ПИН-код. При утере карту можно быстро заблокировать.\n\n➖Надёжность\n Проект разработан и поддерживается Правительством Оренбургской области.\n\n➖Базовые условия:\n🌀Выпуск карты — бесплатно;\n🌀Срок действия карты — 5 лет;\n🌀Информирование об операциях, совершённых с использованием банковской карты, — бесплатно;\n🌀Использование интернет-банка — бесплатно;\n🌀Карту могут оформить граждане РФ старше 14 лет;\n🌀Гражданин может иметь только одну действующую УКО.\n\n📁Необходимые документы:\n📎Паспорт\n📎СНИЛС\n📎 ОМС')

# Курсы валют

   # elif message.text == '💸Курсы валют в офисах г.Оренбург':
        #await bot.send_message(message.from_user.id,'🔵Выберите интересующую Вас валюту для конвертации в г.Оренбург\n➖➖➖➖➖\n🔻🔻🔻⤵️',reply_markup=nav.OtherMenu_curs)
    #elif message.text == '$ Покупка/Продажка':
        #await bot.send_message(message.from_user.id,'Курс в КАССАХ офисов г.Оренбурга\n\n' + '🔹Покупка $ = ' + str(cur.dollar_buy) + '\n\n♦️Продажа $ = ' + str(cur.dollar_sale)+'\n\n ⚫️ КОНВЕРТИРОВАТЬ ВАЛЮТУ ОНЛАЙН ВЫГОДНЕЕ - orbank.ru/internet/')
    #elif message.text == '€ Покупка/Продажа':
        #await bot.send_message(message.from_user.id,'Курс в КАССАХ офисов г.Оренбурга\n\n' +'🔹Покупка € = ' + str(cur.euro_buy) + '\n\n♦️Продажа € = ' + str(cur.euro_sale)+'\n\n ⚫️ КОНВЕРТИРОВАТЬ ВАЛЮТУ ОНЛАЙН ВЫГОДНЕЕ - orbank.ru/internet/')
    #elif message.text == 'Тенге Покупка/Продажа':
        #await bot.send_message(message.from_user.id,'Курс в КАССАХ офисов г.Оренбурга\n\n' + '🔹Покупка Тенге = ' + str(cur.tenge_buy) + '\n\n♦️Продажа Тенге = ' + str(cur.tenge_sale)+'\n\n ⚫️ КОНВЕРТИРОВАТЬ ВАЛЮТУ ОНЛАЙН ВЫГОДНЕЕ - orbank.ru/internet/')

    elif message.text == '☎️Офисы и контакты':
        await bot.send_message(message.from_user.id,'📞Получить консультацию можно по телефону: 373-000\n\n 🖥Обратная связь через сайт:https://orbank.ru/ \n\n Если вы хотите узнать режим работы воспользуйтесь меню ⤵️', reply_markup=nav.contact_menu)
    elif message.text == '☎️Вернуться в меню "Офисы и контакты':
        await bot.send_message(message.from_user.id, 'Вы вернулись в меню "Офисы и контакты"', reply_markup = nav.contact_menu)
    elif message.text == '🌇Офисы в г.Оренбурге':
        await bot.send_message(message.from_user.id, 'Для того, чтобы узнать режим работы офиса в г.Оренбурге выберите код-офиса и отправьте его боту:\n\n Код офиса:\n 1 > ул. Маршала Г. K. Жукова, д. 25 \n 2 > ул. Брестская, д. 5  \n 3 > ул. 8 Марта, д. 35 \n 4 > проспект Гагарина, д. 54/1 \n 5 > ул. Пролетарская, д. 261 \n 6 > ул. Салмышская, д. 48/2', reply_markup=nav.contact_menu)
    elif message.text == '1':
        await bot.send_message(message.from_user.id,'ул. Маршала Г. K. Жукова, д. 25 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 20:00 \n Суббота — с 09:00 до 15:00\n Без перерыва на обед \n Воскресенье — выходной день \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n Без перерыва на обед\n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '2':
        await bot.send_message(message.from_user.id,'ул. Брестская, д. 5 \n Режим работы: \n Обслуживание физических лиц:\n С 09:00 до 20:00 \n Суббота — с 09:00 до 15:00\n Без перерыва на обед \n Воскресенье — выходной день \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n С 13:00 до 14:00 - обед\n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '3':
        await bot.send_message(message.from_user.id,'ул. 8 Марта, д. 35 \n Режим работы: \n Обслуживание физических лиц:\n С 09:00 до 20:00 \n Суббота — с 09:00 до 15:00\n Без перерыва на обед \n Воскресенье — выходной день \n\n Обслуживание юридических лиц:\n С 09:00 до 19:00 \n Без перерыва на обед\n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '4':
        await bot.send_message(message.from_user.id,'проспект Гагарина, д. 54/1 \n Режим работы: \n Обслуживание физических лиц:\n С 09:00 до 20:00 \n Суббота — с 09:00 до 15:00\n Без перерыва на обед \n Воскресенье — выходной день \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n С 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '5':
        await bot.send_message(message.from_user.id,'ул. Пролетарская, д. 261 \n Режим работы: \n Обслуживание физических лиц:\n С 09:00 до 20:00 \n Суббота — с 09:00 до 15:00\n Без перерыва на обед \n Воскресенье — выходной день \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n С 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '6':
        await bot.send_message(message.from_user.id,'ул. Салмышская, д. 48/2  \n Режим работы: \n Обслуживание физических лиц:\n С 09:00 до 20:00 \n Суббота — с 09:00 до 15:00\n Без перерыва на обед \n Воскресенье — выходной день', reply_markup=nav.contact_menu)

    elif message.text == '🌄Офисы в Оренбургской области':
        await bot.send_message(message.from_user.id, 'Для того, чтобы узнать режим работы офиса в вашем населённом пункте выберите код-офиса и отправьте его боту:\n\n Код офиса:\n 10 > с. Александровка  \n 11 > с. Беляевка \n 12 > г. Бугуруслан \n 13 > г. Бузулук \n 14 > г. Гай \n 15 > с. Илек \n 16 > с.Кваркено \n 17 > г.Медногорск\n 18 > г.Орск\n 18 > п. Первомайский \n 19 > п. Переволоцкий \n 20 > с. Плешаново \n 21 > с. Сакмара \n 21 > с. Сакмара \n 21 > с. Сакмара \n 22 > п. Саракташ \n 23 > с. Северное \n 24 > г. Соль-Илецк \n 25 > г. Сорочинкс \n 26 > с. Ташла \n 27 > п. Тюльган \n 28 > г. Ясный', reply_markup=nav.contact_menu)
    elif message.text == '10':
        await bot.send_message(message.from_user.id,'с. Александровка, ул. Мичурина, д. 22 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 17:00 \n  с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '11':
        await bot.send_message(message.from_user.id,'с. Беляевка, ул. Советская, д. 61в \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 17:00 \n  с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '12':
        await bot.send_message(message.from_user.id,'г. Бугуруслан, ул. Революционная, д. 16 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 19:00 \n  Суббота — с 09:00 до 15:00 \n Без перерыва на обед \n Воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '13':
        await bot.send_message(message.from_user.id,'г. Бузулук, ул. Комсомольская, д. 113б \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 19:00 \n  Суббота — с 09:00 до 15:00 \n Без перерыва на обед \n Воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '14':
        await bot.send_message(message.from_user.id,'г. Гай, пр-т Победы, д. 7 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 19:00 \n  Суббота — с 09:00 до 15:00 \n Без перерыва на обед \n Воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '15':
        await bot.send_message(message.from_user.id,'с. Илек, ул. Уральская, д. 61 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 17:00 \n  с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '16':
        await bot.send_message(message.from_user.id,'с. Кваркено, ул. 1-я Целинная, д. 20\n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 17:00 \n  с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '17':
        await bot.send_message(message.from_user.id,'г. Орск, пр-т Ленина, д. 30 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 19:00 \n  Суббота — с 09:00 до 15:00 \n Без перерыва на обед \n Воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '18':
        await bot.send_message(message.from_user.id,'п. Первомайский, ул. Советская, д. 37 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 17:00 \n  с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '19':
        await bot.send_message(message.from_user.id,'п. Переволоцкий, ул. Ленинская, д. 125/1 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 17:00 \n  с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '20':
        await bot.send_message(message.from_user.id,'с. Плешаново, пр. Гагарина, д. 32 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 17:00 \n  с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '21':
        await bot.send_message(message.from_user.id,'с. Сакмара, ул. Советская, д. 32 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '22':
        await bot.send_message(message.from_user.id,'п. Саракташ,ул. Ленина, д. 29а \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '23':
        await bot.send_message(message.from_user.id,'с. Северное, ул. 40 лет Октября, д. 16в \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '24':
        await bot.send_message(message.from_user.id,'г. Соль-Илецк, ул. Пушкина, д. 12 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 19:00 \n  Суббота — с 09:00 до 15:00 \n Без перерыва на обед \n Воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '25':
        await bot.send_message(message.from_user.id,'г. Сорочинск, ул. Чапаева, д. 20 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 19:00 \n  Суббота — с 09:00 до 15:00 \n Без перерыва на обед \n Воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '26':
        await bot.send_message(message.from_user.id,'с. Ташла, ул. Молодёжная, д. 2 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '27':
        await bot.send_message(message.from_user.id,'п. Тюльган, ул. Пионерская, д. 10 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)
    elif message.text == '28':
        await bot.send_message(message.from_user.id,'г. Ясный, ул. Ленина, д. 9 \n Режим работы: \n Обслуживание физических лиц: \n С 09:00 до 19:00 \n  Суббота — с 09:00 до 15:00 \n Без перерыва на обед \n Воскресенье — выходные дни \n\n Обслуживание юридических лиц:\n С 09:00 до 17:00 \n с 13:00 до 14:00 - обед \n Суббота, воскресенье — выходные дни', reply_markup=nav.contact_menu)


    elif message.text == '🗞Новости':
        await bot.send_message(message.from_user.id,'Самые свежие новости о Банке, вы можете найти в наших социальных сетях: \n\n 🔹 VK - https://vk.com/bank_orenburg \n 🔹 TG-канал - @bankorenburg \n 🔹 Одноклассники - https://ok.ru/group/63202630041772 \n\n 🔹 Пресс-центр - https://orbank.ru/about/pressCenter/')


    elif message.text == '🗃Вернуться в главное меню':
        await bot.send_message(message.from_user.id, '🔹Вы вернулись в главное меню↩️\n➖➖➖➖➖\n🌀Выберете интересующую услугу️⤵️', reply_markup = nav.mainMenu)
    else:
        await bot.send_message(message.from_user.id, 'Я только учусь👨‍🎓, поэтому буду рад Вам помочь с помощью разделов моего меню⌨️\n\n🔹Вы вернулись в главное меню↩️\n➖➖➖➖➖\n🌀Выберете интересующую услугу️⤵️', reply_markup = nav.mainMenu)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates = True)
