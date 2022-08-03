print('Задача 8. Замечательные числа')

#Напишите программу,
# которая находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.

for number in range(10, 100):
  first_figure = number // 10
  second_figure = number % 10
  if number == first_figure * second_figure * 3:
    print(number)