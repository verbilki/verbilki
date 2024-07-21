import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_acc_number: str) -> str:
    """
    Функция преобразования банковской карты или счёта вида
    Visa Platinum 7000792289606361
    или Счет 73654108430135874305
    в маскированные строки вида
    Visa Platinum 7000 79** **** 6361
    или Счет **4305
    соответственно.
    """

    # определение позиции первой цифры во входном аргументе card_or_acc_number
    first_digit_pos = 0

    for i, char in enumerate(card_or_acc_number):
        if char.isdigit():
            first_digit_pos = i
            break

    if first_digit_pos == 0:
        exception_msg = (
            "Номер карты должен начинаться с наименования платежной системы,"
            " а номер счёта должен начинаться со слова 'Счет'."
        )
        raise ValueError(exception_msg)

    pattern = r"[\D]"  # регулярное выражение для поиска нецифровых символов
    nondigits = re.findall(pattern, card_or_acc_number[first_digit_pos:])

    if card_or_acc_number[: first_digit_pos - 1] == "Счет":
        if nondigits:
            raise ValueError("Номер счета должен состоять только из цифр.")
        return card_or_acc_number[:first_digit_pos] + get_mask_account(card_or_acc_number[first_digit_pos:])
    else:
        if nondigits:
            raise ValueError("Номер карты должен состоять только из цифр.")
        return card_or_acc_number[:first_digit_pos] + get_mask_card_number(card_or_acc_number[first_digit_pos:])


def get_data(raw_date_str: str) -> str:
    """
    Функция принимает на вход строку вида 'yyyy-MM-ddThh:mm:ss.ssssss'
    и отдает результат в формате 'dd.mm.yyyy'
    """
    if not raw_date_str:
        return ""
    try:
        date_obj = datetime.strptime(raw_date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError(f"Error: time data '{raw_date_str}' does not match format '%Y-%m-%dT%H:%M:%S.%f'")
