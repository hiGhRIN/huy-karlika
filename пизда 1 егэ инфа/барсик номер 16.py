#задание 2
#F(n) = 1 при n = 1;
#F(n) =, если n чётно;
#F(n) = 2 × F(n - 2), если n > 1 и при этом n нечётно.
#Чему равно значение функции F (24)?

import sys
sys.setrecursionlimit(10**7)
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f(n - 1)
    if n > 1:
        if n % 2 == 1:
            return 2 * f(n - 2)

print (f(24))

#задание 3
#F(n) = 1 при n > 3000;
#F(n) = F(n + 1) - n + 1, если n _ 3000 и при этом n чётно;
#F(n) = F(n + 2) - 2 • n + 2, если п 3000 и при этом п нечётно.
#Чему равно значение выражения 2 × F(39) - 2 × F(34)?

import sys
sys.setrecursionlimit(10**7)
def f(n):
    if n > 3000:
        return 1
    if n <= 3000:
        if n % 2 == 0:
            return f(n + 1) - n + 1
    if n <= 3000:
        if n % 2 == 1:
            return f(n + 2) - 2 * n + 2

print (2 * f(39) - 2 * f(34))

#задание 4
#F(n) = 1 при n = 1;
#F(n) = n2 + F(n - 1), если n > 1.
#Чему равно значение выражения F(1 000) - F(997)?

from functools import cache

import sys
sys.setrecursionlimit(10**7)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n**2 + f (n - 1)

print (f(1000) - f (997))

#задание 5
#F(n) = n при п <= 10
#F(n) = n//4 + F(n - 10) при 10 < n <= 36
#F(n) = 2 • F(n - 5) при n > 36
#В качестве ответа на задание выведите значение F(100).

import sys
sys.setrecursionlimit(10**7)
def f(n):
    if n <= 10:
        return n
    if 10 < n <= 36:
        return n//4 + f(n - 10)
    if n > 36:
        return 2 * f(n - 5)

print (f(100))

#задание 6
#F(n) = 2, если п < 3
#F(n) = 2 • F(n - 2), если n > 2
#Чему равно значение выражения F (2222)/F(2182)?

import sys
sys.setrecursionlimit(10**7)
def f(n):
    if n < 3:
        return 2
    if n > 2:
        return 2 * f(n - 2)

print(f(2222)/f(2182))

#задание 7
#F(n) = 1 при n < 3;
#F(n) = F(n - 1) + n, если > 2 и при этом п нечётно;
#F(n) = F(n - 3) + 2n, если n > 2 и при этом п чётно.
#Чему равно значение выражения F(2048) - F(2041)?

import sys
sys.setrecursionlimit(10**7)
def f(n):
    if n < 3:
        return 1
    if n > 2:
        if n%2 == 1:
            return f(n - 1) + n
    if n > 2:
        if n%2 == 0:
            return f(n - 3) + 2*n

print(f(2048) - f(2041))

#задание 9
#F(n) = n при n > 3000;
#F(n) = (2 * n + 4) * F(n + 2), если n <= 3000.
#Чему равна сумма цифр значения выражения F(20)/F(28)?

import sys
sys.setrecursionlimit(10**7)
def f(n):
    if n > 3000:
        return n
    if n <= 3000:
        return (2 * n + 4) * f(n + 2)

print(f(20)/f(28))

#задание 1
#F(n) = 1, если n = 1
#F(n) = n + F(n - 1), если n > 1.
#Определите количество значений п на отрезке [1, 100], для которых значение выражения F(2023)//F(n) будет четным.

import sys
sys.setrecursionlimit(10**7)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n + f(n-1)

count = 0
for n in range (1,101):
    if (f(2023)//f(n))%2 == 0:
        count += 1

print(count)

#задание 10
#F(n) = n, если п _ 10;
#F(n) = 2 • F(n - 2) + 6, если п > 10 и чётно;
#F(n) = F(n - 1) 2 • n, если п > 10 и нечётно.
#Чему равна сумма цифр значения функции F(27) - F(20)?

import sys
sys.setrecursionlimit(10**7)
def f(n):
    if n <= 10:
        return n
    if n > 10:
        if n%2 == 0:
            return 2 * f(n - 2) + 6
    if n > 10:
        if n%2 == 1:
            return f(n - 1) + 2 * n

print(f(27) - f(20))

#задание 8
#F(n) = 1 при п = 1;
#F(n) = (n - 1) × F(n - 1), если n > 1.
#Чему равно значение выражения (F(2024)/7 - F(2023))/F(2022)?

import sys
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * f(n - 1)

print(f(2024)/7)
