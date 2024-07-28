import json

def format_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    formatted = json.dumps(data, indent=4, ensure_ascii=False)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(formatted)

    print(f"Formatted JSON: {file_path}")

if __name__ == "__main__":
    path = input("Enter JSON file path: ")
    format_json_file(path)
