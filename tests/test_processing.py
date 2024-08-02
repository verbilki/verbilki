import pytest

from src.processing import filter_by_state, sort_by_date


# --- filter_by_state ---
@pytest.fixture(scope="module")
def test_filter_by_state_mock_data() -> tuple[list[dict], str, list[dict]]:
    return (
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "EXECUTED",
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
    )


def test_filter_by_state_fixture(test_filter_by_state_mock_data: tuple[list[dict], str, list[dict]]) -> None:
    """
    Test the filter_by_state function using mock data.

    This function tests whether the filter_by_state function correctly filters a list of dictionaries
    based on a given state.

    Parameters:
    test_filter_by_state_mock_data (tuple[list[dict], str, list[dict]]): A tuple containing:
        - A list of dictionaries representing the data to be filtered.
        - A string representing the state to filter by.
        - A list of dictionaries representing the expected filtered result.

    Returns:
    None: This function does not return a value. It asserts that the output of filter_by_state
    matches the expected filtered result.
    """
    assert (
            filter_by_state(test_filter_by_state_mock_data[0], test_filter_by_state_mock_data[1])
            == test_filter_by_state_mock_data[2]
    )


def test_filter_by_state_unknown_state(test_filter_by_state_mock_data: tuple[list[dict], str, list[dict]]) -> None:
    """
    Test the filter_by_state function with an unknown state using mock data.

    This function tests whether the filter_by_state function correctly filters a list of dictionaries
    based on an unknown state.

    Parameters:
    test_filter_by_state_mock_data (tuple[list[dict], str, list[dict]]): A tuple containing:
        - A list of dictionaries representing the data to be filtered.
        - A string representing the unknown state to filter by.
        - An empty list representing the expected filtered result when using an unknown state.

    Returns:
    None: This function does not return a value. It asserts that the output of filter_by_state
    matches an empty list when using an unknown state.
    """
    assert filter_by_state(test_filter_by_state_mock_data[0], "UNKNOWN_STATE") == []


# --- sort_by_date ---
@pytest.fixture(scope="module")
def test_sort_by_date_fixt_desc_order() -> tuple[list[dict], list[dict]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ], [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_desc(test_sort_by_date_fixt_desc_order: tuple[list[dict], list[dict]]) -> None:
    assert sort_by_date(test_sort_by_date_fixt_desc_order[0]) == test_sort_by_date_fixt_desc_order[1]
    assert sort_by_date(test_sort_by_date_fixt_desc_order[0], True) == test_sort_by_date_fixt_desc_order[1]


@pytest.fixture(scope="module")
def test_sort_by_date_fixt_asc_order() -> tuple[list[dict], list[dict]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ], [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_asc(test_sort_by_date_fixt_asc_order: tuple[list[dict], list[dict]]) -> None:
    assert sort_by_date(test_sort_by_date_fixt_asc_order[0], False) == test_sort_by_date_fixt_asc_order[1]


@pytest.fixture(scope="module")
def test_sort_by_date_fixture_same_data() -> tuple[list[dict], list[dict]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ], [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_fixture(test_sort_by_date_fixture_same_data: tuple[list[dict], list[dict]]) -> None:
    """
    Test function to verify the sort_by_date function with the provided test data.

    Args:
        test_sort_by_date_fixture_same_data: A tuple containing the input data to be sorted
        and the expected sorted data.

    Returns:
        None
    """
    assert sort_by_date(test_sort_by_date_fixture_same_data[0]) == test_sort_by_date_fixture_same_data[1]


@pytest.fixture(scope="module")
def test_sort_by_date_fixt_bad_data() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "bad date"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_by_date_bad_date(test_sort_by_date_fixt_bad_data: list[dict]) -> None:
    """
    A test function to check if sort_by_date raises a ValueError when a bad date format is encountered.
    :param test_sort_by_date_fixt_bad_data: List of dictionaries with test data containing bad date formats.
    :return: None
    """
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(test_sort_by_date_fixt_bad_data)
    assert str(exc_info.value) == "Значение ключа 'date' не соответствует формату '%Y-%m-%dT%H:%M:%S.%f'."


@pytest.fixture(scope="module")
def test_sort_by_date_fixt_no_key_date() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_by_date_no_key_date(test_sort_by_date_fixt_no_key_date: list[dict]) -> None:
    with pytest.raises(KeyError) as exc_info:
        sort_by_date(test_sort_by_date_fixt_no_key_date)
    assert exc_info.value.args[0] == "Ключ 'date' отсутствует в одном из словарей."
