def filter_by_state(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
        Фильтрует список транзакций по состоянию.

        :param transactions: Список словарей с транзакциями
        :param state: Состояние для фильтрации (по умолчанию 'EXECUTED')
        """
    return [transaction for transaction in transactions if transaction.get('state') == state]

