"""Игра угадай число"""

import numpy as np

min = 1
max = 100

number = np.random.randint(min, max + 1)  #программа загадывает число
count = 0  #подсчет количества попыток на отгадывание числа

while True:
    count += 1
    mid = int((min + max)/2)
    
    if mid > number:
        max = mid
        
    elif mid < number:
        min = mid
            
    else:
        print(f"Робот угадал число! Это число = {number}, за {count} попыток.")
        break  #конец игры и выход из цикла