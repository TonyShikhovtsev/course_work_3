import pytest
import json
from utils import load_json_from_file, mask_card_number, mask_account_number
from main import print_last_operations

# Тестовые данные для функции mask_card_number
@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "XXXX XXXX XXXX 3456"),
    ("", ""),
    ("1234", "XXXX XXXX XXXX 1234"),
])
def test_mask_card_number(card_number, expected):
    """
    Функция тестирования функции отображения номера карты
    """
    assert mask_card_number(card_number) == expected

@pytest.mark.parametrize("account_number, expected", [
    ("12345678", "**5678"),
    ("", ""),
    ("1234", "**1234"),
])
def test_mask_account_number(account_number, expected):
    """
    Функция тестирования функции вывода номера счета
    """
    assert mask_account_number(account_number) == expected

@pytest.fixture
def example_operations():
    """
    Функция с тестовыми данными
    """
    operations_data = [
        {
            "state": "EXECUTED",
            "date": "2023-07-05T10:50:58.294041",
            "description": "Перевод организации",
            "from": "1234567812345678",
            "to": "9876543210987654",
            "operationAmount": {
                "amount": "82771.72",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            }
        },
    ]
    return operations_data

def test_print_last_operations(capsys, example_operations):
    """
    Функция тестирования функции вывода последних 5 операций
    """
    print_last_operations(example_operations)

    captured = capsys.readouterr()

    assert "05.07.2023 Перевод организации" in captured.out
    assert "XXXX XXXX XXXX 5678 -> XXXX XXXX XXXX 7654" in captured.out
    assert "82771.72 руб." in captured.out
    assert "...\n" not in captured.out


def test_load_json_from_file(tmp_path):
    """
    Функция тестирования функции загрузки файла
    """
    test_data = [{"key": "value"}, {"key": "another_value"}]
    test_file_path = tmp_path / "test_operations.json"
    with open(test_file_path, "w") as file:
        json.dump(test_data, file)

    loaded_data = load_json_from_file(test_file_path)
    assert loaded_data == test_data
