import cv2
import numpy


def display_fps(frame: numpy.ndarray, fps: int):
    '''Функция отрисовки FPS в новом окне
    Args:
        frame (ndarray) : Изображение на котором отобразить Fps.
        fps   (int)     : Число fps
    '''
    cv2.putText(
        frame,                       # Изображение(куда)
        f"{int(fps)}",               # Текст
        (20, 50),                    # Позиция
        cv2.FONT_HERSHEY_SIMPLEX,    # Стиль
        1.5,                           # Размер
        (0, 255, 0),                 # Цвет
        2                            # Толщина
    )