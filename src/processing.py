from typing import Any


def filter_by_state(dictionary_inform: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция задает параметры поиска в исходных данных"""

    list_state = []

    for operation in dictionary_inform:
        if operation.get("state") == state_id:
            list_state.append(operation)
    return list_state


def sort_by_date(data, reverse=True):
    """Функция сортирует исходные данные по дате"""
    sorted_data = sorted(data, key=lambda x: x["date"], reverse=reverse)
    return sorted_data


if __name__ == '__main__':
    dictionary_inform = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    print(sort_by_date(dictionary_inform, False))
