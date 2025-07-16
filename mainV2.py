from threading import Thread
import queue
from ultralytics import YOLO
import cv2
import time
import asyncio

from app.config.config import *
from app.config.game_config import *

from app.utils.game_funcs.fps import display_fps
from app.utils.game_funcs.aim import auto_aim
from app.utils.game_funcs.camera_buffer import CameraBuffer


async def main(model):
    cam = CameraBuffer()
    prev_time = 0

    try:
        while True:
            frame = cam.read()  # Блокирующее чтение из очереди

            # Обработка в основном потоке (или можно вынести в отдельный)
            results = model(
                frame,
                imgsz=640,
                half=True,
                device='cuda',
                conf=CONFIDENCE_THRESHOLD,
                verbose=False
            )
            annotated_frame = results[0].plot()

            # FPS
            current_time = time.time()
            fps = 1 / (current_time - prev_time) if (current_time - prev_time) != 0 else 0
            prev_time = current_time

            display_fps(annotated_frame, int(fps))

            auto_aim(results, model, annotated_frame)

            cv2.imshow("Yolo + OBS", annotated_frame)
            if cv2.waitKey(1) == ord('q'):
                break

    finally:
        cam.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    model = YOLO(r"runs\detect\train\weights\best.pt")
    asyncio.run(main(model))