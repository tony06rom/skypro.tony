import re


def filter_by_description(data_to_find: list[dict], search_string: str) -> str | list[dict]:
    """Фильтрует транзакции по описанию"""
    found_transactions = []
    for data in data_to_find:
        if data_to_find == {}:
            continue
        pattern = f"{search_string}"
        match = re.search(pattern, str(data["description"]), flags=re.IGNORECASE)
        if match:
            found_transactions.append(data)
        else:
            continue
    if not found_transactions:
        print("# Не найдено транзакций по введенным данным")
        return []
    else:
        print(f'# Транзакции по фильтру: "{search_string}"')
        return found_transactions
