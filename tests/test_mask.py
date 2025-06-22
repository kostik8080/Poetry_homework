import pytest

from src.mask import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("9999888877776666", "9999 88** **** 6666"),
        ("1234 5678 1234 5678", "1234 56** **** 5678"),  # с пробелами
        ("MC 1234567812345678", "1234 56** **** 5678"),  # с префиксом
    ],
)
def test_get_mask_card_number_valid(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "invalid_card",
    [
        "12345678",  # слишком короткий
        "12345678123456781234",  # слишком длинный
        "abcdefghijklmnop",  # не цифры
        "",  # пустая строка
        None,  # None
    ],
)
def test_get_mask_card_number_invalid(invalid_card):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card)


@pytest.mark.parametrize(
    "invalid_account, expected_message",
    [
        ("12345678", "Номер счета должен содержать только цифры и содержать 20 символов"),  # слишком короткий
        (
            "123456789012345678901234567890",
            "Номер счета должен содержать только цифры и содержать 20 символов",
        ),  # слишком длинный
        ("abcdefghijklmnopqrst", "Номер счета должен содержать только цифры и содержать 20 символов"),  # не цифры
        ("", "Номер счета должен содержать только цифры и содержать 20 символов"),  # пустая строка
        (None, "Номер счета должен содержать только цифры и содержать 20 символов"),  # None
        (12345678901234567890, "Номер счета должен быть строкой"),  # число вместо строки
        ({"account": "12345678901234567890"}, "Номер счета должен быть строкой"),  # словарь
    ],
)
def test_get_mask_account_invalid(invalid_account, expected_message):
    result = get_mask_account(invalid_account)
    assert result == expected_message


@pytest.mark.parametrize(
    "invalid_account",
    [
        "12345678",  # слишком короткий
        "123456789012345678901234567890",  # слишком длинный
        "abcdefghijklmnopqrst",  # не цифры
        "",  # пустая строка
        None,  # None
    ],
)
def test_get_mask_account_valid(invalid_account):
    result = get_mask_account(invalid_account)
    assert result == "Номер счета должен содержать только цифры и содержать 20 символов"
