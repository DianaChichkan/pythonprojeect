import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "700079** **** 6361"
    assert get_mask_card_number("70007922896063614567893456") == "700079** **** 3456"
    assert get_mask_card_number("") == "Неверный номер карты"


def test_get_mask_account():
    assert get_mask_account("7000792289606361") == "**6361"
    assert get_mask_account("7000792289606361234567845") == "**7845"
    assert get_mask_account("") == "Неверный номер счета"
