<h2 align="center">
Домашнее задание по уроку 10.1
</h2>

Этот проект представляет собой Домашнее Задание ученика Олега Жадана (поток Prof 40.0) по уроку 10.1.

## Инструкция по установке

1. Создать в PyCharm виртуальное окружение

### Для Windows

```commandline
python -m venv venv
```

### Для Linux, macOS

```bash
python3 -m venv venv
```

2. Активировать виртуальное окружение
   Следующую команду следует запускать из корня проекта:

### Для Windows

```commandline
venv\Scripts\activate
```

### Для Linux, macOS

```bash
source ./venv/bin/activate
```

3. Установить Poetry.
4. Установить линтер flake8 и форматтеры black, isort, mypy на основании файла конфигурации pyproject.toml.

```bash
poetry install
```

## Функциональности

- функция *filter_by_state()* фильтрует список словарей банковских операций по заданному значению ключа *state*.
  Аргумент *state* имеет значение по умолчанию 'EXECUTED';
- функция *sort_by_date()* фильтрует список словарей банковских операций по дате операции (ключ 'date').
  Второй аргумент *is_sort_order* задаёт направление сортировки по датам.
  Значение по умолчанию - True (т.е. по убыванию ключа 'date').
  Если аргумент *sort_order* имеет значение False, то сортировка производится по возрастанию ключа 'date'.

## Примеры использования

```python
# Тестовый список словарей для проверки функций filter_by_state и sort_by_date
test_data = [
  {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
  {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
  {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
  {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Сортировка списка словарей test_data по статусу операций (ключ 'state') 'EXECUTED'
print(filter_by_state(test_data, "EXECUTED"))
# Сортировка списка словарей test_data по дефолтному статусу операций (т.е. аргумент state равен 'EXECUTED')
print(filter_by_state(test_data))

# Сортировка списка словарей test_data по дефолтному направлению сортировки (т.е. по убыванию ключа 'date')
print(sort_by_date(test_data))
# Сортировка списка словарей test_data по убыванию ключа 'date' (т.к. аргумент is°sort_order имеет значение True)
print(sort_by_date(test_data, True))
# Сортировка списка словарей test_data по возрастанию ключа 'date' (т.к. аргумент is_sort_order имеет значение False)
print(sort_by_date(test_data, False))

```

## Testing Functions

### Testing Functions in test_masks.py

- The [test_get_mask_account](cci:1:///home/joel/PycharmProjects/skypro_prof_40__prj01/tests/test_masks.py:64:0-68:58)
  function tests
  the [get_mask_account](cci:1:///home/joel/PycharmProjects/skypro_prof_40__prj01/src/masks.py:24:0-32:37) function
  in `test_masks.py`. It takes an account number and an expected mask as input and asserts that
  the [get_mask_account](cci:1:///home/joel/PycharmProjects/skypro_prof_40__prj01/src/masks.py:24:0-32:37) function
  returns the expected mask.

-

The [test_get_mask_account_fixture](cci:1:///home/joel/PycharmProjects/skypro_prof_40__prj01/tests/test_masks.py:60:0-61:65)
function tests the [get_mask_account](cci:1:///home/joel/PycharmProjects/skypro_prof_40__prj01/src/masks.py:24:0-32:37)
function in `test_masks.py` using a pytest fixture. It takes a tuple of account number and expected mask as input and
asserts that the [get_mask_account](cci:1:///home/joel/PycharmProjects/skypro_prof_40__prj01/src/masks.py:24:0-32:37)
function returns the expected mask.

### Testing Functions in test_widget.py

- The `test_get_data` function tests the `get_data` function in `test_widget.py`. It asserts that the `get_data`
  function returns the expected data.

- The `test_mask_account_card` function tests the `mask_account_card` function in `test_widget.py`. It asserts that
  the `mask_account_card` function returns the expected masked account and card number.

### Тестовые функции в модуле tests/test_processing.py

- тестирования функции filter_by_state() из модуля src/processing.py:

1) функция test_filter_by_state_fixture проверяет корректность фильтрации списка словарей по заданному значению ключа '
   state'.
2) функция test_filter_by_state_unknown_state() проверяет, что фильтрация списка словарей по неизвестному статусу
   приводит к пустому списку словарей.

- тестирования функции sort_by_date() из модуля src/processing.py:

1) функция test_sort_by_date_desc() проверяет корректность сортировки списка словарей в порядке убывания ключа 'date'.
2) функция test_sort_by_date_bad_date() проверяет появление исключения ValueError при появлении некорректного значения
   ключа 'date' в каком-либо словаре списка.

### Функции модуля src/generators.py

#### Функция-итератор filter_by_currency

filter_by_currency(transactions: list[dict[str, any]], currency: str = "USD") -> Iterator[dict[str, any]]:
Purpose: Filters a list of transaction dictionaries by currency code.
Parameters:
transactions (conftest.py): A list of dictionaries representing transactions.
currency (optional): The currency code to filter by. Defaults to "USD".
Return: An iterator of filtered transaction dictionaries.
Пример использования:
```python
from src.generators import filter_by_currency

# Создаем список транзакций
transactions = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2022-01-01",
        "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод на карту",
        "from": "Счет 1234567890",
        "to": "Карта 9876543210",
    },
    {
        "id": 2,
        "state": "EXECUTED",
        "date": "2022-01-02",
        "operationAmount": {"amount": "200", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод на счет",
        "from": "Счет 9876543210",
        "to": "Счет 1234567890",
    },
]

# Фильтруем транзакции по валюте
usd_transactions = filter_by_currency(transactions, "USD")

# Выводим транзакции
for transaction in usd_transactions:
    print(transaction)
'''

#### Функция-итератор transaction_descriptions
transaction_descriptions(transactions: list[dict[str, any]]) -> Iterator[str]:
Purpose: Generates an iterator of transaction descriptions from a list of transaction dictionaries.
Parameters:
transactions (conftest.py): A list of dictionaries representing transactions.
Return: An iterator of transaction descriptions.

## Пример использования функции transaction_descriptions

```python
from src.generators import transaction_descriptions

# Создаем список транзакций
transactions = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2022-01-01",
        "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод на карту",
        "from": "Счет 1234567890",
        "to": "Карта 9876543210",
    },
    {
        "id": 2,
        "state": "EXECUTED",
        "date": "2022-01-02",
        "operationAmount": {"amount": "200", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод на счет",
        "from": "Счет 9876543210",
        "to": "Счет 1234567890",
    },
]

# Получаем описания транзакций
transaction_descriptions = transaction_descriptions(transactions)

# Выводим описания
for description in transaction_descriptions:
    print(description)
'''

#### Генераторная функция card_number_generator 
card_number_generator(start: int, end: int) -> Iterator[str]:
Purpose: Generates a sequence of formatted card numbers within a given range.
Parameters:
start: The starting value of the range.
end: The ending value of the range.
Return: An iterator of formatted card numbers.

### Пример использования функции card_number_generator

```python
from src.generators import card_number_generator

# Создаем генератор карточных номеров
card_number_generator = card_number_generator(234567890123456, 1234567890123465)

# Генерируем 10 карточных номеров
card_numbers = [next(card_number_generator) for _ in range(10)]

# Выводим карточные номера
for card_number in card_numbers:
    print(card_number)
'''

## Лицензия

[GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html#license-text)