import re


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX,где X — это цифра номера.
    :rtype: object
    """
    if not card_number:
        return ""

    pattern = r"[^0-9]"  # регулярное выражение для поиска нецифровых символов
    if re.findall(pattern, card_number):
        raise ValueError("Номер карты должен состоять только из цифр.")

    if len(card_number) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр.")

    masked_card_number = card_number[:6] + "******" + card_number[-4:]
    return " ".join(masked_card_number[i : i + 4] for i in range(0, len(masked_card_number), 4))


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX,
    где X — это цифра номера.
    """
    if not account_number:
        return ""
    return "**" + account_number[-4:]
