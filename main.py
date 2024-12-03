from os import access

from src.masks import get_mask_account, get_mask_card_number

input_user = input("Введите номер карты:\n")
print(get_mask_card_number(input_user))

print("===========================")
answer_user = str(input("Хотите продолжить? [да(yes)/нет(no)]\n"))
list_answers = ["да", "нет", "y", "n", "yes", "no",]
if answer_user.lower() in list_answers:
    print("===========================")
    input_user_2 = input("Введите номер счета:\n")
    print(get_mask_account(input_user_2))

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
