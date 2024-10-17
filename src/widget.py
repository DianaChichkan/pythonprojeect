from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data_card: str) -> str:
    """Функция, обрабатывающая информацию о картах и счетах"""
    if data_card.startswith("Счет"):
        parts = data_card.split()
        number = parts[-1]
        hid_number = get_mask_account(number)
    else:
        parts = data_card.split()
        number = parts[-1]
        hid_number = get_mask_card_number(number)
    parts[-1] = hid_number
    return " ".join(parts)


def get_date(user_date: str) -> str:
    """Функция, которая приводит дату к общему формату"""

    date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
