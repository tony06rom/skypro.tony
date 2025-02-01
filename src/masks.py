import logging
from typing import Any
import os
from src.decorators import decor_log as decor


root_dir = os.path.dirname(os.path.abspath('__name__'))
logs_path = os.path.join(root_dir, "../logs/")
wraps_log = os.path.join(root_dir, "../wraps/log_masks.txt")


logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{logs_path}masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(funcName)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


@decor(filename=wraps_log)
def get_mask_card_number(card_number: str) -> Any:
    """Функция маскировки номера банковской карты"""

    logger.info("Запуск программы")

    format_card_number = card_number.replace(" ", "")

    logger.info(f"Введены данные: {format_card_number}")

    if format_card_number.isdigit() is True and len(format_card_number) == 16:

        logger.info("Маскирование завершено успешно")

        return f"{format_card_number[0:4]} {format_card_number[4:6]}** **** {format_card_number[-4:]}"
    elif format_card_number.lower() == "quit":

        logger.info("Пользователь вышел из программы")

        return "До свидания!"
    else:

        logger.error("Введены некорректные данные")

        return get_mask_card_number(
            input("Номер карты введён неверно. " "Повторите ввод или напишите 'quit' для выхода\n")
        )


@decor(filename=wraps_log)
def get_mask_account(score_card: str) -> Any:
    """Функция маскировки номера банковского счета"""

    logger.info("Запуск программы")

    format_score_card = score_card.replace(" ", "")

    logger.info(f"Введены данные: {format_score_card}")

    if format_score_card.isdigit() is True and len(format_score_card) == 20:

        logger.info("Маскирование завершено успешно")

        return f"**{format_score_card[-4:]}"
    elif format_score_card.lower() == "quit":

        logger.info("Пользователь вышел из программы")

        return "До свидания!"
    else:

        logger.error("Введены некорректные данные")

        return get_mask_card_number(
            input("Номер счёта введён неверно. " "Повторите ввод или напишите 'quit' для выхода\n")
        )
