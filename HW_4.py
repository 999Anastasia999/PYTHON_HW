# # 1 Задача: Вычислить число c заданной точностью d
# # Пример:
# # - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
print('Задача 1:')
from math import pi
d =  int(input("Введите число для заданной точности числа Пи:\n"))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')
print()

# print('Задача 1:')
# def calc_pi(eps=1.0e-5):
#     s=0
#     d=1
#     sgn=1
#     while True:
#         a=4/d
#         s=s+sgn*a
#         if a<eps:
#             return s
#         sgn=-sgn
#         d=d+2
# print(calc_pi())
# print()

# 2 Задача: Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
print('Задача 2:')
num = int(input("Введите число: "))
i = 2 # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")
print()

# 3 Задача: Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
print('Задача 3:')
lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")
print()

# 4 Задача: Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
print('Задача 4:')
import random

def write_file(st):
    with open('file33.txt', 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0,101)


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))
print()

# 5 Задача: Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

print('Задача 5:')
with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')
print()