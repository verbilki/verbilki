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

3. Установить линтеры flake8, black, isort, mypy.

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
    {'id': 41428829,  'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Сортировка списка словарей test_data по статусу операций (ключ 'state') 'EXECUTED' 
print(filter_by_state(test_data, 'EXECUTED'))
# Сортировка списка словарей test_data по дефолтному статусу операций (т.е. аргумент state равен 'EXECUTED')
print(filter_by_state(test_data))

# Сортировка списка словарей test_data по дефолтному направлению сортировки (т.е. по убыванию ключа 'date')
print(sort_by_date(test_data))
# Сортировка списка словарей test_data по убыванию ключа 'date' (т.к. аргумент is°sort_order имеет значение True)
print(sort_by_date(test_data, True))
# Сортировка списка словарей test_data по возрастанию ключа 'date' (т.к. аргумент is_sort_order имеет значение False)
print(sort_by_date(test_data, False))
```
## Лицензия
[GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html#license-text)