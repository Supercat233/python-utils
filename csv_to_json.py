import csv
import json

def convert_csv_to_json(csv_path, json_path):
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, indent=4, ensure_ascii=False)

    print(f"Converted {csv_path} → {json_path}")

if __name__ == "__main__":
    csv_path = input("Enter CSV file path: ")
    json_path = input("Enter output JSON file name: ")
    convert_csv_to_json(csv_path, json_path)
