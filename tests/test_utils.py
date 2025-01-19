from unittest.mock import Mock, mock_open, patch
from src.utils import read_json_file, summ_transact_rub

# def test_read_json_file(fix_data_read_json_file):
#     mocked_open = mock_open(read_data=fix_data_read_json_file)
#     with patch("builtins.open", mocked_open):
#         result = read_json_file("builtins.open")
#         assert result == [
#             {'id': 414894334, 'state': 'EXECUTED', 'date': '2019-06-30T15:11:53.136004',
#              'operationAmount': {'amount': '95860.47', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#              'description': 'Перевод со счета на счет',
#              'from': 'Счет 59956820797131895975','to': 'Счет 43475624104328495820'}
#         ]


def test_get_read_file_invalid():
    """Проверяет, что функция читает файл и возвращает пустой словарь,
    если файл не содержит данных"""
    mocked_open = mock_open(read_data=None)
    with patch("builtins.open", mocked_open):
        result = read_json_file("builtins.open")
        assert result == []


# def test_summ_transact_rub():
#     mock_random = Mock(return_value=5)
#     random.randint = mock_random
#     assert summ_transact_rub() == 5
#     mock_random.assert_called_once_with(0, 10)


# {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}
# {'id': 596171168, 'state': 'EXECUTED', 'date': '2018-07-11T02:26:18.671407', 'operationAmount': {'amount': '79931.03', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 72082042523231456215'}


"""
Конечно, Владислав! Вот пример использования `mock_open`:

```python
from unittest.mock import mock_open, patch

# Создаем мок для файла
mocked_open = mock_open(read_data='[{"id": 1, "amount": "100.0"}]')

# Используем patch для замены вызова open
with patch('builtins.open', mocked_open):
    # Здесь вызывай свою функцию, которая читает JSON-файл
    result = твоя_функция_чтения_файла('путь_к_файлу')

# Теперь можешь проверить, что result содержит ожидаемые данные
```

Этот код создаст фиктивный файл с указанными данными и заменит вызов `open` на `mocked_open` в контексте `with patch`. Попробуй использовать это в своих тестах!"""