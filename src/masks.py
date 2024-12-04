def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    format_card_number = card_number.replace(" ", "")
    if format_card_number.isdigit() is True and len(format_card_number) == 16:
        return f"{format_card_number[0:4]} {format_card_number[4:6]}** **** {format_card_number[-4:]}"
    elif format_card_number.lower() == "quit":
        return "До свидания!"
    else:
        return get_mask_card_number(input("Номер карты введён неверно. "
                                          "Повторите ввод или напишите 'quit' для выхода\n"))


def get_mask_account(score_card: str) -> str:
    """Функция маскировки номера банковского счета"""
    format_score_card = score_card.replace(" ", "")
    if format_score_card.isdigit() is True and len(format_score_card) == 20:
        return f"**{format_score_card[-4:]}"
    elif format_score_card.lower() == "quit":
        return "До свидания!"
    else:
        return get_mask_card_number(input("Номер счёта введён неверно. "
                                          "Повторите ввод или напишите 'quit' для выхода\n"))
