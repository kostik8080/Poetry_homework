import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sample_transactions):
    # Фильтрация выполненных транзакций
    executed = filter_by_state(sample_transactions, "EXECUTED")
    assert len(executed) == 2
    assert all(t["state"] == "EXECUTED" for t in executed)

    # Фильтрация отмененных транзакций
    canceled = filter_by_state(sample_transactions, "CANCELED")
    assert len(canceled) == 1
    assert all(t["state"] == "CANCELED" for t in canceled)

    # Фильтрация несуществующего состояния
    none_state = filter_by_state(sample_transactions, "NON_EXISTENT")
    assert len(none_state) == 0


def test_filter_by_state_empty_input():
    assert filter_by_state([], "EXECUTED") == []


def test_sort_by_date_ascending(sample_transactions):
    sorted_asc = sort_by_date(sample_transactions, reverse=False)
    dates = [t["date"] for t in sorted_asc]
    assert dates == sorted(dates)


def test_sort_by_date_descending(sample_transactions):
    sorted_desc = sort_by_date(sample_transactions, reverse=True)
    dates = [t["date"] for t in sorted_desc]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_empty_input():
    assert sort_by_date([], reverse=True) == []


def test_sort_by_date_missing_key(invalid_transactions):
    # Тест с транзакциями без даты
    with pytest.raises(KeyError):
        sort_by_date(invalid_transactions)