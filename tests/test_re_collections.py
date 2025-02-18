import pytest

from src.re_collections import filter_by_description


@pytest.mark.parametrize(
    "value, string_search, expected",
    [
        (
            [
                {
                    "id": 619287771,
                    "state": "EXECUTED",
                    "date": "2019-08-19T16:30:41.967497",
                    "operationAmount": {"amount": "81150.87", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 17691325653939384901",
                    "to": "Счет 49304996510329747621",
                },
                {
                    "id": 490100847,
                    "state": "EXECUTED",
                    "date": "2018-12-22T02:02:49.564873",
                    "operationAmount": {"amount": "56516.63", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Gold 8326537236216459",
                    "to": "MasterCard 6783917276771847",
                },
            ],
            "организации",
            [
                {
                    "id": 619287771,
                    "state": "EXECUTED",
                    "date": "2019-08-19T16:30:41.967497",
                    "operationAmount": {"amount": "81150.87", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 17691325653939384901",
                    "to": "Счет 49304996510329747621",
                }
            ],
        ),
        (
            [
                {
                    "id": 179194306,
                    "state": "EXECUTED",
                    "date": "2019-05-19T12:51:49.023880",
                    "operationAmount": {"amount": "6381.58", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "МИР 5211277418228469",
                    "to": "Счет 58518872592028002662",
                },
                {
                    "id": 27192367,
                    "state": "CANCELED",
                    "date": "2018-12-24T20:16:18.819037",
                    "operationAmount": {"amount": "991.49", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 71687416928274675290",
                    "to": "Счет 87448526688763159781",
                },
            ],
            "на счет",
            [
                {
                    "id": 27192367,
                    "state": "CANCELED",
                    "date": "2018-12-24T20:16:18.819037",
                    "operationAmount": {"amount": "991.49", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 71687416928274675290",
                    "to": "Счет 87448526688763159781",
                }
            ],
        ),
        (
            [
                {
                    "id": 921286598,
                    "state": "EXECUTED",
                    "date": "2018-03-09T23:57:37.537412",
                    "operationAmount": {"amount": "25780.71", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Счет 26406253703545413262",
                    "to": "Счет 20735820461482021315",
                },
                {
                    "id": 957763565,
                    "state": "EXECUTED",
                    "date": "2019-01-05T00:52:30.108534",
                    "operationAmount": {"amount": "87941.37", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 46363668439560358409",
                    "to": "Счет 18889008294666828266",
                },
            ],
            "вклада",
            [],
        ),
        ([], "вклада", []),
    ],
)
def test_filter_by_description(value, string_search, expected):
    """Тестирование функции поиска словарей по заданной строке в описании транзакций"""
    assert filter_by_description(value, string_search) == expected
