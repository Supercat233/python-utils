import os
import shutil
from datetime import datetime

def sync_folders(source, destination):
    print(f"🔄 Syncing from {source} → {destination}")
    for root, dirs, files in os.walk(source):
        relative_path = os.path.relpath(root, source)
        dest_path = os.path.join(destination, relative_path)

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dest_path, file)

            if not os.path.exists(dst_file) or os.path.getmtime(src_file) > os.path.getmtime(dst_file):
                shutil.copy2(src_file, dst_file)
                print(f"📁 Copied: {src_file} → {dst_file}")

    print("✅ Sync completed!")

if __name__ == "__main__":
    src = input("Enter source folder path: ")
    dst = input("Enter destination folder path: ")
    sync_folders(src, dst)
