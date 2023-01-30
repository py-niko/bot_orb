from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('🗃Вернуться в главное меню')
# main menu

btnkredit = KeyboardButton('🚩Кредиты')
btndeposit = KeyboardButton('🛡Вклады')
bank_card = KeyboardButton('💳Карты')
school_mark = KeyboardButton('🥣Школьное питание')
#curs_v = KeyboardButton('💸Курсы валют в офисах г.Оренбург')
consultation_mark = KeyboardButton('☎️Офисы и контакты')
news_mark = KeyboardButton('🗞Новости')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnkredit, btndeposit, bank_card, school_mark, news_mark, consultation_mark)

#other menu

loanMenu = KeyboardButton('Вернуться в меню "🚩Кредиты"')

btnconsumercredit = KeyboardButton('💎Потребительские кредиты')
emty_1 = KeyboardButton('')
refinancingcredit = KeyboardButton('🔄Рефинансирование кредитов')
mortgage = KeyboardButton('🏡Ипотека')
stocking = KeyboardButton('🔖Акция! Честный процент')
credit_self = KeyboardButton('👨‍💻Кредит самозанятым')
OtherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnconsumercredit, emty_1, refinancingcredit, mortgage, stocking, credit_self, btnMain)

#other_costumer_credit

word_loan = KeyboardButton('👷‍♂️Кредит для работающих')
emty_1 = KeyboardButton('')
grand_loan = KeyboardButton('👨Кредит для пенсионеров')
credit_card = KeyboardButton('💳Кредитная карта')
emty_1 = KeyboardButton('')
OtherMenu_1 = ReplyKeyboardMarkup(resize_keyboard = True).add(word_loan, emty_1, grand_loan, credit_card, emty_1, loanMenu, btnMain)

#other_costumer_refinancing

word_ref = KeyboardButton('👷‍♂Рефинансирование кредитов работающим клиентам')
emty_1 = KeyboardButton('')
grand_ref = KeyboardButton('👨Рефинансирование кредитов пенсионерам')
OtherMenu_ref = ReplyKeyboardMarkup(resize_keyboard = True).add(word_ref, emty_1, grand_ref,loanMenu, btnMain)

#other_costumer_mortgage
buy_app = KeyboardButton('Покупка квартиры')
buy_ref = KeyboardButton('Рефинансирование ипотеки')
buy_house = KeyboardButton('Покупка/строительство дома')
buy_gover = KeyboardButton('Ипотека с господдержкой')
buy_family = KeyboardButton('Семейная ипотека')
buy_it = KeyboardButton('IT Ипотека')
OtherMenu_mort = ReplyKeyboardMarkup(resize_keyboard = True).add(buy_app, buy_ref, buy_house, buy_gover, buy_family, buy_it, loanMenu, btnMain)

#other_deposit

depositMenu = KeyboardButton('Вернуться в меню "🛡Вклады"' )
# меню вклада
depositOn = KeyboardButton('☕️Вклады в офисах Банка')
depositOff = KeyboardButton('📲Вклады онлайн')
moneybox = KeyboardButton('🗄 Счета')
OffOnMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(depositOn, depositOff, moneybox, btnMain)

# оффлайн вклады
right_choice = KeyboardButton('🤝Правильный выбор')
newhoriz_deposit = KeyboardButton('🌄Новый горизонт')
pension_deposit = KeyboardButton('👨Пенсионный')
olimp = KeyboardButton('⛰Олимп')
Offline_deposit = ReplyKeyboardMarkup(resize_keyboard = True).add(right_choice, newhoriz_deposit, pension_deposit, olimp, depositMenu, emty_1,  consultation_mark, btnMain)

# онлайн вклады
right_choice_online = KeyboardButton('📲Правильный выбор онлайн')
online_deposit = KeyboardButton('🚀Онл@йн')
Online_deposit = ReplyKeyboardMarkup(resize_keyboard = True).add(right_choice_online, online_deposit, depositMenu, btnMain)

# счета накопительные

money_one = KeyboardButton('🗄 Накопительный счёт')
money_box_menu = ReplyKeyboardMarkup(resize_keyboard = True).add(money_one, emty_1, depositMenu, btnMain)
money_two = KeyboardButton('')

#other_deposit_card
cardMenu_back = KeyboardButton('Вернуться в меню 💳Карты')

deposit_card = KeyboardButton('🏞Карты МИР')
oren_card = KeyboardButton('🌇Карта Оренбуржца')
Other_Menu_card = ReplyKeyboardMarkup(resize_keyboard = True).add(deposit_card, oren_card, btnMain)

#other_deposit_card_1   

classic_deposit = KeyboardButton('Классическая карта МИР')
emty_1 = KeyboardButton('')
OtherMenu_cardmir = ReplyKeyboardMarkup(resize_keyboard = True).add(classic_deposit, emty_1, cardMenu_back, btnMain)

# Офисы
contact = KeyboardButton('☎️Вернуться в меню "Офисы и контакты"')
orenoffice_time = KeyboardButton('🌇Офисы в г.Оренбурге')
regionoffice_time = KeyboardButton('🌄Офисы в Оренбургской области')

contact_menu = ReplyKeyboardMarkup(resize_keyboard = True).add(orenoffice_time, emty_1, regionoffice_time, btnMain)


#other_kurs

# curs_dollar = KeyboardButton('$ Покупка/Продажка')
# curs_euro = KeyboardButton('€ Покупка/Продажа')
# curs_tenge = KeyboardButton('Тенге Покупка/Продажа')

# OtherMenu_curs = ReplyKeyboardMarkup(resize_keyboard = True).add(curs_dollar, curs_euro, curs_tenge, btnMain)