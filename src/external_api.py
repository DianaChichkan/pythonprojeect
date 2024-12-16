from locale import currency

import requests
import json
import os
from dotenv import load_dotenv
from src.utils import get_transactions

load_dotenv()
list_of_transactions = get_transactions(r"..\data\operation.json")
print(list_of_transactions)

def get_transaction_amount(transaction: dict) -> float:
    """Функция принимает на вход сумму транзакцию и производит конвертацию в рубли"""
    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        if currency == "RUB":
            return currency
        elif currency == "USD":
            return get_convert_from_to("USD", "RUB", amount)
        elif currency == "EUR":
            return get_convert_from_to("EUR", "RUB", amount)
    except Exception as e:
        print(e)

def get_convert_from_to(from_currency: str, to_currency: str, amount: float) -> float:
    API_KEY = os.getenv("API_KEY")
    url = f'https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}'

    payload = {}
    headers = {"apikey": API_KEY}

    response = requests.request("GET", url, headers=headers, data=payload)
    json = response.json()
    return json['query']['amount']


for transaction in list_of_transactions:
    result = get_transaction_amount(transaction)
    print(result)
