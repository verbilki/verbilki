from src.widget import get_data, mask_account_card

# print(
#     f'Банковская карта: 1234567890123456, маска: {get_mask_card_number("1234567890123456")}'
# )
# print(
#     f'Банковский счёт: 43210810000000012345, маска: {get_mask_account("43210810000000012345")}'
# )

print(
    f'Банковская карта: Visa Platinum 7000792289606361, маска: {mask_account_card("Visa Platinum 7000792289606361")}'
)
print(f'Банковская карта: Maestro 7000792289606361, маска: {mask_account_card("Maestro 7000792289606361")}')
print(f'Счет 73654108430135874305, маска: {mask_account_card("Счет 73654108430135874305")}')
print(f'Исходная строка даты-времени: 2024-03-11T02:26:18.671407, Результат форматирования: {get_data(
    "2024-03-11T02:26:18.671407")}')