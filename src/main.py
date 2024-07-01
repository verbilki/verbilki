from src.masks import get_mask_account, get_mask_card_number, mask_account_card

# print(
#     f'Банковская карта: 1234567890123456, маска: {get_mask_card_number("1234567890123456")}'
# )
# print(
#     f'Банковский счёт: 43210810000000012345, маска: {get_mask_account("43210810000000012345")}'
# )

print(f'Банковская карта: Visa Platinum 7000 7922 8960 6361, маска: {mask_account_card("Visa Platinum 7000 7922 8960 6361")}')
print(f'Счет 73654108430135874305, маска: {mask_account_card("Счет 73654108430135874305")}')
