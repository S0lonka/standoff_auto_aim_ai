from ultralytics import YOLO

from app.config.config import *

# ! ЗАПУСКАТЬ ЧЕРЕЗ КОНСОЛЬ - Python НЕ ВИДИТ Видео карту

def train_model() -> None:
    model = YOLO(YOLO_MODEL_PATH).to("cuda")

    results = model.train(
        data = "data_set_config.yaml",
        epochs=400,
        imgsz=640,
        batch=16,        # Можно уменьшить, если не хватает памяти GPU
        device="cuda",
        # name=f"{yolo_model}_train"
    )

    results = model.predict("data_set\\test\\images\\enemy_148_png.rf.6e716582bc98c8e4056deadf89a4c79f.jpg", conf=0.5)
    results[0].show()  # Показать результат