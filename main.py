from ultralytics import YOLO

import cv2

from app.config.config import *
from app.config.game_config import *

from app.utils.model.model_train import train_model, resume_train_model


def main(model) -> None:
    cap = cv2.VideoCapture(OBS_CAPTURE) # Захватываем виртуальную камеру OBS

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
            half=True,                  # Половинная точность (если GPU с CUDA)
            device='cuda',              # Явно указываем GPU
            conf=CONFIDENCE_THRESHOLD,  # Порог уверенности (меньше = быстрее, но менее точно)
            verbose=False               # verbose=False отключает лишний вывод
        )






if __name__ == "__main__":
    model = YOLO(r"runs\detect\train\weights\best.pt")
    main(model)