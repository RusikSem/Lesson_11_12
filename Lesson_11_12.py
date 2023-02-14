# for i in 0, 1, 2, 3, 4, 5, 6, 7, 8, 9:
#     print(i)

# for i in range(10):
#     print(i)

# Задание 1
# Пользователь вводит с клавиатуры число.
# Необходимо проверить его на четность и нечетность. Если число
# четное требуется вывести на экран число и надпись Even
# number. Если число нечетное выведите на экран число и
# надпись Odd number.

# Задание 3
# Пользователь вводит с клавиатуры два числа. Нужно
# показать все нечетные числа в указанном диапазоне.
# a = 0
# b = 10
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         print(i)

# Задание 3
# Пользователь вводит с клавиатуры два числа. Нужно
# показать все четные числа в указанном диапазоне.
# a = 0
# b = 10
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         print(i)

# [18:32] Буйлук Андрей
# Задание 4
# Пользователь вводит с клавиатуры два числа.
# Нужно показать все числа в указанном диапазоне в порядке
# убывания.

# a = 4
# b = 9
# while a < b:
#     print(b)
#     b = b - 1

# a = 10
# b = 1
# for i in range(a, b - 1, -1):
#     print(i)


# Задание 5
# Пользователь вводит с клавиатуры два числа. Н
# ужно показать все нечетные числа в указанном диапазоне.
# Если границы диапазона указаны неправильно требуется
# произвести нормализацию границ.
# Например, пользователь ввел 33 и 13,
# требуется нормализация после которой
# начало диапазона станет равно 13, а конец 33.
# a = 33
# b = 13
# if b < a:
#     c = a
#     a = b
#     b = c
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         print(i)

# while True:
#     print('1 raz')
#     break
#
# a = 0
# b = 10
# for i in range(a, b + 1):
#     if i == 5:
#       break
#         print(i)


# Задание 1

# Задание 1
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
# Требуется проанализировать все
# числа в этом диапазоне по следующему правилу: если
# число кратно 7, его надо выводить на экран.
# a = 1
# b = 50
# if a > b:
#     c = a
#     a = b
#     b = c
# while a <= b:
#     a = a + 1
#     if a % 7 == 0:
#         continue
#     print(a)

# Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать сумму чисел в указанном диапазоне, а также
# среднеарифметическое.

# a = 1
# b = 5
# summa = 0
# for i in range(a, b, +1):
#     summa = summa + 1
# print(summa)

# a = 5
# b = 1
# sum = 0
# if a > b:
#     c = a
#     a = b
#     b = c
# for i in range(a, b + 1):
#     sum = sum + a
#     a += 1
#     sr = sum / (b)
# print(sum)
# print(sr)

# a = 2
# b = 9
# summa = 0
# if a > b:
#     c = a
#     a = b
#     b = c
# for i in range(a , b + 1):
#     summa = summa + a
#     a = a + 1
#     average = summa/(b-1)
# print(summa)
# print(average)

# import random
# my_number = 0
# secret_number = random.randint(1, 20)
# while secret_number != my_number:
#     my_number = int(input('Enter your number: '))
#     if secret_number > my_number:
#         print('Your number less than secret number')
#     elif secret_number < my_number:
#         print('Your number greater than secret number')
#     elif secret_number == my_number:
#         print('Your win')

# import random
# money = 0
# while True:
#     tries = int(input('Enter count of tries: '))
#     a = int(input('Enter start of range: '))
#     b = int(input('Enter finish of range: '))
#     my_number = 0
#     secret_number = random.randint(1, 20)
#     while secret_number != my_number and tries >= 0:
#         my_number = int(input('Enter your number: '))
#         if secret_number > my_number:
#             print('Your number less than secret number')
#         elif secret_number < my_number:
#             print('Your number greater than secret number')
#         elif tries < 0:
#             print('Your lose!')
#         elif secret_number == my_number and tries >= 0:
#             print('Your win!')
#     e = str(input('Press [Enter] to continue or Press [Any key] + [Enter] to exit: '))
#     if e:
#         break


import random
player_choice = ''
bot_choice = ''
player_score = 0
bot_score = 0
for i in range(1, 3 + 1):
    print(f'ROUND {i}')
    player_choice = str(input('Enter your choice [r], [p], [s] :  '))
    bot_choice = random.choice('rps')
    print(f'Player choice : {player_choice}\nBot choice : {bot_choice}')
    if player_choice == bot_choice:
        print('Draw round')
    if player_choice == 's':
        if bot_score == 'p':
            print('Player win the round!')
            player_score = player_score + 1
    elif bot_choice == 'r':
        print('Bot win the round!')
        bot_score = bot_score + 1

    elif player_choice == 'p':
        if bot_score == 's':
            print('Bot win the round!')
            player_score = player_score + 1
    elif bot_choice == 'r':
        print('Player win the round!')
        bot_score = bot_score + 1

    elif player_choice == 'r':
        if bot_score == 'p':
            print('Bot win the round!')
            player_score = player_score + 1
        elif bot_choice == 's':
            print('Player win the round!')
            bot_score = bot_score + 1


if player_score == bot_score:
    print('Draw the game')
elif player_score > bot_score:
    print('Player win the game')
elif player_score < bot_score:
    print('Bot win the game')
if i == 3:
    print('With play again!')



