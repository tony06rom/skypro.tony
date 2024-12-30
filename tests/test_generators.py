import pytest
from mypy.erasetype import erase_type

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


def test_filter_by_currency_usd_rub(fix_transactions):
    var_test_filter_by_currency_usd = filter_by_currency(fix_transactions, "USD")
    var_test_filter_by_currency_rub = filter_by_currency(fix_transactions, "RUB")
    assert next(var_test_filter_by_currency_usd) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(var_test_filter_by_currency_usd) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(var_test_filter_by_currency_rub) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(var_test_filter_by_currency_rub) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


#    assert filter_by_currency(fix_transactions, "QWERTY") == []
#    assert filter_by_currency(fix_transactions, "") == []


# def test_filter_if_currency_is_empty(fix_transactions, currency, fix_uniq_code):
#     check_currency = fix_uniq_code(fix_transactions)
#     if currency not in check_currency:
#         assert filter_by_currency(fix_transactions, currency) == f"transact_list without '{currency}'"

# def test_transaction_descriptions(fix_transactions):
#     assert transaction_descriptions(fix_transactions) == fix_sorted_true
#     assert transaction_descriptions(fix_transactions) == fix_sorted_false
#     assert transaction_descriptions(fix_transactions) == fix_sorted_true
#
# @pytest.mark.parametrize("start_range, end_range", [
#         ("1", "10", "f"),
#         ("9999999999999995", "9999999999999999"),
#         ("10", "5", "Выбран неверный диапазон"),
#     ])
# def test_card_number_generator(start_range, end_range, fix_card_number_generator_1_10, fix_card_number_generator_95_99):
#     assert transaction_descriptions(start_range, end_range) == fix_card_number_generator_1_10
#     assert transaction_descriptions(start_range, end_range) == fix_card_number_generator_95_99
#     assert transaction_descriptions(start_range, end_range) == wrong
#
#
# def test_filter_by_currency_errors(fix_transactions, fix_filter_by_state):
#
#     with pytest.raises(StopIteration):
#         filter_by_currency(fix_transactions, fix_filter_by_state)
#
#     with pytest.raises(StopIteration):
#         filter_by_currency(fix_transactions, fix_press_enter)
#
#     with pytest.raises(StopIteration):
#         filter_by_currency(fix_transactions, "qwerty")
#
#
# def test_card_number_generator_start_high_end(ix_card_number_generator_start_high_end):
#     with pytest.raises(AttributeError):
#         card_number_generator(ix_card_number_generator_start_high_end)
