from src.masks import get_mask_account, get_mask_card_number

""" --- 9.1 Poetry. Оформление кода --- """

# Тест функции get_mask_card_number
input_user = input("Введите номер карты:\n")
print(get_mask_card_number(input_user))

print("===========================")
# Тест функции get_mask_account
answer_user = str(input("Хотите продолжить? [да(yes)/нет(no)]\n"))
list_answers_yes = ["да", "y", "yes"]
list_answers_no = ["нет", "n", "no"]
if answer_user.lower() in list_answers_yes:
    print("===========================")
    input_user_2 = input("Введите номер счета:\n")
    print(get_mask_account(input_user_2))
else:
    print("До свидания!")
