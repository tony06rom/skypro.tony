from src.decorators import decor_log as decor


@decor(filename="../wraps/log_processing.txt")
def filter_by_state(filter_data: list[dict[str, int]], state: str = "EXECUTED") -> list[dict[str, int]]:
    """Словарь с фильтром state.
    Принимает на вход список словарей, делает выборку по совпадению значения ключа state.
    Далее выводит список словарей с совпадающим state"""
    filter_data_state = []
    for data in filter_data:
        for state_of_data in data.values():
            if state_of_data == state:
                filter_data_state.append(data)
    return filter_data_state


@decor(filename="../wraps/log_processing.txt")
def sort_by_date(sort_data: list[dict[str, int]], reverse: bool = True) -> list[dict[str, int]]:
    """Словарь отсортированный по дате.
    Принимает на вход список словарей, имеет стандартную сортировку в обратном порядке по data.
    Далее выводит список словарей в обратном порядке, если не было задано другой сортировки"""
    sorted_data = sorted(sort_data, key=lambda x: x["date"], reverse=reverse)
    return sorted_data
