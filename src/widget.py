import logging
from pathlib import Path
from typing import Any

from src.decorators import decor_log as decor
from src.masks import get_mask_account, get_mask_card_number

ROOT_DIR = Path(__file__).resolve().parents[1]
LOGS_DIR = ROOT_DIR / "logs"

logger = logging.getLogger("widget")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{LOGS_DIR}\\widget.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(funcName)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


@decor(filename="log_widget.txt")
def mask_account_card(user_number: str) -> Any:
    """Обрабатывает информацию как о картах, так и о счетах"""

    logger.info("Запуск программы")

    format_user_number = user_number.split(" ")

    logger.info(f"Введены данные: {format_user_number}")

    number_of_card_or_score = "".join(format_user_number[-1:])
    card_name_or_score = " ".join(format_user_number[:-1])

    logger.info("Обработка данных ...")

    variable_score_name = ["счёт", "счет", "номер счёта", "номер счета", "личный счет", "личный счёт", "л/с"]
    if len(number_of_card_or_score) == 16 and card_name_or_score.replace(" ", "").isalpha():

        logger.info("Запуск функции 'get_mask_card_number' из модуля 'masks' для маскирования __номера карты__")

        mask_number = get_mask_card_number(number_of_card_or_score)
        return f"{card_name_or_score} {mask_number}"
    elif len(number_of_card_or_score) == 20 and card_name_or_score.lower() in variable_score_name:

        logger.info("Запуск функции 'get_mask_account' из модуля 'masks' для маскирования __номера счёта__")

        mask_score = get_mask_account(number_of_card_or_score)
        return f"{card_name_or_score.title()} {mask_score}"
    elif user_number.lower() == "quit":

        logger.info("Пользователь вышел из программы")

        return "До свидания!"
    else:

        logger.error("Введены некорректные данные")

        return mask_account_card(input("Введены некорректные данные. Повторите ввод или напишите 'quit' для выхода\n"))


@decor(filename="log_widget.txt")
def get_date(date_unformat: str) -> Any:
    """Принимает на вход дату формата '2024-03-11T02:26:18.671407' и
    отдает корректный результат в формате '11.07.2018'"""

    logger.info("Запуск программы")

    #    marks = ['.', '-', '\\', '/', ':', ',', '_', '*', '^', '`'] # доработать на разделители
    if "T" in date_unformat:
        raw_date = "-".join((date_unformat.split("T"))[:1])

        logger.info("Первичная обработка даты")

        if "-" in raw_date:
            raw_date_2 = raw_date.split("-")

            logger.info("Финальная обработка даты")

            date_format = ".".join(reversed(raw_date_2))

            logger.info("Работа программы завершена")

            return str(date_format)
    else:

        logger.error("Дата имеет недопустимый формат")

        return "Неизвестный формат даты и времени"
