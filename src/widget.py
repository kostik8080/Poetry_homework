from datetime import datetime

from .mask import get_mask_account, get_mask_card_number


def mask_account_card(world: str) -> str:
    """Функция, принимает строку счет или карту и выводит замаскированный счет или карту в формате строки"""
    if not world or world.isspace():
        return "Номер карты или номер счета должен содержать целые числа"

    res = world.split()

    # Если нет частей после split или последняя часть не содержит цифр
    if not res or not any(c.isdigit() for c in res[-1]):
        return "Номер карты или номер счета должен содержать целые числа"

    # Если последний элемент - 16 цифр, это карта
    if len(res[-1]) == 16 and res[-1].isdigit():
        name = " ".join(res[:-1])
        return f"{name} {get_mask_card_number(res[-1])}"
    # Если последний элемент - 20 цифр, это счет
    elif len(res[-1]) == 20 and res[-1].isdigit():
        name = " ".join(res[:-1])
        return f"{name} {get_mask_account(res[-1])}"

    return "Номер карты или номер счета должен содержать целые числа"


def get_date(date_str: str) -> str:
    """Функция принимает ввиде строки дату и время и выводи в виде читаемого формата"""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Некорректный формат даты"
