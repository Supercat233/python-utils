import os

def rename_files():
    files = os.listdir()
    for i, filename in enumerate(files):
        if filename.endswith(".jpg"):
            new_name = f"image_{i+1}.jpg"
            os.rename(filename, new_name)
            print(f"Renamed {filename} → {new_name}")

if __name__ == "__main__":
    rename_files()
