import cv2
import time

# Желаемые размеры (ширина, высота)
TARGET_WIDTH = 1980
TARGET_HEIGHT = 1024


cap = cv2.VideoCapture(1)  # Виртуальная камера OBS
cap.set(cv2.CAP_PROP_FRAME_WIDTH, TARGET_WIDTH)   # Ширина
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, TARGET_HEIGHT)  # Высота


# Переменные для расчёта FPS
prev_time = 0
fps = 0


while True:
    ret, frame = cap.read()
    if not ret:
        print("Ошибка захвата кадра!")
        break

        # Расчёт FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if (current_time - prev_time) != 0 else 0
    prev_time = current_time

    # Вывод FPS на кадр (зелёным цветом)
    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (30, 50),  # Позиция текста (x, y)
        cv2.FONT_HERSHEY_SIMPLEX,
        1,  # Размер шрифта
        (0, 255, 0),  # Цвет (BGR: зелёный)
        2,  # Толщина шрифта
    )

    # Показываем результат
    cv2.imshow("OBS Virtual Camera (Resized)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()