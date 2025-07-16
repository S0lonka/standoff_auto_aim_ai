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


Поднял производительность используя

results = model(frame, 
   imgsz=640,    #Размер обработки (меньше = быстрее)
   half=True,    # Половинная точность (если GPU с CUDA)
   device='cuda',  # Явно указываем GPU
   conf=0.5, # Порог уверенности (меньше = быстрее, но менее точно)
   verbose=False    # verbose=False отключает лишний вывод
   )