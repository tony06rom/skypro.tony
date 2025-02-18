from collections import Counter

import pytest

from src.transact_counter import transact_counter


@pytest.mark.parametrize(
    "value, categories, expected",
    [
        (
            [
                {"amount": "79931.03", "currency": "RUB", "description": "Открытие вклада"},
                {"amount": "31957.58", "code": "RUB", "description": "Перевод организации"},
            ],
            ["открытие вклада", "перевод организации"],
            Counter({"Открытие вклада": 1, "Перевод организации": 1}),
        ),
        (
            [
                {"amount": "31957.58", "code": "RUB", "description": "Перевод организации"},
                {"amount": "8221.37", "code": "USD", "description": "Перевод со счета на счет"},
            ],
            ["перевод организации", "перевод со счета на счет"],
            Counter({"Перевод организации": 1, "Перевод со счета на счет": 1}),
        ),
        ([], ["Открытие вклада"], Counter()),
    ],
)
def test_transact_counter(value, categories, expected):
    """ Тестирование функции подсчета количества банковских операций по заданным категориям """
    assert transact_counter(value, categories) == expected
