import pytest

from src.widget import get_data, mask_account_card


# --- mask_account_card ---
@pytest.fixture(scope="module")
def card_or_acc_number() -> tuple[str, str]:
  return "Visa Classic 2200792289606361", "Visa Classic 2200 79** **** 6361"


def test_mask_account_card_fixture(card_or_acc_number: str) -> None:
  assert mask_account_card(card_or_acc_number[0]) == card_or_acc_number[1]


@pytest.mark.parametrize(
  "card_or_acc_number, expected",
  [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Visa 4111111111111111", "Visa 4111 11** **** 1111"),
  ],
)
def test_mask_account_card(card_or_acc_number: str, expected: str) -> None:
  assert mask_account_card(card_or_acc_number) == expected


def test_mask_account_card_error() -> None:
  with pytest.raises(ValueError) as exc_info:
    mask_account_card("12345678901234567890")
  assert (
          str(exc_info.value) == "Номер карты должен начинаться с наименования платежной системы,"
                                 " а номер счёта должен начинаться со слова 'Счет'."
  )


# --- get_data ---


@pytest.mark.parametrize(
  "raw_date_str, expected",
  [
    ("2023-10-01T12:34:56.789012", "01.10.2023"),
    ("2022-01-15T00:00:00.000000", "15.01.2022"),
    ("2020-02-29T23:59:59.999999", "29.02.2020"),
    ("2019-12-31T23:59:59.999999", "31.12.2019"),
    ("2000-01-01T00:00:00.000000", "01.01.2000"),
    ("", ""),
  ],
)
def test_get_data(raw_date_str: str, expected: str) -> None:
  assert get_data(raw_date_str) == expected


def test_get_data_error() -> None:
  err_datetime_str = "2023-13-01T12:34:56.789012"
  with pytest.raises(ValueError) as exc_info:
    get_data(err_datetime_str)
  assert str(exc_info.value) == f"Error: time data '{err_datetime_str}' does not match format '%Y-%m-%dT%H:%M:%S.%f'"
