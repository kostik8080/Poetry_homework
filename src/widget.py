from mask import get_mask_card_number, get_mask_account


def mask_account_card(world):
    res = world.split()
    # Если последний элемент - 16 цифр, это карта
    if len(res[-1]) == 16 and res[-1].isdigit():
        name = " ".join(res[:-1])
        return f"{name} {get_mask_card_number(res[-1])}"
    # Если последний элемент - 20 цифр, это счет
    elif len(res[-1]) == 20 and res[-1].isdigit():
        name = " ".join(res[:-1])
        return f"{name} {get_mask_account(res[-1])}"
    return None

print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
print(mask_account_card("Счет 64686473678894779589"))      # Счет **9589