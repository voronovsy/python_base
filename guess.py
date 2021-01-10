# Это игра по угадыванию чисел
import random # Импортируем модуль random

guessesTaken = 0 # Приваеваем переменной значение = 0

print('Привет! Как тебя зовут?') # Выводим на экран строку ('')
myName = input() # Получаем от пользователя информацию и приваеваем ее переменно myName

number = random.randint(1, 10) # Приваеваем переменной number = случайное значение(число) от 1 до 20
print('Что ж, ' + myName + ', я загадываю число от 1 до 10. На все это, ' + myName + ', у тебя есть 3 попытки. Удачи!') # Выводим на экран имя пользователя и условия игры

for guessesTaken in range(3): # Запускаем цикл for
    print('Попробуй угадать.') # Четыре пробела перед именем функции print
    guess = input() # Получаем число от игрока
    guess = int(guess) # Приводим результат в целое число с помощью функции int()?

    if guess < number:
        print('Твое число слишком маленькое.')
    
    if guess > number:
        print('Твое число слишком большое.')

    if guess == number: # если число угадано то цикл завершается
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Отлично, ' + myName + '! Ты справился за ' + guessesTaken + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Я загадала число ' + number + '.')