import torch
def gpu_test() -> bool:
    '''Функция проверки, что тренировку можно запустить на видеокарте
    Results: 
        Bool: если pytorch может использовать видео карту
    '''
    return torch.cuda.is_available()