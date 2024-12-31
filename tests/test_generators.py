import pytest
from mypy.erasetype import erase_type

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions


def test_filter_by_currency_usd_rub(fix_transactions):
    var_test_filter_by_currency_usd = filter_by_currency(fix_transactions, "USD")
    var_test_filter_by_currency_rub = filter_by_currency(fix_transactions, "RUB")
    assert next(var_test_filter_by_currency_usd) == {
        "id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации", "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }
    assert next(var_test_filter_by_currency_usd) == {
        "id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
    assert next(var_test_filter_by_currency_usd) == {
        "id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту", "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
        }
    assert next(var_test_filter_by_currency_rub) == {
        "id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет", "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }
    assert next(var_test_filter_by_currency_rub) == {
        "id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации", "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }

def test_filter_by_currency_or_list_miss(fix_transactions):
    assert next(filter_by_currency(fix_transactions, "QWERTY")) == "Транзакций в валюте 'QWERTY' нет"
    assert next(filter_by_currency([], "USD")) == "Список транзакций пуст"


def test_transaction_descriptions(fix_transactions):
    gen_descript = transaction_descriptions(fix_transactions)
    assert next(gen_descript) == "Перевод организации"
    assert next(gen_descript) == "Перевод со счета на счет"
    assert next(gen_descript) == "Перевод со счета на счет"
    assert next(gen_descript) == "Перевод с карты на карту"
    assert next(gen_descript) == "Перевод организации"


def test_transaction_descriptions_empty_list(empty_descript_list):
    gen_descript_empty_list = transaction_descriptions([])
    gen_descript_empty_descript = transaction_descriptions(empty_descript_list)
    assert next(gen_descript_empty_list) == "Список транзакций пуст"
    assert next(gen_descript_empty_descript) == "Данных по операциям нет"


@pytest.mark.parametrize("start_range, end_range, result", [
        (1, 10, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004",
        "0000 0000 0000 0005", "0000 0000 0000 0006", "0000 0000 0000 0007", "0000 0000 0000 0008",
        "0000 0000 0000 0009", "0000 0000 0000 0010"]),
        (9999999999999995, 9999999999999999, ["9999 9999 9999 9995", "9999 9999 9999 9996", "9999 9999 9999 9997", "9999 9999 9999 9998",
        "9999 9999 9999 9999"])
])
def test_card_number_generator(start_range, end_range, result):
    gen_card_number_generator = card_number_generator(start_range, end_range)
    assert list(gen_card_number_generator) == result


def test_card_number_generator_wrong_range():
    gen_card_number_generator_wrong = card_number_generator(5, 3)
    assert next(gen_card_number_generator_wrong) == "Выбран неверный диапазон"
