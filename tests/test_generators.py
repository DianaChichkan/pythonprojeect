import pytest
from src.generators import  filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transactions_list():
    return [
{
    "id": 939719570,
 "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
        "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
          "state": "EXECUTED",
          "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                "amount": "79114.93",
                "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
            }
     ]


@pytest.mark.parametrize("description", ["Перевод организации"])
def test_transaction_descriptions(transactions_list, description):
    """Функция тестирует выдачу списка описания операций"""
    trans = transaction_descriptions(transactions_list)
    assert next(trans) == description


def test_filter_by_currency(transactions_list, transaction):
    """Функция тестирует выдачу списка операция по названию валют"""
    assert list(filter_by_currency(transactions_list, "USD")) == transaction


def test_card_number_generator():
    """Функция тестирует генератор номеров карт"""
    card_number = card_number_generator(9999999999999998, 9999999999999999)
    assert next(card_number) == "9999 9999 9999 9998"
    assert next(card_number) == "9999 9999 9999 9999"

