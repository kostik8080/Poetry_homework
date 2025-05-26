def get_mask_card_number(card_number: str) -> str:
    """Функция, получает строку ввиде целого числа из 16 символов"""
    # Извлекаем все цифры из входной строки
    digits: str = "".join(filter(lambda c: c.isdigit(), str(card_number)))

    # Проверяем, что номер карты содержит 16 цифр
    if len(digits) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Разбиваем цифры на группы по 4
    groups = [digits[i : i + 4] for i in range(0, 16, 4)]

    # Маскируем группы
    masked_groups = [groups[0], groups[1][:2] + "**", "****", groups[3]]

    # Объединяем группы в итоговую строку с пробелами
    return " ".join(masked_groups)


def get_mask_account(account_number: str) -> str:
    """Функция принимает строку из цифр и возвращает последние 4 цифры"""
    if account_number.isdigit() and len(account_number) == 20:
        return f"**{account_number[-4:]}"
    return "Номер счета должен содержать только цифры и содержать 20 символов"
