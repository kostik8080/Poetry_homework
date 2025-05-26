from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
