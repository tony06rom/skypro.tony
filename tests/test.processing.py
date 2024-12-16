from src.processing import filter_by_state, sort_by_date

# Входные данные для проверки
origin_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


# Тест функции filter_by_state
def uniq_data(start_data):
    uniq_state = []
    for data in start_data:
        for k, v in data.items():
            if k == 'state':
                if v not in uniq_state:
                    uniq_state.append(v)
    return '\n'.join(uniq_state)


input_user = str(input(f"Введите одно из допустимых значений state:\n{uniq_data(origin_data)}\n"))
final = filter_by_state(origin_data, input_user)
print(f"Словарь с фильтром state = {input_user}\n\n{final}:")

print("===========================")


# Тест функции sort_by_date
def choose_reverse(reverse_mode):
    if reverse_mode == str("True"):
        return {"reverse_mode_bool": True, "reverse_mode_string": "убыванию"}
    elif reverse_mode == str("False"):
        return {"reverse_mode_bool": False, "reverse_mode_string": "возрастанию"}
    else:
        return {"reverse_mode_bool": True, "reverse_mode_string": "умолчанию (по убыванию)"}


input_user_2 = str(input(f"Введите одно из допустимых значений сортировки:\nTrue\nFalse\n"))
reverse_equals = choose_reverse(input_user_2)
final_2 = sort_by_date(origin_data, reverse_equals["reverse_mode_bool"])
print(f"Сортировка словарей в списке по {str(reverse_equals["reverse_mode_string"])} по ключу data\n\n{final_2}")
