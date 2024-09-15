from datetime import datetime
from masks import get_mask_card_number


def mask_account_card(data_card: str) -> str:
    """Функция, обрабатывающая информацию о картах и счетах"""
    number_card = "".join(el if el.isdigit() else "" for el in data_card)
    number_card_mask = get_mask_card_number(number_card)
    name_card = "".join(el if el.isdigit() else "" for el in data_card)
    data_card_mask = name_card + number_card_mask
    return data_card_mask


def get_date(user_date: str) -> str:
    """Функция. которая приводит дату  к общему формату"""
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
print(get_date("2024-03-11T02:26:18.671407*"))
