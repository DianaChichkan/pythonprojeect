import json
from json import JSONDecodeError


def get_transactions(path_to_json: str) -> list:
    try:
        with open(path_to_json, "r", encoding="utf-8") as file_json:
            data = json.load(file_json)
            return data
    except FileNotFoundError as file_not_found:
        return []
    except JSONDecodeError as json_decode:
        return []
    except Exception as e:
        print(e)
        return []

print(get_transactions("../data/operation.json"))
