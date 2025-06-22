import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("input_str, expected", [
    ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444"),
    ("МИР 9999888877776666", "МИР 9999 88** **** 6666"),
])
def test_mask_account_card_valid(input_str, expected):
    assert mask_account_card(input_str) == expected

@pytest.mark.parametrize("invalid_input", [
    "Invalid 123",           # неверная длина
    "Card abcdefghijklmnop", # не цифры
    "",                      # пустая строка
    "Just text",             # нет номера
    None,                    # None
])
def test_mask_account_card_invalid(invalid_input):
    assert mask_account_card(invalid_input) == "Номер карты или номер счета должен содержать целые числа"

@pytest.mark.parametrize("date_str, expected", [
    ("2023-05-15T14:30:00.000000", "15.05.2023"),
    ("2022-12-31T23:59:59.999999", "31.12.2022"),
    ("2000-01-01T00:00:00.000000", "01.01.2000"),
])
def test_get_date_valid(date_str, expected):
    assert get_date(date_str) == expected

@pytest.mark.parametrize("invalid_date", [
    "2023-05-15",            # неполный формат
    "invalid-date",          # некорректная дата
    "",                      # пустая строка
    None,                    # None
])
def test_get_date_invalid(invalid_date):
    assert get_date(invalid_date) == "Некорректный формат даты"