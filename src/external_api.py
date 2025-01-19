import os
from dotenv import load_dotenv
import requests


# Загружаем API-токен из .env
load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"

def convert_amount(all_summ, from_currency, to_currency):
    payload = {
        "amount": str(all_summ),
        "from": from_currency,
        "to": to_currency
    }
    headers = {
        "apikey": API_KEY
    }
    if all_summ != 0:
        r = requests.get(url, headers=headers, params=payload)
    else:
        return 0

    r_status = r.status_code
    result = r.json()
    return result['result']

# final = convert_amount('100', 'USD', 'RUB')
# print(final)
# print(r_status)
# print(result)

# def read_json_file(open_file):
#     """ Принимает на вход транзакцию и возвращает сумму транзакции в рублях """
#     amount = 0
#     pass
