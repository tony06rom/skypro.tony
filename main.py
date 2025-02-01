from src.processing import filter_by_state, sort_by_date
from src.re_collections import filter_by_description
from src.utils import read_json_file
from src.csv_pandas import csv_worker, excel_worker
import os
from pathlib import Path

root_dir = os.path.dirname(os.path.abspath('__name__'))
data_path = os.path.join(root_dir, "./data")

ROOT_DIR = Path(__file__).resolve().parents[0]
DATA_DIR = ROOT_DIR / "data"


# Приветствие пользователя и выбор файла
def welcome():
    def choose_mode(users_mode):
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


# Фильтруем прочитанный файл по транзакции
def filter_transact_by_state(input_user):
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


# Выборка доступных статусов
def uniq_data(start_data):
    uniq_final_data = []
    for data in start_data:
            for k, v in data.items():
                if k == "state":
                    if v not in uniq_final_data:
                        uniq_final_data.append(v)
    return "\n".join(uniq_final_data)


def uniq_currency(start_data):
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


def choose_reverse(reverse_mode):
    if reverse_mode == str("по возрастанию"):
        return {"reverse_mode_bool": True, "reverse_mode_string": "убыванию"}
    elif reverse_mode == str("по убыванию"):
        return {"reverse_mode_bool": False, "reverse_mode_string": "возрастанию"}
    else:
        return {"reverse_mode_bool": True, "reverse_mode_string": "умолчанию (по убыванию)"}


def sort_transact_by_date(input_user, filtered_state_to_data):
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


def filter_by_currency(input_user, sorted_data_to_currency):
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


# ==========================================

# Основная функция для связки всех функций
if __name__ == "__main__":
    stock_transactions = welcome()
    object_transactions = []

    # Соотносим цифры с файлами
    if stock_transactions == '1':
        stock_transactions = input(
            f'# Введите имя JSON-файла. Доступные файлы:{list_files_in_data(DATA_DIR, 'json')}\n===> ')
        object_transactions = read_json_file(stock_transactions)

    elif stock_transactions == '2':
        stock_transactions = input(
            f'# Введите имя CSV-файла. Доступные файлы:{list_files_in_data(DATA_DIR, 'csv')}\n===> ')
        object_transactions = csv_worker(f"{DATA_DIR}\\{stock_transactions}.csv")

    elif stock_transactions == '3':
        stock_transactions = input(
            f'# Введите имя Excel-файла. Доступные файлы:{list_files_in_data(DATA_DIR, 'xlsx')}\n===> ')
        object_transactions = excel_worker(f"{DATA_DIR}\\{stock_transactions}.xlsx")

    # Применяем функцию чтения из файла
    print(object_transactions)

    # Чтение уникальных статусов из файла
    uniq_state = uniq_data(object_transactions)

    # Выбор пользователем фильтрации по статусу транзакции
    choose_filter_state = input("# Введите статус, по которому необходимо выполнить фильтрацию.\n"
                                f"# Доступные статусы для фильтрации :\n{uniq_state}\n===> ")

    # Фильтруем файл
    filtered_by_state = filter_transact_by_state(choose_filter_state)

    print(filtered_by_state[0], filtered_by_state[-1])

    # Запрос сортировки по дате
    users_sort_by_data = input("# Отсортировать операции по дате? [да(yes)/нет(no)]\n===> ")

    # Сортировка транзакций по дате
    sorted_by_data = sort_transact_by_date(users_sort_by_data, filtered_by_state)

    print(sorted_by_data[0], sorted_by_data[-1])

    # Запрос фильтрации по валюте
    choose_filter_currency = input("# Выводить только рублевые транзакции? [да(yes)/нет(no)]\n===> ")

    # Фильтрация транзакций по валюте
    filtered_by_currency = filter_by_currency(choose_filter_currency, sorted_by_data)

    print(filtered_by_currency[0], filtered_by_currency[-1])

    # Запрос фильтрации по описанию
    choose_filter_description = input(
        "# Отфильтровать список транзакций по определенному слову? [да(yes)/нет(no)]\n===> ")

    # Фильтрация транзакций по описанию
    filtered_by_description = filter_transact_by_description(filtered_by_currency, choose_filter_description)

    print(filtered_by_description)
