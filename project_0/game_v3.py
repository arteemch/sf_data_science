import numpy as np

def game_core_v3(number: int = None) -> int:
    """
    Угадывает число бинарным поиском
    Args:
        number (int, optional): Загаданное число. Defaults to None. Если число не задается, оно выбирается случайным образом

    Returns:
        int: Число попыток
    """
    if number is None:
        number = np.random.randint(1,101)        
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
    
    

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за: {score} попыток")
    
    
        
print(f'Количество попыток: {game_core_v3()}')
score_game(game_core_v3)



