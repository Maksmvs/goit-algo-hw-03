import os
import shutil
import argparse

def copy_files(src_dir, dest_dir):
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                
                _, extension = os.path.splitext(file)
                
                sub_dir = os.path.join(dest_dir, extension[1:])
                if not os.path.exists(sub_dir):
                    os.makedirs(sub_dir)

                shutil.copy2(file_path, os.path.join(sub_dir, file))
        
        print("Копіювання завершено.")
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")

def main():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів.")
    parser.add_argument("src_dir", help="Шлях до вихідної директорії")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням - dist)")

    args = parser.parse_args()

    copy_files(args.src_dir, args.dest_dir)

if __name__ == "__main__":
    main()
