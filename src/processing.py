def filter_by_state(filter_data: str, state: str = 'EXECUTED') -> list[dict[int, str,]]:
    """ Словарь с фильтром state.
    Принимает на вход список словарей, делает выборку по совпадению значения ключа state.
    Далее выводит список словарей с совпадающим state """
    filter_data_state = []
    for data in filter_data:
        for state_of_data in data.values():
            if state_of_data == state:
                filter_data_state.append(data)
    return filter_data_state


def sort_by_date(sort_data: str, reverse: bool = True) -> list[dict[int, str,]]:
    """ Словарь отсортированный по дате.
    Принимает на вход список словарей, имеет стандартную сортировку в обратном порядке по data.
    Далее выводит список словарей в обратном порядке, если не было задано другой сортировки """
    sorted_data = sorted(sort_data, key=lambda x: x['date'], reverse=reverse)
    return sorted_data


# Входные данные
lost_input = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
              {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
              {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
              {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

# Тесты
# final = filter_by_state(lost_input, 'CANCELED')
# print(final)

final_2 = sort_by_date(lost_input,False)
print(final_2)
