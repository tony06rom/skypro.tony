import json
import os
from pathlib import Path
from dotenv import load_dotenv


# Директория ./data/
ROOT_DIR=Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / 'data'

# Загружаем API-токен из .env
load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


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

print(read_json_file("empty"))
print(read_json_file("mistake_json"))
print(read_json_file("not_json"))
print(read_json_file("йцукенег47435пукп34н"))
print(read_json_file("operations"))
