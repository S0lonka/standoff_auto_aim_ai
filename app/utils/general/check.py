import os

def check_segments_in_labels(labels_dir="labels"):
    """
    Проверяет, какие файлы в папке labels содержат сегменты (полигоны).
    Выводит имена файлов, где есть разметка типа segments.
    """
    segment_files = []

    for filename in os.listdir(labels_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(labels_dir, filename)
            with open(filepath, "r") as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) > 5:  # Если больше 5 чисел → это полигон
                        segment_files.append(filename)
                        break  # Достаточно одной строки с полигоном

    if segment_files:
        print("Файлы с сегментами (полигонами):")
        for file in segment_files:
            print(file)
    else:
        print("Файлов с сегментами не найдено.")

# Пример вызова
check_segments_in_labels(r"C:\Programs\python\standoff_AI\AI\data_set\valid\labels")