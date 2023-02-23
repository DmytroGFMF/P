import random

numbers = [random.randint(-10, 10) for i in range(10)]
min = min(numbers)
max = max(numbers)
a = len([num for num in numbers if num < 0])
print("Список чисел:", numbers)
print("Мінімальний елемент:", min)
print("Максимальний елемент:", max)
print("Кількість від'ємних елементів:", a)

