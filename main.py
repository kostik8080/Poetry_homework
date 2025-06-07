from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date

data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

if __name__ == "__main__":
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))

    # Получить выполненные транзакции
    executed = filter_by_state(data)
    print(executed)

    # Получить отмененные транзакции
    canceled = filter_by_state(data, 'CANCELED')
    print(canceled)

    # Сортировка по убыванию (новые сначала)
    sorted_desc = sort_by_date(data)
    print(sorted_desc)

    # Сортировка по возрастанию (старые сначала)
    sorted_asc = sort_by_date(data, reverse=False)
    print(sorted_asc)
