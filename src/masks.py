def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX,где X — это цифра номера.
    """
    masked_card_number = card_number[:6] + '******' + card_number[-4:]
    return ' '.join(masked_card_number[i:i+4] for i in range(0, len(masked_card_number), 4))

def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX,
    где X — это цифра номера.
    """
    return '**' + account_number[-4:]
