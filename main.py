from pathlib import Path

from src.csv_pandas import csv_worker, excel_worker
from src.linking_functions_main import (filter_by_currency, filter_transact_by_description, filter_transact_by_state,
                                        list_files_in_data, sort_transact_by_date, true_output, uniq_data, welcome)
from src.utils import read_json_file

ROOT_DIR = Path(__file__).resolve().parents[0]
DATA_DIR = ROOT_DIR / "data"

if __name__ == "__main__":
    """Начало основной логики программы"""
    stock_transactions = welcome()
    object_transactions = []

    if stock_transactions == "1":  # Соотносим цифры с файлами
        print("# Доступные файлы:")
        list_of_dir = list_files_in_data(DATA_DIR, "json")
        print(list_of_dir)
        stock_transactions = input("# Введите имя JSON-файла\n===> ")
        object_transactions = read_json_file(stock_transactions)
    elif stock_transactions == "2":
        print("# Доступные файлы:")
        list_of_dir = list_files_in_data(DATA_DIR, "csv")
        print(list_of_dir)
        stock_transactions = input("# Введите имя CSV-файла\n===> ")
        object_transactions = csv_worker(f"{DATA_DIR}\\{stock_transactions}.csv")
    elif stock_transactions == "3":
        print("# Доступные файлы:")
        list_of_dir = list_files_in_data(DATA_DIR, "xlsx")
        print(list_of_dir)
        stock_transactions = input("# Введите имя Excel-файла\n===> ")
        object_transactions = excel_worker(f"{DATA_DIR}\\{stock_transactions}.xlsx")

    # Чтение уникальных статусов из файла
    uniq_state = uniq_data(object_transactions)

    # Выбор пользователем
    choose_filter_state = input("# Введите статус, по которому необходимо выполнить фильтрацию.\n"
        f"# Доступные статусы для фильтрации :\n{uniq_state}\n===> ")

    # Фильтруем файл
    filtered_by_state = filter_transact_by_state(choose_filter_state, uniq_state, object_transactions)

    # Запрос сортировки по дате
    users_sort_by_data = input("# Отсортировать операции по дате? [да(yes)/нет(no)]\n===> ")

    # Сортировка транзакций по дате
    sorted_by_data = sort_transact_by_date(users_sort_by_data, filtered_by_state)

    # Запрос фильтрации по валюте
    choose_filter_currency = input("# Выводить только рублевые транзакции? [да(yes)/нет(no)]\n===> ")

    # Фильтрация транзакций по валюте
    filtered_by_currency = filter_by_currency(choose_filter_currency, sorted_by_data)

    # Запрос фильтрации по описанию
    choose_filter_description = input("# Отфильтровать список транзакций по определенному слову? [да(yes)/нет(no)]\n===> ")

    # Фильтрация транзакций по описанию
    filtered_by_description = filter_transact_by_description(filtered_by_currency, choose_filter_description)

    # Форматирование для конечного вывода
    final_result = true_output(filtered_by_description)

    print(final_result)
