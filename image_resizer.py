from PIL import Image
import os

def resize_images(folder, width):
    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(folder, filename)
            img = Image.open(path)
            ratio = width / img.width
            new_height = int(img.height * ratio)
            resized = img.resize((width, new_height))
            resized.save(os.path.join(folder, f"resized_{filename}"))
            print(f"Resized {filename}")

if __name__ == "__main__":
    folder_path = input("Enter folder path: ")
    width = int(input("Enter new width (px): "))
    resize_images(folder_path, width)
