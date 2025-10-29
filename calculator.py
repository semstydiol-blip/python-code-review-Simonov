#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Простой калькулятор на Python
Выполнил: [Твое ФИО], группа [Твоя группа]
"""

def add(a, b):
    """Возвращает сумму двух чисел"""
    return a + b

def subtract(a, b):
    """Возвращает разность двух чисел"""
    return a - b

def multiply(a, b):
    """Возвращает произведение двух чисел"""
    return a * b

def divide(a, b):
    """
    Возвращает результат деления a на b
    Проверяет деление на ноль
    """
    if b == 0:
        raise ValueError("Ошибка: Деление на ноль невозможно!")
    return a / b

def main():
    """Основная функция с консольным интерфейсом"""
    print("🐍 Простой калькулятор")
    print("=" * 25)
    
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Выберите операцию (+, -, *, /): ").strip()
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("❌ Неизвестная операция!")
            return
        
        print(f"✅ Результат: {result}")
        
    except ValueError as e:
        print(f"❌ Ошибка ввода: {e}")
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
