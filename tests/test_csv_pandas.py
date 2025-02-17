from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.csv_pandas import csv_worker, excel_worker

""" Тесты для функции считывания финансовых операций из CSV используют Mock и patch. """


def test_csv_worker_success(fix_valid_data_for_csv_worker, fix_valid_return_for_csv_worker):
    """Проверка на чтение файла с CSV. Возвращает список транзакций"""
    mocked_open = mock_open(read_data=fix_valid_data_for_csv_worker)
    with patch("builtins.open", mocked_open) as mocked_open:
        result = csv_worker("builtins.open")
        assert result == fix_valid_return_for_csv_worker
        mocked_open.assert_called_once_with("builtins.open", mode="r", encoding="utf-8")


def test_csv_worker_file_not_found_error(capsys):
    """Проверка на наличие Excel файла. Выход из программы"""
    with pytest.raises(SystemExit):
        csv_worker("builtins.open")
    out, err = capsys.readouterr()
    assert out == "Файл не найден\n"
    print(out, err)


def test_read_csv_file_invalid_data(capsys):
    """Проверка на наличие корректных данных в CSV файле. Выход из программы"""
    mocked_open = mock_open(read_data=None)
    with patch("builtins.open", mocked_open):
        with pytest.raises(SystemExit):
            csv_worker("builtins.open")
    out, err = capsys.readouterr()
    assert out == "Файл не содержит корректных данных\n"
    print(out, err)


def test_read_csv_file_empty_file(capsys, fix_empty_return_for_csv_worker):
    """Проверка на отсутствие данных в файле. Выход из программы"""
    mocked_open = mock_open(read_data=fix_empty_return_for_csv_worker)
    with patch("builtins.open", mocked_open):
        with pytest.raises(SystemExit):
            csv_worker("builtins.open")
    out, err = capsys.readouterr()
    assert out == "Файл не содержит корректных данных\n"
    print(out, err)


""" Тесты для функции считывания финансовых операций из XLSX используют Mock и patch. """


@patch("pandas.read_excel")
def test_excel_worker_file(mock_read_excel: pd.DataFrame):
    """Проверка на чтение файла с Excel. Возвращает список транзакций"""
    sample_data = {"id": [650703, 3598919], "description": ["Перевод организации", "Перевод с карты на карту"]}
    mock_data = pd.DataFrame(sample_data)
    mock_read_excel.return_value = mock_data
    result = excel_worker("sample")
    expected = [
        {"id": 650703, "description": "Перевод организации"},
        {"id": 3598919, "description": "Перевод с карты на карту"},
    ]
    assert result == expected


@patch("pandas.read_excel")
def test_excel_worker_invalid_data(mock_read_excel: pd.DataFrame):
    """Проверка на наличие корректных данных в Excel файле. Возвращает пустой список"""
    mock_data = pd.DataFrame(None)
    mock_read_excel.return_value = mock_data
    result = excel_worker("sample")
    expected = []
    assert result == expected


def test_excel_worker_file_not_found(capsys):
    """Проверка на наличие Excel файла. Выход из программы"""
    with pytest.raises(SystemExit):
        excel_worker("builtins.open")
    out, err = capsys.readouterr()
    assert out == "Файл не найден\n"
    print(out, err)
