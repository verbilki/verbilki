from typing import Any, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], currency: str = "USD") -> Iterator[dict[str, Any]]:
  """
  :Назначение функции: фильтрация списка словарей банковских операций по значению ключа 'currency'.

  :param transactions: список словарей банковских операций для фильтрации.
  :param currency: значение ключа 'currency' для фильтрации. По умолчанию, 'USD'.
  :return: итератор словарей.
  """

  if currency not in ["USD", "RUB"]:
    raise ValueError("Валюта должна быть одним из: USD, RUB")

  for transaction in transactions:
    if not isinstance(transaction, dict):
      raise TypeError("Значение должно быть словарем.")
    try:
      if "currency" in transaction and "code" in transaction["currency"]:
        if transaction.get("currency", {}).get("code") == currency:
          yield transaction
    except KeyError:
      raise KeyError("В словаре транзакции отсутствует ключ 'currency' или подключ 'code'.")

    except TypeError as e:
      raise TypeError(f"Тип значения ключа 'currency' в словаре транзакции должен быть словарем: {e}")


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[str]:
  """
  Generate an iterator of transaction descriptions from a list of transaction dictionaries.
  Args:
      transactions (list[dict[str, Any]]): A list of dictionaries representing transactions. Each dictionary
          should have a "description" key.
  Yields:
      str: The description of each transaction.
  """
  try:
    for transaction in transactions:
      yield transaction["description"]
  except KeyError:
    raise StopIteration("В словаре транзакции отсутствует ключ 'description'.")


def card_number_generator(start: int, end: int) -> Iterator[str]:
  """
  Generates a sequence of formatted card numbers within a given range.
  Args:
      start (int): The starting value of the range.
      end (int): The ending value of the range.

  Yields:
      str: A formatted card number with spaces between every 4 digits.

  Example:
      >>> card_generator = card_number_generator(1234567890123456, 1234567890123459)
      >>> next(card_generator)
      '1234 5678 9012 3456'
      >>> next(card_generator)
      '1234 5678 9012 3457'
      >>> next(card_generator)
      '1234 5678 9012 3458'
      >>> next(card_generator)
      '1234 5678 9012 3459'
  """
  if start > end:
    raise ValueError("Значение параметра start не может быть больше значения параметра end.")

  if not isinstance(start, int) or not isinstance(end, int):
    raise TypeError("Параметры start и end должны быть целыми числами.")

  if start < 1000000000000000 or end > 9999999999999999:
    raise ValueError(
      "Значения параметров start и end должны быть в диапазоне от 1000000000000000 to 9999999999999999."
    )

  if not (7 <= len(str(start)) <= 16) or not (7 <= len(str(end)) <= 16):
    raise ValueError("Значени параметров start и end должны содержать от 7 до 16 цифр.")

  if not all(char.isdigit() for char in str(start)) or not all(char.isdigit() for char in str(end)):
    raise ValueError("Параметры start и end должны содержать только цифры.")

  for number in range(start, end + 1):
    card_number = str(number).zfill(16)
    formatted_card_number = " ".join([card_number[i: i + 4] for i in range(0, len(card_number), 4)])
    yield formatted_card_number
