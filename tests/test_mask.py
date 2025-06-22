import pytest
from masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    ("1234567812345678", "1234 56** **** 5678"),
    ("1111222233334444", "1111 22** **** 4444"),
    ("9999888877776666", "9999 88** **** 6666"),
    ("1234 5678 1234 5678", "1234 56** **** 5678"),  # с пробелами
    ("MC 1234567812345678", "1234 56** **** 5678"),   # с префиксом
])
def test_get_mask_card_number_valid(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("invalid_card", [
    "12345678",              # слишком короткий
    "12345678123456781234",  # слишком длинный
    "abcdefghijklmnop",      # не цифры
    "",                      # пустая строка
    None,                    # None
])
def test_get_mask_card_number_invalid(invalid_card):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card)

@pytest.mark.parametrize("account_number, expected", [
    ("12345678901234567890", "**7890"),
    ("98765432109876543210", "**3210"),
    ("00001111222233334444", "**4444"),
])
def test_get_mask_account_valid(account_number, expected):
    assert get_mask_account(account_number) == expected

@pytest.mark.parametrize("invalid_account", [
    "12345678",              # слишком короткий
    "123456789012345678901234567890",  # слишком длинный
    "abcdefghijklmnopqrst",  # не цифры
    "",                      # пустая строка
    None,                    # None
])
def test_get_mask_account_invalid(invalid_account):
    result = get_mask_account(invalid_account)
    assert result == "Номер счета должен содержать только цифры и содержать 20 символов"