from src.decorators import decor_log as decor


@decor(filename="log.txt")
@decor("")
def func_test(x, y):
    result = int(x) / int(y)
    return result


def test_log_no_errors(capsys):

    func_test("15", "3")
    captured = capsys.readouterr()
    assert captured.out[58:-26] == "Function: func_test | Args: ('15', '3') | Kwargs: {}\nStatus 'OK' | Result: 5.0\n"

    file = open("log.txt", "r")
    line = file.readlines()
    file.close()
    assert line[-2] == "Status 'OK' | Result: 5.0\n"


def test_log_if_not_number(capsys):
    func_test("5", "asd")
    captured = capsys.readouterr()
    assert captured.out[58:-26] == (
        "Function: func_test | Args: ('5', 'asd') | Kwargs: {}\n"
        "Status 'ERROR' | ValueError: invalid literal for int() with base 10: 'asd'\n"
    )

    file = open("log.txt", "r")
    line = file.readlines()
    file.close()
    assert line[-2] == "Status 'OK' | Result: None\n"


def test_log_if_zero_dvision(capsys):
    func_test("5", "0")
    captured = capsys.readouterr()
    assert captured.out[58:-26] == (
        "Function: func_test | Args: ('5', '0') | Kwargs: {}\n"
        "Status 'ERROR' | ZeroDivisionError: division by zero\n"
    )

    file = open("log.txt", "r")
    line = file.readlines()
    file.close()
    assert line[-2] == "Status 'OK' | Result: None\n"
