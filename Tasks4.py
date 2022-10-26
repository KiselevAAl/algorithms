"""
Сложность (log n)
"""

def sumBase():
    n = int(input('Введите число n: '))
    k = int(input('Введите число k: '))
    count = 0
    while n != 0:   # пока число n не равно нулю
        count += n % k       # к счетчеку прибавляем остаток от деления
        n = n // k      # n равно целой части от деления n на k
    return count          # возвращаем результата

print(sumBase())


