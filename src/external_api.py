import os
from typing import Any

import requests
from dotenv import load_dotenv

# Загружаем API-токен из .env
load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"


def convert_amount(all_summ: str, from_currency: str, to_currency: str) -> Any:
    """Конвертирует сумму одной валюты в другую через API"""
    payload = {"amount": all_summ, "from": from_currency, "to": to_currency}
    headers = {"apikey": API_KEY}
    try:
        if all_summ != "0":
            r = requests.get(url, headers=headers, params=payload)
            result = r.json()
            print(result)
            return result["result"]
        else:
            return "0"
    except KeyError as exc_info:
        return f"Error: {type(exc_info).__name__}, Incorrect Value"
