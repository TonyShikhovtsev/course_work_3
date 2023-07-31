from utils import print_last_operations,load_json_from_file, mask_card_number, mask_account_number

def print_last_operations(operations):
    """
    Выводит на экран список из 5 последних выполненных операций.
    """
    executed_operations = [x for x in operations if "state" in x and x["state"] == "EXECUTED"]
    sorted_operations = sorted(executed_operations, key=lambda op: op["date"], reverse=True)

    for operation in sorted_operations[:5]:
        date = operation["date"][:10]  # Получаем только дату (без времени)
        description = operation["description"]
        from_account = mask_account_number(operation.get("from", ""))
        to_account = mask_account_number(operation["to"])
        amount = float(operation["operationAmount"]["amount"])
        currency = operation["operationAmount"]["currency"]["name"]
        print("Информация о 5 последних переводах:")
        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"{amount:.2f} {currency}")
        print()

if __name__ == "__main__":
    operations_data = load_json_from_file("operations.json")
    print_last_operations(operations_data)