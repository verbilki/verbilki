from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_USD(sample_transactions: list[dict[str, Any]]) -> None:
  """
  Проверка функции filter_by_currency на фильтрацию по валююте USD.
  Parameters:
      sample_transactions (list[dict[str, Any]]): A list of dictionaries representing transactions.
  Returns: None
  """
  try:
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    assert next(usd_transactions) == {
      "id": 939719570,
      "state": "EXECUTED",
      "date": "2018-06-30T02:08:58.425572",
      "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
      "description": "Перевод организации",
      "from": "Счет 75106830613657916952",
      "to": "Счет 11776614605963066702",
    }
  except StopIteration:
    pass


def test_filter_by_currency_RUB(sample_transactions: list[dict[str, Any]]) -> None:
  """
  Проверка функции filter_by_currency на фильтрацию по валююте RUB.

  Parameters:
      sample_transactions (list[dict[str, Any]]): A list of dictionaries representing transactions.
  Returns: None
  """
  try:
    usd_transactions = filter_by_currency(sample_transactions, "RUB")
    assert next(usd_transactions) == {
      "id": 873106923,
      "state": "EXECUTED",
      "date": "2019-03-23T01:09:46.296404",
      "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
      "description": "Перевод со счета на счет",
      "from": "Счет 44812258784861134719",
      "to": "Счет 74489636417521191160",
    }
  except StopIteration:
    pass


def test_filter_by_currency_invalid_currency(sample_transactions: list[dict[str, Any]]) -> None:
  with pytest.raises(ValueError) as exc_info:
    filter_invalid_currency = filter_by_currency(sample_transactions, "EUR")
    next(filter_invalid_currency)
    assert str(exc_info.value) == "Валюта должна быть одним из: USD, RUB"


def test_filter_by_currency_empty_list() -> None:
  """
  Test the filter_by_currency function by passing it an empty list and asserting that a StopIteration exception is
  raised.
  Parameters: None
  Returns: None
  """
  with pytest.raises(StopIteration):
    filter_empty_list = filter_by_currency([], "USD")
    assert next(filter_empty_list) is None


def test_transaction_descriptions(sample_transactions: list[dict[str, Any]]) -> None:
  """
  Test the transaction_descriptions generator function by passing it a sample list of transaction descriptions
  and asserting that the generated descriptions match the expected values.
  Parameters:
      sample_transactions (list[str]): A list of transaction descriptions.
  Returns:
      None
  """
  try:
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
  except StopIteration:
    pass
  finally:
    pass


def test_transaction_descriptions_empty_list() -> None:
  """
  Test the transaction_descriptions generator function by passing it an empty list and asserting
  that a StopIteration exception is raised.
  This test case verifies that the transaction_descriptions generator function correctly handles
  the case when an empty list
  is passed as input.
  It uses the pytest.raises context manager to assert that a StopIteration exception is raised
  when calling the next() function on the result of transaction_descriptions([]).

  Parameters: None
  Returns: None
  """
  with pytest.raises(StopIteration):
    assert next(transaction_descriptions([])) is None


def test_card_number_generator(card_number_range: tuple[int, int]) -> None:
  start, end = card_number_range
  card_numbers = card_number_generator(start, end)

  assert next(card_numbers) == "1234 5678 9012 3456"
  assert next(card_numbers) == "1234 5678 9012 3457"
  assert next(card_numbers) == "1234 5678 9012 3458"
  assert next(card_numbers) == "1234 5678 9012 3459"
