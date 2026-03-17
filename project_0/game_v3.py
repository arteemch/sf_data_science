import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Угадывает число бинарным поиском
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
            
    count = 0
    low, high = 1, 100    # Устанавливаем границы динамического диапазона, который будет сужаться с каждой новой попыткой 

    
    while True:
        count += 1
        predict = (low + high) // 2  # Делим диапазон пополам
        
        if predict == number:
            return count
        elif predict < number:
            low = predict + 1  # Ищем в верхней половине
        else:
            high = predict - 1  # Ищем в нижней половине
    

game_core_v3(67)