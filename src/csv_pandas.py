import csv
import pandas as pd
import logging


logger = logging.getLogger("csv_pandas")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/csv_pandas.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(funcName)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

csv_transact = "../data/transactions.csv"
excel_transact = "../data/transactions_excel.xlsx"

def csv_worker(include_file: str=csv_transact) -> list[dict[str, int | float | str]] | Exception | str:
    """ Считывает финансовые операции из CSV """

    logger.info(f"Старт программы 'csv_worker'")

    try:
        with open(include_file, mode='r', encoding="utf-8") as file:

            logger.info(f"File '{include_file}' was opened")

            csv_data = csv.DictReader(file, delimiter=';')

            transact_list = [row for row in csv_data]

            logger.info(f"File '{include_file}' was success transform to dict")

            return transact_list

    except FileNotFoundError as exc_info:

        logger.error(f"File '{include_file}' not found")

        return f"Error: {type(exc_info).__name__}, Incorrect path to file or file name"


def excel_worker(include_file: str=excel_transact) -> list[dict[str, int | float | str]] | Exception | str:
    """ Считывает финансовые операции из Excel """

    logger.info(f"Старт программы 'excel_worker'")

    try:
        excel_data = pd.read_excel(include_file, sheet_name='Лист 1')

        logger.info(f"File '{include_file}' was opened")

        transact_list = excel_data.to_dict(orient='records')

        logger.info(f"File '{include_file}' was success transform to dict")

        return transact_list
    except FileNotFoundError as exc_info:

        logger.error(f"File '{include_file}' not found")

        return f"Error: {type(exc_info).__name__}, Incorrect path to file or file name"
