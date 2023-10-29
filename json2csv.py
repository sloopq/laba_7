import json
import csv
import sys
import os

def json_to_csv(json_filename):
    # Проверяем, существует ли JSON-файл
    if not os.path.exists(json_filename):
        print(f"JSON файл {json_filename} не найден.")
        return

    # Определяем имя CSV-файла на основе имени JSON-файла
    base_filename = os.path.splitext(json_filename)[0]
    csv_filename = f"{base_filename}.csv"

    # Открываем JSON-файл для чтения
    with open(json_filename, 'r') as json_file:
        data = json.load(json_file)

    # Открываем CSV-файл для записи
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Записываем заголовки (первую строку) в CSV
        csv_writer.writerow(data.keys())

        # Записываем данные в CSV
        csv_writer.writerow(data.values())

    print(f"Файл {csv_filename} успешно создан.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python json2csv.py example.json")
    else:
        json_filename = sys.argv[1]
        json_to_csv(json_filename)
