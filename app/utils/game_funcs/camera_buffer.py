import cv2
from threading import Thread
import queue

from app.config.config import *
from app.config.game_config import *


class CameraBuffer:
    def __init__(self, src=OBS_CAPTURE, maxsize=2):
        """Инициализация буферизированного захвата кадров с камеры.
        
        Args:
            src: Источник видеопотока (по умолчанию OBS_CAPTURE)
            maxsize: Максимальный размер очереди кадров (для предотвращения переполнения памяти)
        """
     
        self.cap = cv2.VideoCapture(src)            # Инициализация захвата видео
        self.queue = queue.Queue(maxsize=maxsize)   # Очередь для хранения кадров (потокобезопасная)
        self.running = True                         # Флаг для управления потоком захвата

        # Создание и запуск потока для чтения кадров
        self.thread = Thread(target=self._update, daemon=True)# daemon=True - поток завершится при завершении главного потока
        self.thread.start()

    def _update(self):
        """Внутренний метод потока для непрерывного чтения кадров с камеры."""
        
        while self.running:
            # Чтение кадра
            ret, frame = self.cap.read()
            if not ret:
                break  # Выход при ошибке чтения
            
            # Добавление кадра в очередь, если есть место
            if not self.queue.full():
                self.queue.put(frame)

    def read(self):
        """Получение последнего кадра из очереди.
        
        Returns:
            Кадр в формате numpy.ndarray
        """
        # Блокирующее получение кадра из очереди
        return self.queue.get()

    def stop(self):
        """Безопасное завершение работы: останавливает поток и освобождает ресурсы."""

        self.running = False   # Установка флага остановки
        self.thread.join()     # Ожидание завершения потока
        self.cap.release()     # Освобождение ресурсов видеозахвата