def count_text_info(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)

    print(f"Lines: {num_lines}")
    print(f"Words: {num_words}")
    print(f"Characters: {num_chars}")

if __name__ == "__main__":
    path = input("Enter file path: ")
    count_text_info(path)
