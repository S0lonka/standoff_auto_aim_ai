from ultralytics import YOLO

# from app.config.config import YOLO_MODEL

def model_check(photo_path: str, model_path: str ="runs/detect/train/weights/best.pt") -> None:
    '''Проверка модели на указанном изображении.

    Args:
        photo_path (str): Путь к изображению для тестирования модели.
        model_path (str): Путь к файлу модели (по умолчанию "runs/detect/train/weights/best.pt").

    Returns:
        None - Отображает фото с результатом.
    '''

    model = YOLO(model_path)

    result = model.predict(photo_path)
    result[0].show()
