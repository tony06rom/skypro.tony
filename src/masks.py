import logging
from typing import Any

from src.decorators import decor_log as decor

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('"../logs/masks.log/"', "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(funcName)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


@decor(filename="../wraps/log_masks.txt")
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


@decor(filename="../wraps/log_masks.txt")
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


get_mask_card_number("1234567890123456")
