from collections import Counter
from typing import Any


def transact_counter(transact_list: list[dict], transact_category: list) -> Counter[Any] | str:
    """Считает количество банковских операций по категории"""
    descriptions = []
    for data in transact_list:
        if data == {}:
            continue
        else:
            if data["description"] is not None and (data["description"]).lower() in transact_category:
                descriptions.append(data["description"])
            else:
                continue
    counted = Counter(descriptions)

    return counted
