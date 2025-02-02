from src.processing import filter_by_state, sort_by_date
from src.re_collections import filter_by_description
import os
from pathlib import Path

root_dir = os.path.dirname(os.path.abspath('__name__'))
data_path = os.path.join(root_dir, "./data")

ROOT_DIR = Path(__file__).resolve().parents[0]
DATA_DIR = ROOT_DIR / "data"

def welcome():
    """ Приветствует пользователя и дает выбор работы с транзакциями """
    def choose_mode(users_mode):
        """ Выбирает режим работы """
        mode = {'1': 'JSON-файла', '2': 'CSV-файла', '3': 'XLSX-файла'}
        if users_mode in mode.keys():
            for key, value in mode.items():
                if users_mode == key:
                    print(f'# Был выбран режим получения данных из {value}\n')
                    return users_mode
        elif users_mode == 'quit':
            print('# До свидания!')
            exit()
        else:
            return choose_mode(input('# Пожалуйста, введи цифру от 1 до 3 для продолжения операции.\n'
                              '# Или введи "quit" для выхода из программы\n===> '))

    input_user = input("# Добро пожаловать в программу работы с банковскими транзакциями!\n"
                        "# Выбери необходимый пункт меню [1-3]:\n"
                        "1. Получить информацию о транзакциях из JSON-файла\n"
                        "2. Получить информацию о транзакциях из CSV-файла\n"
                        "3. Получить информацию о транзакциях из XLSX-файла\n"
                        "===> ")
    first_exec = choose_mode(input_user)
    return first_exec


def list_files_in_data(path_of_data, type_files):
    """ Вычитывает файлы определенного расширения в директории и выводит пользователю """
    print('# ../data:')
    count = 0
    if type_files == 'csv':
        type_files = ".csv"
    elif type_files == 'json':
        type_files = ".json"
    elif type_files == 'xlsx':
        type_files = ".xlsx"
    for file_name in os.listdir(path_of_data):
        if file_name.endswith(type_files):
            count += 1
            print(f"-> {file_name[:-len(type_files)]}")
    print(f"!!! Inform !!! ---> Доступно '{type_files}' файлов в директории /data: {count}")


def uniq_data(start_data):
    """ Вычитывает доступные статусы транзакций и выводит пользователю """
    uniq_final_data = []
    for data in start_data:
            for k, v in data.items():
                if k == "state":
                    if v not in uniq_final_data:
                        uniq_final_data.append(v)
    return "\n".join(uniq_final_data)


# Фильтрует прочитанный файл по транзакции
def filter_transact_by_state(input_user):
    """ Фильтрует по выбранному статусу транзакции """
    if input_user in uniq_state:
        filter_data = filter_by_state(object_transactions, input_user)
        print(f"# Операции отфильтрованы по статусу '{choose_filter_state}'")
        return filter_data
    elif input_user == 'quit':
        print('# До свидания!')
        exit()
    else:
        filter_transact_by_state(input('# Пожалуйста, введи один статус из списка ниже:\n'
                                       f'{uniq_state}\n# Или введи "quit" для выхода из программы\n===> '))


def choose_reverse(reverse_mode):
    """ Считает тип сортировки списка по дате """
    if reverse_mode == str("по возрастанию"):
        return {"reverse_mode_bool": True, "reverse_mode_string": "убыванию"}
    elif reverse_mode == str("по убыванию"):
        return {"reverse_mode_bool": False, "reverse_mode_string": "возрастанию"}
    else:
        return {"reverse_mode_bool": True, "reverse_mode_string": "умолчанию (по убыванию)"}


def sort_transact_by_date(input_user, filtered_state_to_data):
    """ Сортирует по дате """
    list_answers_yes = ["да", "д", "y", "yes", "+"]
    list_answers_no = ["нет", "н", "n", "no", "-"]
    if input_user.lower() in list_answers_yes:
        need_sort = input('# Отсортировать [1] по возрастанию или [2] по убыванию? Введите цифру\n===> ')
        if need_sort == '1':
            need_sort = 'по возрастанию'
        elif need_sort == '2':
            need_sort = 'по убыванию'
        reverse_equals = choose_reverse(need_sort)
        filtered_data = sort_by_date(filtered_state_to_data, reverse_equals["reverse_mode_bool"])
        print(f"# Операции отсортированы {need_sort}")
        return filtered_data
    elif input_user.lower() in list_answers_no:
        print("# Фильтрация по дате не применена")
        return filtered_state_to_data
    else:
        print("# Фильтрация по дате не применена, так как не было дано допустимого ответа")
        return filtered_state_to_data


def uniq_currency(start_data):
    """ Считывает и выводит на экран доступные валюты """
    uniq_final_currency = []
    for data in start_data:
        if "operationAmount" in data:
            if data["operationAmount"]["currency"]["code"] not in uniq_final_currency:
                uniq_final_currency.append(data["operationAmount"]["currency"]["code"])
        else:
            for k, v in data.items():
                if k == "currency_code":
                    if v not in uniq_final_currency:
                        uniq_final_currency.append(v)
    return "\n".join(uniq_final_currency)


def filter_by_currency(input_user, sorted_data_to_currency):
    """ Фильтрует по валюте """
    list_answers_yes = ["да", "д", "y", "yes", "+"]
    list_answers_no = ["нет", "н", "n", "no", "-"]
    if input_user.lower() in list_answers_yes:
        filter_data_state = []
        for data in sorted_data_to_currency:
            if "operationAmount" in data:
                if data["operationAmount"]["currency"]["code"] == 'RUB':
                    filter_data_state.append(data)
            else:
                filtered_data = filter_by_state(sorted_data_to_currency, 'RUB')
                return filtered_data
        print(f"# Операции отсортированы по '{input_user}'")
        return filter_data_state
    elif input_user.lower() in list_answers_no:
        print("# Фильтрация по валютам не применена")
        return sorted_data_to_currency
    else:
        print("# Фильтрация по валютам не применена, так как не было дано допустимого ответа")
        return sorted_data_to_currency


def filter_transact_by_description(filter_data_to_description, input_user):
    """ Фильтрует по описанию """
    list_answers_yes = ["да", "д", "y", "yes", "+"]
    list_answers_no = ["нет", "н", "n", "no", "-"]
    if input_user.lower() in list_answers_yes:
        find = input("# Введите строку поиска для фильтрации по описанию\n===> ")
        filtered_data = filter_by_description(filter_data_to_description, find)
        return filtered_data
    elif input_user.lower() in list_answers_no:
        return filter_data_to_description
    else:
        print("# Фильтрация по описанию не применена, так как не было найдено совпадений")
        return filter_data_to_description