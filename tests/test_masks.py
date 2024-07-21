import pytest

from src.masks import get_mask_account, get_mask_card_number


# ---- get_mask_card_number ------
@pytest.fixture(scope="module")
def fixture_card_number() -> tuple[str, str]:
    return "4321000000332345", "4321 00** **** 2345"


def test_get_mask_card_number_fixture(fixture_card_number: tuple[str, str]) -> None:
    assert get_mask_card_number(fixture_card_number[0]) == fixture_card_number[1]


@pytest.mark.parametrize(
    "card_number, expected_mask",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("7000792289606361", "7000 79** **** 6361"),
        ("4321000000012345", "4321 00** **** 2345"),
        ("", ""),
    ],
)
def test_get_mask_card_number(card_number: str, expected_mask: str) -> None:
    assert get_mask_card_number(card_number) == expected_mask


# Тест на длину номера карты. не равную 16.


def test_get_mask_card_number_length_error() -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("123456789012345")
    assert str(exc_info.value) == "Номер карты должен состоять из 16 цифр."


# Тест на проверку наличия нецифровых символов в номере карты.
@pytest.mark.parametrize(
    "card_number",
    [
        "1234abcd56789012",  # Contains letters
        "1234 5678 9012 3456",  # Contains spaces
        "1234-5678-9012-3456",  # Contains hyphens
        "1234!5678@9012#3456",  # Contains special characters
        "1234.5678.9012.3456",  # Contains dots
    ],
)
def test_get_mask_card_number_non_digital_symbols(card_number: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)
    assert str(exc_info.value) == "Номер карты должен состоять только из цифр."


# ----- get_mask_account ------
@pytest.fixture(scope="module")
def account_number() -> tuple[str, str]:
    return "43210810000000017890", "**7890"


def test_get_mask_account_fixture(account_number: tuple[str, str]) -> None:
    assert get_mask_account(account_number[0]) == account_number[1]


@pytest.mark.parametrize(
    "account_number, expected_mask", [("43210810000000012345", "**2345"), ("73654108430135874305", "**4305"), ("", "")]
)
def test_get_mask_account(account_number: str, expected_mask: str) -> None:
    assert get_mask_account(account_number) == expected_mask
