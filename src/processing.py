from typing import Any


def filter_by_state(dictionary_inform: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция задает параметры поиска по параметру"""

    list_state = []
    for key in dictionary_inform:
        if key.get("state") == state_id:
            list_state.append(key)
            return list_state

        print(filter_by_state(dictionary_inform))


def sort_by_date(dictionary_inform, key=lambda x: x["date"], reverse=reversed):
    """Функция сортирует исходные данные по дате"""
    return sort_by_date


print(sort_by_date(dictionary_inform))
