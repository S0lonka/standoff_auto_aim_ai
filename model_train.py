from ultralytics import YOLO

from config import yolo_model


model = YOLO(f"yolo_model\\{yolo_model}")

model.train(
    data = "data_set_config.yaml",
    epochs=400,
    device="cuda",
    name=f"{yolo_model}_train"
)