from typing import Any

from src.decorators import decor_log as decor
from src.masks import get_mask_account, get_mask_card_number


@decor(filename="log_widget.txt")
def mask_account_card(user_number: str) -> Any:
    """Обрабатывает информацию как о картах, так и о счетах"""
    format_user_number = user_number.split(" ")
    number_of_card_or_score = "".join(format_user_number[-1:])
    card_name_or_score = " ".join(format_user_number[:-1])
    variable_score_name = ["счёт", "счет", "номер счёта", "номер счета", "личный счет", "личный счёт", "л/с"]
    if len(number_of_card_or_score) == 16 and card_name_or_score.replace(" ", "").isalpha():
        mask_number = get_mask_card_number(number_of_card_or_score)
        return f"{card_name_or_score} {mask_number}"
    elif len(number_of_card_or_score) == 20 and card_name_or_score.lower() in variable_score_name:
        mask_score = get_mask_account(number_of_card_or_score)
        return f"{card_name_or_score.title()} {mask_score}"
    elif user_number.lower() == "quit":
        return "До свидания!"
    else:
        return mask_account_card(
            input("Введены некорректные данные. Повторите ввод или напишите 'quit' для выхода\n")
        )


@decor(filename="log_widget.txt")
def get_date(date_unformat: str) -> Any:
    """Принимает на вход дату формата '2024-03-11T02:26:18.671407' и
    отдает корректный результат в формате '11.07.2018'"""
    #    marks = ['.', '-', '\\', '/', ':', ',', '_', '*', '^', '`'] # доработать на разделители
    if "T" in date_unformat:
        raw_date = "-".join((date_unformat.split("T"))[:1])
        if "-" in raw_date:
            raw_date_2 = raw_date.split("-")
            date_format = ".".join(reversed(raw_date_2))
            return str(date_format)
    else:
        return "Неизвестный формат даты и времени"
