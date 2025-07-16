import cv2

def display_fps(frame, fps: int):
    '''Функция отрисовки FPS в новом окне
    Args:
        frame       : Изображение на котором отобразить Fps.
        fps   (int) : Число fps
    '''
    cv2.putText(
        frame,                       # Изображение(куда)
        f"FPS: {int(fps)}",          # Текст
        (30, 50),                    # Позиция
        cv2.FONT_HERSHEY_SIMPLEX,    # Стиль
        2,                           # Размер
        (0, 255, 0),                 # Цвет
        2                            # Толщина
    )