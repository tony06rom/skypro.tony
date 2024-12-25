import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_user, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("quit", "До свидания!"),
    ],
)
def test_widget_account_card(input_user, expected):
    assert mask_account_card(input_user) == expected


def test_widget_account_card_errors():
    with pytest.raises(OSError):
        mask_account_card("")
    with pytest.raises(OSError):
        mask_account_card("Счет 12345678901234567")
    with pytest.raises(OSError):
        mask_account_card("Visa 12345678901234567890")
    with pytest.raises(OSError):
        mask_account_card("Отчёт 123456789012345678901")


@pytest.mark.parametrize(
    "now, expected",
    [
        ("2024-02-11T07:26:53.633677", "11.02.2024"),
        ("1990-09-07T02:27:18", "07.09.1990"),
        ("2025-05-29T", "29.05.2025"),
        ("2025-05-29", "Неизвестный формат даты и времени"),
        ("2024-02-11WWW07:26:53.633677", "Неизвестный формат даты и времени"),
    ],
)
def test_get_date(now, expected):
    assert get_date(now) == expected
