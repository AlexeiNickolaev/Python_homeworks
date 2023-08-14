# Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


fibonacci = fibonacci_generator(20)
for number in fibonacci:
    print(number)
