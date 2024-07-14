# from src.widget import get_data, mask_account_card

# print(
#     f'Банковская карта: 1234567890123456, маска: {get_mask_card_number("1234567890123456")}'
# )
# print(
#     f'Банковский счёт: 43210810000000012345, маска: {get_mask_account("43210810000000012345")}'
# )

# print(
#     f'Банковская карта: Visa Platinum 7000792289606361, маска: {mask_account_card("Visa Platinum 7000792289606361")}'
# )
# print(f'Банковская карта: Maestro 7000792289606361, маска: {mask_account_card("Maestro 7000792289606361")}')
# print(f'Счет 73654108430135874305, маска: {mask_account_card("Счет 73654108430135874305")}')
# print(f'Исходная строка даты-времени: 2024-03-11T02:26:18.671407, Результат форматирования: {get_data(
#     "2024-03-11T02:26:18.671407")}')

from src.processing import filter_by_state, sort_by_date

# Тестовый список словарей для проверки функций filter_by_state и sort_by_date
test_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(test_data, "EXECUTED"))
print(filter_by_state(test_data))

print(sort_by_date(test_data))
print(sort_by_date(test_data, True))
print(sort_by_date(test_data, False))
