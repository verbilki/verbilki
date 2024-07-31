from datetime import datetime
from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    :Назначение функции: фильтрация списка словарей банковских операций по значению ключа 'state'.

    :param data: список словарей банковских операций для фильтрации.
    :param state: значение ключа 'state' для фильтрации. По умолчанию, 'EXECUTED'.
    :return: список словарей.
    """
    return [item for item in data if item["state"] == state]


def sort_by_date(data: list[dict[str, Any]], is_sort_order: bool = True) -> list[dict[str, Any]]:
    """
    :Назначение функции: сортировка списка словарей банковских операций по дате операции
    :param data: список словарей банковских операций для фильтрации.
    :param: is_sort_order: булевый флаг направления сортировки по датам операций.
                          (True (по умолчанию) - по убыванию дат; False - по возрастанию дат).
    :return: отсортированный список словарей
    """
    for d in data:
        if "date" in d:
            try:
                datetime.strptime(d["date"], "%Y-%m-%dT%H:%M:%S.%f")
            except ValueError:
                raise ValueError("Значение ключа 'date' не соответствует формату '%Y-%m-%dT%H:%M:%S.%f'.")
        else:
            raise KeyError("Ключ 'date' отсутствует в одном из словарей.")

    return sorted(data, key=lambda item: item["date"], reverse=is_sort_order)
