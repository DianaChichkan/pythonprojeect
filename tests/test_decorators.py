import pytest
from src.decorators import log


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)


def test_my_function(capsys):
    @log()
    def my_function(x, y):
        return x + y

    result = my_function("2", "5")
    captured = capsys.readouterr()
    assert captured.out == "Function started\nFunction finished\nmy_function error: can`t multiply sequence by non-int of type 'str'. Inputs:(('2', '5', {}\n"
    assert result == 7


def test_loging_decorator():
    with pytest.raises(Exception, match="Unsupported operand type(s) for: 'int' and 'str'"):
        my_function(1, 1)