import pytest
from src.widget import get_date, mask_account_card
# Прикрутить параметризацию еще на 1 случай(isa Platinum "номер")

def test_mask_account_card():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_card("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"



def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_value_error():
    with pytest.raises(ValueError):
        get_date("202403-11T02:26:18.671407")