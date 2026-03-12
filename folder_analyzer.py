import os

def analyze_folder(path):
    total_files = 0
    total_size = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            total_files += 1
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
        

    size_mb = total_size / (1024 * 1024)

    print("\nFolder Analysis Result")
    print("----------------------")
    print(f"Folder: {path}")
    print(f"Total files: {total_files}")
    print(f"Total size: {size_mb:.2f} MB")


folder = input("Enter folder path to analyze: ")
analyze_folder(folder)