# Папка Yolo 11
- images - изображения для обучения 
    - train - файлы для тренировки модели
    - val - файлы для проверки модели
- labels - файлы с разметкой 
    - train - файлы для тренировки модели
    - val - файлы для проверки модели


## Запуск тренировки YOLO через PowerShell
```
yolo detect train `
   resume=True `
   model="runs\detect\train\weights\last.pt" ` # Либо модель(yolo11m.pt)
   data="data_set\data.yaml" `
   epochs=400 `
   imgsz=640 `
   batch=16 `
   device="cuda" # Видео карта
```