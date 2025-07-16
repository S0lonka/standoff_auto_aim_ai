import pygetwindow as gw

from app.config.game_config import ENEMY

def main_window_cords(box, frame):
    '''Функция перевода кординат из окна с ИИ в основное окно'''
    # Получаем координаты bounding box'а в формате [x1, y1, x2, y2]
    x1, y1, x2, y2 = box.xyxy[0].tolist()

    # Вычисляем центр объекта
    center_x = int((x1 + x2) / 2)
    center_y = int((y1 + y2) / 2)
                

    # Найти окно игры по названию (например, "Counter-Strike 2")
    game_window = gw.getWindowsWithTitle("BlueStacks App Player")[0]  # Если окно найдено

    # Получить его координаты (left, top, width, height)
    game_x, game_y, game_width, game_height = (
        game_window.left,
        game_window.top,
        game_window.width,
        game_window.height,
    )


    scale_x = game_width / frame.shape[1]  # frame.shape[1] = ширина кадра OpenCV
    scale_y = game_height / frame.shape[0]  # frame.shape[0] = высота кадра OpenCV

    # Итоговые координаты в игровом окне
    game_center_x = game_x + (center_x * scale_x)
    game_center_y = game_y + (center_y * scale_y)
    return game_center_x, game_center_y






def auto_aim(results, model, frame):
    for box in results[0].boxes:
        class_id = int(box.cls)             # ID класса объектаэ
        class_name = model.names[class_id]  # Имя Класса объекта


        # Если есть голова врага, наводим на неё, иначе на тело врага
        if class_name == f"{ENEMY}_h":
            game_center_x, game_center_y = main_window_cords(box, frame)
        elif class_name == ENEMY:
            game_center_x, game_center_y = main_window_cords(box, frame)
