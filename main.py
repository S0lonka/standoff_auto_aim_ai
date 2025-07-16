from ultralytics import YOLO

import cv2
import time

from app.config.config import *
from app.config.game_config import *

from app.utils.game_funcs.fps import display_fps


def main(model) -> None:
    cap = cv2.VideoCapture(OBS_CAPTURE) # Захватываем виртуальную камеру OBS

    #----Можно изменить размер изображения, НО жертвуя FPS----
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

    #-----FPS-----
    prev_time = 0
    fps = 0

    #---FLAG---
    running = True

    #--MAIN_WHILE--
    while running:

        #---Получаем картинку с виртуальной камеры---
        ret, frame = cap.read()
        if not ret:
            print("Ошибка захвата кадра")
            break


        #---------Получаем переменную для работы с нейросетью---------
        results = model(
            frame,                      # Изображение над которым работаем
            imgsz=640,                  # Размер обработки (меньше = быстрее)
            half=True,                  # Половинная точность (если GPU с CUDA) | +FPS
            device='cuda',              # Явно указываем GPU
            conf=CONFIDENCE_THRESHOLD,  # Порог уверенности (меньше = быстрее, но менее точно)
            verbose=False,              # verbose=False отключает лишний вывод
            # iou=0.45                    # Порог для подавления дубликатов
        )

        annotated_frame = results[0].plot()  # Кадр с нарисованными Боксами




        #----------Расчитываем FPS----------
        current_time = time.time()
        fps = 1 / (current_time - prev_time) if (current_time - prev_time) != 0 else 0
        prev_time = current_time

        #----------Отображаем FPS-----------
        display_fps(annotated_frame, int(fps))



        #-----Отрисовываем окно-----
        cv2.imshow("Yolo + OBS boxs", annotated_frame)

        #-----Обработка завершения программы----- (без этого окно зависнет)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()





if __name__ == "__main__":
    model = YOLO(r"runs\detect\train\weights\best.pt")
    main(model)