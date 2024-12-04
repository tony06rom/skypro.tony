from os import access

from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date

# ==============================================================================================================
""" --- 9.1 Poetry. Оформление кода --- """

# input_user = input("Введите номер карты:\n")
# print(get_mask_card_number(input_user))
#
# print("===========================")
# answer_user = str(input("Хотите продолжить? [да(yes)/нет(no)]\n"))
# list_answers = ["да", "нет", "y", "n", "yes", "no",]
# if answer_user.lower() in list_answers:
#     print("===========================")
#     input_user_2 = input("Введите номер счета:\n")
#     print(get_mask_account(input_user_2))

# ==============================================================================================================
""" --- 9.2 Основы Git --- """

user_input_number = str(input("Введите номер карты или счета в формате:\n'Тип карты / Счет + номер карты/счета'\n"))
print(mask_account_card(user_input_number))
# mask_account_card("Visa Platinum 7000792289606361")
print("===========================")
raw_date = "2024-03-11T02:26:18.671407"
print(get_date(raw_date))

# ==============================================================================================================

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
