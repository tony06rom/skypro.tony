import json
from pathlib import Path
from src.external_api import convert_amount


# Директория ./data/
ROOT_DIR=Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / 'data'


def read_json_file(open_file):
    """ Принимает на вход имя JSON-файла по пути ./data/ и
    возвращает список словарей с данными о финансовых транзакциях """
    open_file += '.json'
    try:
        with open(DATA_DIR / open_file, 'r', encoding='utf-8') as jf:
            try:
                json_obj = json.load(jf)
                if json_obj:
                    return json_obj
                else:
                    print("Файл содержит пустой список")
                    return []
            except json.JSONDecodeError:
                print("Объект не является JSON или JSON имеет неверный формат")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []


def summ_transact_rub(finance_transacts):
    """ Принимает на вход транзакцию и возвращает сумму транзакции в рублях """
    amount_all_transacts = 0
    amount_usd_transacts = 0
    amount_eur_transacts = 0
    for transaction in finance_transacts:
        if "operationAmount" in transaction:
            print(transaction)
            if transaction["operationAmount"]["currency"]["code"] == 'RUB':
                amount_all_transacts += float(transaction["operationAmount"]["amount"])
            elif transaction["operationAmount"]["currency"]["code"] == 'USD':
                amount_usd_transacts += float(transaction["operationAmount"]["amount"])
            elif transaction["operationAmount"]["currency"]["code"] == 'EUR':
                amount_eur_transacts += float(transaction["operationAmount"]["amount"])
        else:
            continue


    convert_usd = convert_amount(amount_usd_transacts, 'USD', 'RUB')
    convert_eur = convert_amount(amount_eur_transacts, 'EUR', 'RUB')
    final = round((amount_all_transacts+convert_usd+convert_eur), 2)
    return f'{final} руб.'

# print(read_json_file("empty"))
# print(read_json_file("mistake_json"))
# print(read_json_file("not_json"))
# print(read_json_file("йцукенег47435пукп34н"))
#print(read_json_file("operations"))

print(summ_transact_rub(read_json_file("operations")))