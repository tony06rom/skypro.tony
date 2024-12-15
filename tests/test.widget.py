from src.widget import mask_account_card, get_date

""" --- 9.2 Основы Git --- """

# Тест функции mask_account_card
user_input_number = str(input("Введите номер карты или счета в формате:\n'Тип карты / Счет + номер карты/счета'\n"))
print(mask_account_card(user_input_number))
# mask_account_card("Visa Platinum 7000792289606361")
print("===========================")
# Тест функции get_date
raw_date = "2024-03-11T02:26:18.671407"
print(get_date(raw_date))
