from ultralytics import YOLO

from app.config.config import *

# ! ЗАПУСКАТЬ ЧЕРЕЗ КОНСОЛЬ - Python НЕ ВИДИТ Видео карту

def train_model(data: str = "AI/data_set/data.yaml",
                epochs: int = 400,
                batch: int = 8,
                device: str = "cuda",
                model_path: str = YOLO_MODEL_PATH
                ) -> None:
    '''Обучает YOLO-модель на указанных данных.

    Args:
        - data       (str, optional): Путь к YAML-файлу с конфигурацией данных.     По умолчанию: "AI/data_set/data.yaml".
        - epochs     (int, optional): Количество эпох обучения.                     По умолчанию: 400.
        - batch      (int, optional): Размер пакета (batch size).                   По умолчанию: 8.
        - device     (str, optional): Устройство для обучения ("cuda" или "cpu").   По умолчанию: "cuda".
        - model_path (str, optional): Путь к файлу модели (.pt).                    По умолчанию: YOLO_MODEL_PATH (глобальная константа).

    Returns:
        None: Функция не возвращает значений, но сохраняет обученную модель на диск.

    Examples:
        >>> train_model()                      # Обучение с параметрами по умолчанию
        >>> train_model(batch=16, epochs=100)  # Кастомные параметры
    '''
    
    model = YOLO(model_path).to("cuda")

    model.train(
        data = data,
        epochs=epochs,
        batch=batch,        # Уменьшить, если не хватает памяти GPU
        device=device,
        imgsz=640,
        project="AI/runs/",
        name=f"standoff_{YOLO_MODEL}_V"
    )



def resume_train_model(model_path: str,
                        data: str = "AI/data_set/data.yaml",
                        epochs: int = 400,
                        batch: int = 8,
                        device: str = "cuda",
                        ) -> None:
    '''Продолжает(возобновляет) обучение YOLO-модели на указанных данных.

    Args:
        - model_path (str)           : Путь к последним весам модели (last.pt).      По умолчанию: 
        - data       (str, optional) : Путь к YAML-файлу с конфигурацией данных.     По умолчанию: "AI/data_set/data.yaml".
        - epochs     (int, optional) : Количество эпох обучения.                     По умолчанию: 400.
        - batch      (int, optional) : Размер пакета (batch size).                   По умолчанию: 8.
        - device     (str, optional) : Устройство для обучения ("cuda" или "cpu").   По умолчанию: "cuda".

    Returns:
        None: Функция не возвращает значений, но сохраняет обученную модель на диск.

    Examples:
        >>> resume_train_model("AI/runs/standoff_yolo11m_V")                        # Обучение с параметрами по умолчанию
        >>> resume_train_model("AI/runs/standoff_yolo11m_V", batch=16, epochs=100)  # Кастомные параметры
    '''

    model = YOLO(model_path).to("cuda")

    model.train(
        data = data,
        epochs=epochs,
        batch=batch,        # Уменьшить, если не хватает памяти GPU
        device=device,
        imgsz=640,
        project="AI/runs/"
    )