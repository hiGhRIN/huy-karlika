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