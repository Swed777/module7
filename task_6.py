print('Задача 6. Успеваемость в классе')
print('--------------------------------------------')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.

count_3 = 0
count_4 = 0
count_5 = 0

list_score = int(input('Введите количество учеников в классе: '))
for student in range(1, list_score + 1):
  score = int(input('Введите оценку: '))
  if score == 3:
    count_3 += 1
  elif score == 4:
    count_4 += 1 
  elif score == 5:
    count_5 += 1
#print(count_3, count_4, count_5)
if count_3 > count_4 and count_3 > count_5:
   max = count_3
   for_print = ('ТРИ')
elif count_4 > count_3 and count_4 > count_5:
  max = count_4
  for_print = ('ЧЕТЫРЕ')
elif count_5 > count_3 and count_5 > count_4:
  max = count_5
  for_print = ('ПЯТЬ')
print('Сегодня больше учеников с оценкой: ', for_print)
if count_3 == count_4 or count_3 == count_5 or count_4 == count_5:
  print('** Есть одинаковое количество учеников с оценками **')
print('--------------------------------------------')

  