import pytest

from src.decorators import log


@log()
def my_function(x, y):
    """Функция, которая суммирует два числа"""
    return x + y


def test_test_console_ok(capsys):
    """Тест функции, при которой логи будут записываться в файл"""
    my_function(2, 3)
    output = capsys.readouterr()
    assert output.out == "my_function ok\n"


def test_log_console_error(capsys):
    """Тест функции, при которой логи выводятся в консоль"""
    my_function(2, "3")
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: (2, '3'), {}\n"
