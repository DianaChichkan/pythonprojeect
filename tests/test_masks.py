import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("data, expected", (("7000792289606361", "7000 79** **** 6361"), ("", "Неверный номер карты")))
def test_get_mask_card_number(data, expected):
    assert get_mask_card_number(data) == expected


def test_get_mask_account():
    assert get_mask_account("7000792289606361234567845") == "**7845"
    assert get_mask_account("") == "Неверный номер счета"
