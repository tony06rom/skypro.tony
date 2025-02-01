import json
import logging
from typing import Any
import os
from src.external_api import convert_amount
from pathlib import Path


root_dir = os.path.dirname(os.path.abspath('__name__'))
logs_path = os.path.join(root_dir, "./logs/")
data_path = os.path.join(root_dir, "./data/")

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
LOGS_DIR = ROOT_DIR / "logs"

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{LOGS_DIR}\\utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(funcName)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(open_file: Any) -> Any:
    """Принимает на вход имя JSON-файла по пути ./data/ и
    возвращает список словарей с данными о финансовых транзакциях"""

    logger.info("Запуск программы")

    try:
        with open(f"{DATA_DIR}\\{open_file}.json", "r", encoding="utf-8") as jf:

            logger.info(f"Открыт файл {DATA_DIR}\\{open_file}.json на чтение")

            try:
                json_obj = json.load(jf)
                if json_obj:

                    logger.info("Конвертация JSON файла прошла успешно")

                    return json_obj
                else:

                    logger.warning(f"JSON в файле {open_file} имеет пустой список")

                    print("Файл содержит пустой список")
                    return []
            except json.JSONDecodeError:

                logger.error("Ошибка работы с файлов. Некорректный формат JSON")

                print("Объект не является JSON или JSON имеет неверный формат")
                return []
    except FileNotFoundError:

        logger.error(f"JSON с именем {open_file} не найден в директории ../data/")

        print("Файл не найден")
        return []


def summ_transact_rub(finance_transacts: list[Any]) -> int:
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    logger.info("Запуск программы")

    amount_all_transacts = 0
    amount_usd_transacts = 0
    amount_eur_transacts = 0
    for transaction in finance_transacts:

        logger.info("Запуск цикла перебора имеющихся транзакций")

        if "operationAmount" in transaction:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                amount_all_transacts += transaction["operationAmount"]["amount"]
            elif transaction["operationAmount"]["currency"]["code"] == "USD":
                amount_usd_transacts += transaction["operationAmount"]["amount"]
            elif transaction["operationAmount"]["currency"]["code"] == "EUR":
                amount_eur_transacts += transaction["operationAmount"]["amount"]
        else:

            logger.warning(f'Пропуск. Ключ "operationAmount" отсутствует в транзакции: {transaction}')

            continue
    convert_usd = convert_amount(str(amount_usd_transacts), "USD", "RUB")
    convert_eur = convert_amount(str(amount_eur_transacts), "EUR", "RUB")
    final = round((amount_all_transacts + int(convert_usd) + int(convert_eur)), 2)

    logger.info("Конвертация различных валют в RUB прошла успешно")

    return final
