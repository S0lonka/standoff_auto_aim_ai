from ultralytics import YOLO

from config import yolo_model



model = YOLO("runs/detect/train/weights/best.pt")

result = model.predict(r"data_set\test\images\enemy_1575_png.rf.7e3087f0179a5337dc0339ffb0103cf9.jpg")
result[0].show()