import pytest
from datetime import datetime

@pytest.fixture
def sample_transactions():
    return [
        {
            "state": "EXECUTED",
            "date": "2023-05-15T14:30:00.000000",
            "description": "Payment",
            "from": "Visa 1234567812345678",
            "to": "Счет 12345678901234567890"
        },
        {
            "state": "PENDING",
            "date": "2023-05-10T10:15:00.000000",
            "description": "Transfer",
            "from": "MasterCard 8765432187654321",
            "to": "Счет 98765432109876543210"
        },
        {
            "state": "EXECUTED",
            "date": "2023-05-20T18:45:00.000000",
            "description": "Withdrawal",
            "from": "Maestro 1111222233334444",
            "to": "Счет 11112222333344445555"
        },
        {
            "state": "CANCELED",
            "date": "2023-04-30T09:00:00.000000",
            "description": "Deposit",
            "to": "Счет 55556666777788889999"
        }
    ]


@pytest.fixture
def invalid_transactions():
    return [
        {"state": "EXECUTED", "date": "invalid-date"},
        {"state": "PENDING", "description": "No date"},
        {"date": "2023-01-01T00:00:00.000000"},
        {}
    ]
