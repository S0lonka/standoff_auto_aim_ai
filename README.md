## Запуск тренировки YOLO через PowerShell
```
yolo detect train `
   resume=True `
   model="runs\detect\train\weights\last.pt" ` # Либо модель(yolo11m.pt)
   data="AI\data_set\data.yaml" `
   epochs=400 `
   imgsz=640 `
   batch=8 `
   device="cuda" # Видео карта
```