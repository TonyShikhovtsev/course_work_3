import os
import json

def load_json_from_file(path):
    """
    Загрузка данных из файлов json
    """
    if not os.path.exists(path):
        return []

    with open(path, 'r') as file:
        data = json.load(file)
    return data

def mask_card_number(card_number):
    """
    Функция вывода номера карты (часть скрыта)
    """
    masked_number = f'XXXX XXXX XXXX {card_number[-4:]}' if card_number else ""
    return masked_number

def mask_account_number(account_number):
    """
    Функция отображения 4 последних цифр счета
    """
    masked_number = f'**{account_number[-4:]}' if account_number else ""
    return masked_number



