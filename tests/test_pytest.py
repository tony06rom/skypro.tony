from src.masks import *
from src.widget import *
from src.processing import *
import pytest
from src.learning import calculate_logarithm, reverse_string

def test_masks():
    assert get_mask_card_number("1234567890123456")
    assert get_mask_account("12345678901234567890")


def test_widget():
    assert mask_account_card("Visa Platinum 7000792289606361")
    assert get_date("Счет 12345678901234567890")


def test_processing():
    assert filter_by_state(origin_data, "EXECUTED")
    assert sort_by_date(origin_data, True)


origin_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_calc_log():
    assert calculate_logarithm(8, 2) == 3.0
    assert calculate_logarithm(8, 4) == 1.5


    with pytest.raises(ValueError):
        calculate_logarithm(0, 2)

    with pytest.raises(ValueError):
        calculate_logarithm(8, 0)


# def test_reverse_string_num(numbers):
#     assert reverse_string('123') == numbers
#
# def test_reverse_string_str(letters):
#     assert reverse_string('hello') == letters

@pytest.mark.parametrize('value, expected', [
    ('123', '321'),
    ('hello', 'olleh'),
    ('world', 'dlrow')
])

def test_reverse_string(value, expected):
    assert reverse_string(value) == expected