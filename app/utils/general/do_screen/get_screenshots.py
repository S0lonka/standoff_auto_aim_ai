import pyautogui
import time
import os
import keyboard

folder = "app\\utils\\general\\do_screen\\enemy_screenshots"
counter_file = "app\\utils\\general\\do_screen\\counter.txt"
interval = 4  # в секундах

# Читаем счётчик из файла
if os.path.exists(counter_file):
    with open(counter_file, "r") as f:
        try:
            counter = int(f.read())
        except:
            counter = 0
else:
    counter = 0

# Создаём папку, если её нет
if not os.path.exists(folder):
    os.makedirs(folder)

print("Скрипт запущен! Нажми Ctrl+C чтобы остановить.")

try:
    while True:
        screenshot = pyautogui.screenshot()
        filename = os.path.join(folder, f"enemy_{counter}.png")
        screenshot.save(filename)
        print(f"Сохранено: {filename}")

        # Сохраняем текущий счётчик в файл
        with open(counter_file, "w") as f:
            f.write(str(counter))

        counter += 1
        time.sleep(interval)


except KeyboardInterrupt:
    # Увеличиваем счётчик на 1 перед выходом
    with open(counter_file, "w") as f:
        f.write(str(counter))
    print(f"Скрипт остановлен. Счёт увеличен на 1: следующий файл будет enemy_{counter}.png")