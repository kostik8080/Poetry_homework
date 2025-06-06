def filter_by_state(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
        Фильтрует список транзакций по состоянию.

        :param transactions: Список словарей с транзакциями
        :param state: Состояние для фильтрации (по умолчанию 'EXECUTED')
        """
    return [transaction for transaction in transactions if transaction.get('state') == state]

def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
        Сортирует список транзакций по дате.

        :param transactions: Список словарей с транзакциями
        :param reverse: Если True (по умолчанию), сортирует по убыванию (новые сначала),
                       если False — по возрастанию (старые сначала)
        :return: Отсортированный список транзакций
        """
    return sorted(
        transactions,
        key=lambda x: x['date'],
        reverse=reverse
    )
