from src.decorators import log


def test_log_decorator_basic(capsys) -> None:
    """
    Test the basic functionality of the log decorator.

    This test case verifies that the log decorator correctly logs the execution of the `add` function
    and returns the expected result.

    Parameters: None
    Returns: None
    Raises: AssertionError: If the result of the `add` function is not equal to the expected value.
    """

    def add(a: tuple[int]) -> int:
        return sum(a)

    add = log()(add)
    result_1 = add((1, 2))
    captured = capsys.readouterr()

    assert result_1 == 3
    assert "Finished execution of 'add' with status: ok" in captured.out


def test_log_decorator_filename() -> None:
    """
    Test the functionality of the log decorator with a specified filename.

    This test case verifies that the log decorator correctly logs the execution of the `add` function
    with the specified filename and returns the expected result. It also checks if the log file contains
    the expected log messages.

    Parameters: None
    Returns: None
    Raises:
        AssertionError: If the result of the `add` function is not equal to the expected value.
        AssertionError: If the log file does not contain the expected log messages.
    """

    def add(a: tuple[int]) -> int:
        return sum(a)

    add = log(filename="logs/test.log")(add)
    assert add((1, 2)) == 3

    with open("logs/test.log", "r", encoding="utf-8") as file:
        f_read = file.read()
        assert "Starting execution of 'add' with arguments: {'a': (1, 2)}\n" in f_read
        assert "Finished execution of 'add' with status: ok\n" in f_read
