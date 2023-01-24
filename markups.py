from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('🗃Вернуться в главное меню')
# main menu

btnkredit = KeyboardButton('🚩Кредиты')
btndeposit = KeyboardButton('🛡Вклады')
bank_card = KeyboardButton('💳Банковские карты')
#curs_v = KeyboardButton('💸Курсы валют в офисах г.Оренбург')
consultation_mark = KeyboardButton('☎️Консультация с специалистом')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnkredit, btndeposit, bank_card, consultation_mark)

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
buy_gover = KeyboardButton('Ипотека с гос.поддержкой')
buy_family = KeyboardButton('Семейная ипотека')
buy_it = KeyboardButton('IT Ипотека')
OtherMenu_mort = ReplyKeyboardMarkup(resize_keyboard = True).add(buy_app, buy_ref, buy_house, buy_gover, buy_family, buy_it, loanMenu, btnMain)

#other_deposit

depositMenu = KeyboardButton('Вернуться в меню "🛡Вклады"' )

right_choice = KeyboardButton('🤝Правильный выбор')
emty_1 = KeyboardButton('')
right_choice_online = KeyboardButton('📲Правильный выбор онлайн')
comfort_deposit = KeyboardButton('💺Комфортный')
pension_deposit = KeyboardButton('👨Пенсионный')
online_deposit = KeyboardButton('📲Онл@йн')
OtherMenu_deposit = ReplyKeyboardMarkup(resize_keyboard = True).add(right_choice, emty_1, right_choice_online, comfort_deposit, pension_deposit, online_deposit, btnMain)

#other_deposit_card

cardMenu_back = KeyboardButton('Вернуться в меню 💳Банковские карты')

deposit_card = KeyboardButton('🏞Карты МИР')
oren_card = KeyboardButton('🌇Карта Оренбуржца')
Other_Menu_card = ReplyKeyboardMarkup(resize_keyboard = True).add(deposit_card, oren_card, btnMain)

#other_deposit_card_1   

classic_deposit = KeyboardButton('Классическая карта МИР')
emty_1 = KeyboardButton('')
premium_deposit = KeyboardButton('Премиальная карта МИР')
OtherMenu_cardmir = ReplyKeyboardMarkup(resize_keyboard = True).add(classic_deposit,emty_1, premium_deposit, cardMenu_back, btnMain)

#other_kurs

curs_dollar = KeyboardButton('$ Покупка/Продажка')
curs_euro = KeyboardButton('€ Покупка/Продажа')
curs_tenge = KeyboardButton('Тенге Покупка/Продажа')

OtherMenu_curs = ReplyKeyboardMarkup(resize_keyboard = True).add(curs_dollar, curs_euro, curs_tenge, btnMain)