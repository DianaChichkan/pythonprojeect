import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from src.external_api import get_transaction_amount, get_convert_from_to


class TestTransactionConversion(unittest.TestCase):

    @patch("src.external_api.requests.request")
    @patch("src.external_api.os.getenv")
    def test_get_convert_from_to(self, mock_getenv, mock_request):
        mock_getenv.return_value = "fake_api_key"
        mock_response = MagicMock()
        mock_response.json.return_value = {"query": {"amount": 100.0}}
        """Возвращаемый результат API_KEY"""
        mock_request.return_value = mock_response

        result = get_convert_from_to("USD", "RUB", 100.0)

        self.assertEqual(result, 100.0)
        mock_getenv.assert_called_with("API_KEY")
        mock_request.assert_called_once()

    @patch("src.external_api.get_convert_from_to")
    def test_get_transaction_amount(self, mock_convert):
        """Подготовка данных"""
        mock_convert.return_value = 7500.0
        transaction_usd = {"operationAmount": {"currency": {"code": "USD"}, "amount": 100.0}}
        transaction_rub = {"operationAmount": {"currency": {"code": "USD"}, "amount": 5000.0}}

        result_usd = get_transaction_amount(transaction_usd)

        self.assertEquel(result_usd, 7500.0)
        result_rub = get_transaction_amount(transaction_rub)
        self.assertEquel(result_rub, "RUB")

        mock_convert.assert_called_once_with("USD", "RUB", 100.0)


if __name__ == "__main__":
    unittest.main()
