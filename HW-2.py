# #1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:
# # - 6782 -> 23
# # - 0,56 -> 11
print('Задача 1:')
x = input('Введите число: ')
def summa(x):                            
    if float(x) < 0:                            
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number
print(f'Сумма чисел равна {summa(x)}')
print()
# #2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# # Пример:
# # # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
print('Задача 2:')
N = int(input('N = '))
f = 1
for i in range(N):
    i = i + 1
    f = i * f    
    print(f, end = " ")

print()

# #3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# # Пример:
# # - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print('Задача 3:')
n = int(input('n = ')) 
def sequence(n):
    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]           
print(sequence(n))
print(round(sum(sequence(n))))
# n = int(input('n = '))
# lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
# print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')
print()

#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
print('Задача 4:')

from random import randint

with open('file.txt', 'w') as data:
    data.write('0\n')
    data.write('1\n')
    data.write('5\n')
    data.write('8\n')
    data.write('10\n')

def get_numbers(n):
    return [randint(-n/2, n) for i in range(-n, n + 1)]

def get_data_from_file(path):
    data = open(path, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist

def get_mult(numbers, datalist):
    mult = 1
    for i in datalist:
        mult *= numbers[i]
    return mult

path = 'file.txt'
n = 10 
datalist = get_data_from_file(path)
numbers = get_numbers(n)

print(numbers)
print(datalist)
print(get_mult(numbers, datalist))
print()

#5. Реализуйте алгоритм перемешивания списка.
print('Задача 5:')
import random
test_list = [1, 4, 5, 6, 3]
print ("Первоначальный список: " + str(test_list))
for i in range(len(test_list)-1, 0, -1):
    j = random.randint(0, i + 1)
    test_list[i], test_list[j] = test_list[j], test_list[i]
print ("Перемешанный список:   " +  str(test_list))
print()