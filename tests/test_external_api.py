from unittest.mock import patch

import requests

from src.external_api import convert_amount


@patch("requests.get")
def test_convert_amount(mock_get):
    mock_get.return_value.json.return_value = {"result": 102}
    response = requests.get(
        "https://api.apilayer.com/exchangerates_data/convert", headers={"amount": "1", "from": "USD", "to": "RUB"}
    )
    assert response.json()["result"] == 102


def test_convert_amount__key_error():
    """Проверка на правильность данных. Будет вызвано исключение KeyError"""
    assert convert_amount("100", "RUB", "доллар") == "Error: KeyError, Incorrect Value"
