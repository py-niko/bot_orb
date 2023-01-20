from aiogram import Bot, Dispatcher, executor, types
import markups as nav
#import kurs as cur

TOKEN = '5090944343:AAHgzeqLCwyQhhfD_j1Hh9Xv0PSBZ09eKUg'

bot=Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вас приветствует АО "БАНК ОРЕНБУРГ"💙'.format(message.from_user),reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    #ВЕТКА КРЕДИТОВ
    if message.text == '🚩Кредиты':
       #await bot.send_message(message.from_user.id,'🔹ПОТРЕБИТЕЛЬСКИЙ КРЕДИТ ОТ 7.77%\n➖➖➖➖➖\n 🔹Выберите интересующий Вас продукт 🔽🔽🔽')
        await bot.send_message(message.from_user.id, '🚩Выберите вид кредитного продукта, в завивисмости от вашей цели:\n➖➖➖➖\n🔻🔻🔻⤵️', reply_markup=nav.OtherMenu)

    #Потребительские кредиты блок
    elif message.text == '💎Потребительские кредиты':
        await bot.send_message(message.from_user.id,'🔥ПОТРЕБИТЕЛЬСКИЙ КРЕДИТ ОТ 7.00%\n➖➖➖➖➖\n🔵Выберите категорию потребительского кредита:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup= nav.OtherMenu_1)
    elif message.text == '👷‍♂️Кредит для работающих':
        await bot.send_message(message.from_user.id,'👷‍♂️ПОТРЕБИТЕЛЬСКИЙ КРЕДИТ ДЛЯ РАБОТАЮЩИХ\n\n 🎯 Цель - на любые цели\n\n 📍 Ставка от 7,00% до 18,45%\n\n 🕑 Срок от 6 до 120 месяцев\n\n❌ БЕЗ СТРАХОВОК И КОМИССИЙ!\n\n🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документ, подтверждающий доход (2-НДФЛ/СЗИ-ИЛС/Выписка по зарплатному счёту).\n\n📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys \n\n Доверяй своим!💙')
    elif message.text == '👨Кредит для пенсионеров':
        await bot.send_message(message.from_user.id,'👨ПОТРЕБИТЕЛЬСКИЙ КРЕДИТ ДЛЯ ПЕНСИОНЕРОВ\n\n 🎯 Цель - на любые цели\n\n 📍 Ставка от 11,75% до 15,35%\n\n 🕑 Срок от 6 до 60 месяцев\n\n❌ БЕЗ СТРАХОВОК И КОМИССИЙ!\n\n🔹Документы для подачи заявки:\n\n▫️ Паспорт;\n▫️ СНИЛС;\n▫️️️Документ, подтверждающий доход (Справка ПФР/СЗИ-ИЛС/Выписка по зарплатному счёту).\n\n📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys \n\n Доверяй своим!💙')
    elif message.text == '🔖Акция! Честный процент':
        await bot.send_message(message.from_user.id,'🔖АКЦИЯ "Честный процент"\n\n 🎯 Цель - на любые цели и рефинансирование\n\n 📍 Ставка 13,50%\n\n 🕑 Срок от 6 до 60 месяцев\n\n❌ БЕЗ СТРАХОВОК И КОМИССИЙ!\n\n🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документ, подтверждающий доход (2-НДФЛ/СЗИ-ИЛС/Выписка по зарплатному счёту/Справка ПФР).\n\n📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys \n\n Доверяй своим!💙')
    elif message.text == '💳Кредитная карта':
        await bot.send_message(message.from_user.id,'💳Кредитная карта\n\n 🎯 Цель - на любые цели\n\n 📍 Ставка от 15,9% до 17,9%\n\n Срок до 730 дней\n\n📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys \n\n Доверяй своим!💙')
    elif message.text == 'Вернуться в меню "🚩Кредиты"':
        await bot.send_message(message.from_user.id, 'Вы вернулись в меню 🚩Кредиты ', reply_markup=nav.OtherMenu)

    #Рефинансирование_блок

    elif message.text == '🔄Рефинансирование кредитов':
        await bot.send_message(message.from_user.id,'🔹РЕФИНАНСИРОВАНИЕ КРЕДИТОВ ОТ 7,00%\n➖➖➖➖➖\n🔵Выберите категорию рефинансирования:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup= nav.OtherMenu_ref)
    elif message.text == '👷‍♂Рефинансирование кредитов работающим клиентам':
        await bot.send_message(message.from_user.id,'👨Рефинансирование кредитов для РАБОТАЮЩИХ КЛИЕНТОВ\n\n 🎯 Цель - Рефинансирование кредитов\n\n 📍 Ставка от 7,77% до 17,25%\n\n 🕑 Срок от 6 до 60 месяцев\n\n❌ БЕЗ СТРАХОВОК И КОМИССИЙ!\n\n🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документ, подтверждающий доход (2-НДФЛ/СЗИ-ИЛС/Выписка по зарплатному счёту).\n ▫️ Справка об остатке долга по рефинансируемому кредиту\n\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys \n\n Доверяй своим!💙')
    elif message.text == '👨Рефинансирование кредитов пенсионерам':
        await bot.send_message(message.from_user.id,'👨Рефинансирование кредитов для ПЕНСИОНЕРОВ\n\n 🎯 Цель - Рефинансирование кредитов\n\n 📍 Ставка от 11,65% до 15,25%\n\n 🕑 Срок от 6 до 60 месяцев\n\n❌ БЕЗ СТРАХОВОК И КОМИССИЙ!\n\n🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документ, подтверждающий доход (Справка ПФР/СЗИ-ИЛС/Выписка по зарплатному счёту).\n ▫️ Справка об остатке долга по рефинансируемому кредиту\n\n📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys \n\n Доверяй своим!💙')

    #Ипотека

    elif message.text == '🏡Ипотека':
        await bot.send_message(message.from_user.id,'🔹ИПОТЕКА ОТ 8,8%\n➖➖➖➖➖\n🔵Выберите ипотечный продукт:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup=nav.OtherMenu_mort)
    elif message.text == 'Покупка квартиры':
        await bot.send_message(message.from_user.id,'🏙 Покупка квартиры \n\n 🎯 Цель - Покупка кватиры на первичном или вторичном рынке \n\n 📍 Ставка от 8,8% до 12,20% \n\n 🕑 Срок от 3 до 30 лет \n\n 🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документы, подтверждающие доход (2-НДФЛ/СЗИ-ИЛС/Выписка по зарплатному счёту);\n ▫️ иные документы при запросе менеджера.\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys')
    elif message.text == 'Рефинансирование ипотеки':
        await bot.send_message(message.from_user.id,'♻️ Рефинансирование ранее оформленной ипотеки \n\n 🎯 Цель - Рефинансирование ипотечного кредита \n\n 📍 Ставка от 8,8% до 12,95% \n\n 🕑 Срок от 3 до 30 лет \n\n 🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документы, подтверждающие доход (2-НДФЛ/СЗИ-ИЛС/Выписка по зарплатному счёту);\n ▫️ Документу о рефинансируемом кредите(справка об остатке ссудной задолженности, кредитный договор,график платежей);\n ▫️ иные документы при запросе менеджера.\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys')
    elif message.text == 'Покупка/строительство дома':
        await bot.send_message(message.from_user.id,'🏡 Кредит на покупку/строительства дома \n\n 🎯 Цель - Покупка/строительство дома\n\n 📍 Ставка от 9,8% до 12,95% \n\n 🕑 Срок от 3 до 30 лет \n\n 🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документы, подтверждающие доход (2-НДФЛ/СЗИ-ИЛС/Выписка по зарплатному счёту)\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys')
    elif message.text == 'Ипотека с гос.поддержкой':
        await bot.send_message(message.from_user.id,'🇷🇺 Ипотека с гос.поддержкой \n\n 🎯 Цель - Приоберитение у юридического лица/ИП квартиры/дома/ОНС\n\n 📍 Ставка от 6,95% до 7,20% \n\n 🕑 Срок от 3 до 20 лет \n\n 🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документы, подтверждающие доход (2-НДФЛ)\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys')
    elif message.text == 'Семейная ипотека':
        await bot.send_message(message.from_user.id,'👪 Семейная ипотека \n\n 🎯 Цель - Приобретение у юридического лица недвижимости или рефинансирование ипотечного кредита, ранее взятого на аналогичные цели\n\n 📍 Ставка 4,95% \n\n 🕑 Срок от 3 до 30 лет \n\n 🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документы, подтверждающие доход (2-НДФЛ)\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys')
    elif message.text == 'IT Ипотека':
        await bot.send_message(message.from_user.id,'💻 IT Ипотека\n\n 🎯 Цель - Приобретение у юридического лица недвижимости физическими лицами  основным местом работы которых является организация,которая осуществляет деятельность в области информационных технологий и имеет аккредитацию Минцифры России\n\n 📍 Ставка 4,95% \n\n 🕑 Срок от 3 до 30 лет \n\n 🔹 Документы для подачи заявки:\n\n ▫️ Паспорт;\n ▫️ СНИЛС;\n ▫️ Документы, подтверждающие доход\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys')

    #Кредит для самозанятых

    elif message.text == '👨‍💻Кредит самозанятым':
        await bot.send_message(message.from_user.id,'👨‍💻 Кредит "Старт" для самозанятых \n\n 🎯 Цель - на любые цели или рефинансирование, имеющихся кредитов\n\n📍 Ставка от 17,45% до 18,95%\n\n 🕑 Срок от6 до 60 месяцев\n 📲 ПОДАТЬ ЗАЯВКУ ОНЛАЙН НА САЙТЕ https://esia.gosuslugi.ru/aas/oauth2/ac?client_id=905301_3T&redirect_uri=https%3A%2F%2Fcp.modernsys')

    # Вклад

    elif message.text == '🛡Вклады':
        await bot.send_message(message.from_user.id, '✨Вклады с доходностью до 6,00%\n➖➖➖➖➖\n🔹Выберите интересующий вас сберегательный продукт:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup=nav.OtherMenu_deposit)
    elif message.text == '🤝Правильный выбор':
        await bot.send_message(message.from_user.id,'🔑Вклад "Правильный выбор"\n\n▫️Доходность до 5,5%\n\n▫️Срок вклада 837 дней\n\n▫️Пополняемый с 94 дня')
    elif message.text == '📲Правильный выбор онлайн':
        await bot.send_message(message.from_user.id,'🔑Вклад "Правильный выбор ОНЛАЙН"\n\n▫️Доходность до 6%\n\n️▫️️Срок вклада 837 дней\n\n️▫️️Сумма от 10 000 руб.\n\n▫️Пополняемый с 94 дня\n\n🔹ОТКРЫТЬ ВКЛАД МОЖНО В ПРИЛОЖЕНИИ БАНКА')
    elif message.text == '💺Комфортный':
        await bot.send_message(message.from_user.id,'🔑Вклад "Доходный"▫️Доходность до 5,10%\n\n️▫️️Срок вклада 1 080 дней\n\n️▫️️Сумма от 10 000 руб.\n\n▫️Пополняймый в течении 180 дней')
    elif message.text == '👨Пенсионный':
        await bot.send_message(message.from_user.id,'🔑Вклад "Пенсионный"▫️Доходность до 5,25%\n\n️▫️️Срок вклада 1 140 дней\n\n️▫️️Сумма от 5 000 руб.\n\n▫Пополняемый в течении 180 дней')
    elif message.text == '📲Онл@йн':
        await bot.send_message(message.from_user.id,'🔑Вклад "Онл@йн"▫️Доходность до 5,50%\n\n️▫️️Срок вклада 370 дней\n\n️▫️️Сумма от 5 000 руб.\n\n▫️Пополняемый в течении 180 дней\n\n🔹ОТКРЫТЬ ВКЛАД МОЖНО В ПРИЛОЖЕНИИ БАНКА')


# Банковские карты
    elif message.text == '💳Банковские карты':
        await bot.send_message(message.from_user.id, '💳Карты АО "БАНК ОРЕНБУРГ" позволяют комфортно и оперативно осущеставлять банковские операции\n➖➖➖➖➖\n🔹Выберите интересующий карточные продукты:\n➖➖➖➖➖\n🔻🔻🔻⤵️', reply_markup=nav.Other_Menu_card)
    elif message.text == '🏞Карты МИР':
        await bot.send_message(message.from_user.id, '🌍Платёжная система «Мир» создана при поддержке государства с учетом особенностей российского финансового рынка и нацелена на обеспечение финансовой безопасности страны.\n➖➖➖➖➖\n🔹Выберите карту ПС МИР️:\n➖➖➖➖➖\n🔻🔻🔻⤵️',reply_markup= nav.OtherMenu_cardmir)
    elif message.text == 'Классическая карта МИР':
        await bot.send_message(message.from_user.id, '🌷Классическая карта МИР\n▫️ Карта позволяет без ограничений получать наличные, рассчитываться за товары и услуги, а также оплачивать покупки в Интернете.\n▫️ Срок действия - 5 лет \n▫️ CASHBACK ДО 10% ')
    elif message.text == 'Премиальная карта МИР':
        await bot.send_message(message.from_user.id,'🔥Премиальная карта МИР\n▫️ Карта премиум-категории, подчёркивающая статус держателя, позволяет получать наличные, рассчитываться за товары и услуги, оплачивать покупки в Интернете, а также открывает доступ к ряду привилегий, предоставляя ещё большую финансовую свободу.\n▫️ Срок действия - 3 года \n▫️ CASHBACK ДО 10% ')
    elif message.text == 'Вернуться в меню 💳Банковские карты':
        await bot.send_message(message.from_user.id, 'Вы вернулись в меню "💳Банковские карты"', reply_markup = nav.Other_Menu_card)
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

    elif message.text == '☎️Консультация с специалистом':
        await bot.send_message(message.from_user.id,'📞Получить консультацию можно по телефону: 373-000\n\n 🖥Обратная связь через сайт:https://orbank.ru/')

    elif message.text == '🗃Вернуться в главное меню':
        await bot.send_message(message.from_user.id, '🔹Вы вернулись в главное меню↩️\n➖➖➖➖➖\n🌀Выберете интересующую услугу️⤵️', reply_markup = nav.mainMenu)
    else:
        await bot.send_message(message.from_user.id, 'Я только учусь👨‍🎓, поэтому буду рад Вам помочь с помощью разделов моего меню⌨️\n\n🔹Вы вернулись в главное меню↩️\n➖➖➖➖➖\n🌀Выберете интересующую услугу️⤵️', reply_markup = nav.mainMenu)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates = True)
