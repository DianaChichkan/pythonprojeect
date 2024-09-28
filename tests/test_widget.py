import pytest


from src.widget import get_date, mask_account_card


@pytest.fixture
def test_mask_account_card(data_card_mask):
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596** ****5199"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_card("") == "Некорректный ввод"
    with pytest.raises(ValueError) as exc_info:
        data_card_mask("-", "/", "&", "!", "@", ".", "%")
        assert str(exc_info.value) == "Некорректный ввод данных"


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2.24-03-1/T02:26:18.671407") == "Некорректный ввод"
    assert get_date("2024-03-11T02:") == "Некорректный ввод"
    assert get_date("") == "Некорректный ввод"
    with pytest.raises(ValueError) as exc_info:
        get_date("-", "/", "&", "!", "@", ".", "%")
        assert str(exc_info.value) == "Некорректный ввод данных"
