print('Задача 7. Отрезок')
print('-------------------')
# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
count_number = 0
summ_3 = 0

for number in range(a,b):
  if number % 3 == 0:
    summ_3 += number
    count_number += 1  
print('Среднее арифметическое чисел, кратных 3 =', summ_3 / count_number)
print('-------------------')