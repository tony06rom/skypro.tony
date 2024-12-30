import pytest


@pytest.fixture
def fix_press_enter():
    return "\r"


@pytest.fixture
def fix_origin_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def fix_sorted_executed():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def fix_sorted_canceled():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def fix_sorted_true():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def fix_sorted_false():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def fix_transactions():
    return [
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


# @pytest.fixture
# def fix_filter_by_currency_usd():
#     yield {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
#          'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
#          'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
#          'to': 'Счет 11776614605963066702'}
#     yield {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
#          'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
#          'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
#          'to': 'Счет 75651667383060284188'}
#
#
# @pytest.fixture
# def fix_filter_by_currency_rub():
#     yield {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
#          'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#          'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',
#          'to': 'Счет 74489636417521191160'}
#     yield {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689',
#          'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#          'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588',
#          'to': 'Счет 14211924144426031657'}


@pytest.fixture
def fix_uniq_code(start_data):
    currency_code = []
    for data in start_data:
        if data["operationAmount"]["currency"]["code"] not in currency_code:
            currency_code.append(data["operationAmount"]["currency"]["code"])
    return currency_code

print(fix_uniq_code(fix_transactions()))

@pytest.fixture
def fix_card_number_generator_1_10():
    yield "0000 0000 0000 0001"
    yield "0000 0000 0000 0002"
    yield "0000 0000 0000 0003"
    yield "0000 0000 0000 0004"
    yield "0000 0000 0000 0005"
    yield "0000 0000 0000 0006"
    yield "0000 0000 0000 0007"
    yield "0000 0000 0000 0008"
    yield "0000 0000 0000 0009"
    yield "0000 0000 0000 0010"


@pytest.fixture
def fix_card_number_generator_95_99():
    yield "9999 9999 9999 9995"
    yield "9999 9999 9999 9996"
    yield "9999 9999 9999 9997"
    yield "9999 9999 9999 9998"
    yield "9999 9999 9999 9999"


@pytest.fixture
def fix_card_number_generator_10_5():
    yield "9999 9999 9999 9995"
    yield "9999 9999 9999 9996"
    yield "9999 9999 9999 9997"
    yield "9999 9999 9999 9998"
    yield "9999 9999 9999 9999"

@pytest.fixture
def ix_card_number_generator_start_high_end(start, end):
    if start > end:
        return "Выбран неверный диапазон"
