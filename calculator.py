def ADD(x,y):  # Ошибка 1: нарушение стиля (большие буквы)
    result = x+y  # Ошибка 2: нет пробелов вокруг +
    return result

def subtract(a, b):
    r = a - b  # Ошибка 3: непонятное имя переменной
    return r

def multiply(a, b):
    c = a * b  # Ошибка 4: избыточная переменная
    return c

def divide(a, b):
    return a / b  # Ошибка 5: нет проверки на ноль

def main():
    num1 = input("Введите число: ")  # Ошибка 6: нет преобразования в float
    # Ошибка 7: нет обработки нечислового ввода
    result = ADD(num1, 5)
    
    if result > 100:  # Ошибка 8: магическое число
        print("Много")
        
