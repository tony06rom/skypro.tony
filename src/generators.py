from typing import Any


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transact_list: list[dict[Any, Any]], currency: str) -> Any:
    """Принимает список транзакций.
    Возвращает итератор, который поочередно выдает транзакции, где currency - валюта"""
    for transaction in transact_list:
        if currency in transaction["operationAmount"]["currency"]["code"]:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        else:
            return f"transact_list without '{currency}'"


def transaction_descriptions(transact_list: list[dict[str, int]]) -> Any:
    """Принимает список транзакций и возвращает описание каждой операции по очереди"""
    is_list = isinstance(transact_list, list)
    if is_list is True:
        for transaction in transact_list:
            if "description" in transaction:
                if transaction.get("description") == '':
                    yield "descriptionIsEmpty"
                else:
                    yield transaction.get("description")
            else:
                yield "descriptionNotInTransact"
    else:
        return "TransactListIsNotList"


def card_number_generator(start_range: int, end_range: int) -> Any:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    Генератор генерирует номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров"""
    if start_range < end_range:
        for number in range(start_range, end_range + 1):
            new_number = str(number)
            while len(new_number) < 16:
                new_number = "0" + new_number
            format_card_number = f"{new_number[0:4]} {new_number[4:8]} {new_number[8:12]} {new_number[12:16]}"
            yield format_card_number
    else:
        print("Выбран неверный диапазон")


# t = filter_by_currency(transactions, 'e56SD')
# for i in range(2):
#     print(next(t))
