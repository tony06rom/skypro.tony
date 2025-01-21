from unittest.mock import mock_open, patch

from src.utils import read_json_file


def test_read_json_file(fix_data_read_json_valid_file):
    """Проверка на чтение файла с JSON. Возвращает список транзакций"""
    mocked_open = mock_open(read_data=fix_data_read_json_valid_file)
    with patch("builtins.open", mocked_open):
        result = read_json_file("builtins.open")
        assert result == [
            {
                "id": 414894334,
                "state": "EXECUTED",
                "date": "2019-06-30T15:11:53.136004",
                "operationAmount": {"amount": "95860.47", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 59956820797131895975",
                "to": "Счет 43475624104328495820",
            }
        ]


def test_get_read_file_invalid():
    """Проверка на отсутствие JSON в файле. Возвращает пустой список"""
    mocked_open = mock_open(read_data=None)
    with patch("builtins.open", mocked_open):
        result = read_json_file("builtins.open")
        assert result == []


def test_get_read_file_empty_list(fix_data_read_json_empty_list):
    """Проверка на пустой список. Возвращает пустой список"""
    mocked_open = mock_open(read_data=fix_data_read_json_empty_list)
    with patch("builtins.open", mocked_open):
        result = read_json_file("builtins.open")
        assert result == []


def test_get_read_file_not_found_return():
    """Проверка на отсутствие файла. Возвращает пустой список"""
    result = read_json_file("test.json")
    assert result == []
