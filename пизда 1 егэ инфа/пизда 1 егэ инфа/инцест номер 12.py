print('номер 1.....☠️')
s = '5' * 874
while '555' in s or '111' in s:
    if '555' in s:
        s = s.replace('555', '1', 1)
    else:
        s = s.replace('111', '5', 1)
print (s.count('5'))

print('номер 2...☠️☠️☠️☠️☠️☠️☠️')
s = '1' + '0' * 55
while '1' in s:
    if '10' in s:
        s = s.replace('10', '001', 1)
    else:
        s = s.replace('1', '00', 1)
print (s.count('0'))

print('номер 3...☠️')
from random import shuffle
s = list ('1' * 13 + '2' * 17 + '0' * 19)
shuffle(s)
while '10' in s or '20' in s:
    if '20' in s:
        s = s.replace('20', '00', 1)
    else:
        s = s.replace('10', '200', 1)
print (s.count('0'))

print('номер 4...☠️')
for n in range (3, 10000):
    s = '4' + '1' * n
    while '411' in s  or '1111' in s:
        if '411' in s:
            s = s.replace('411', '14', 1)
        if '1111' in s:
            s = s.replace('1111', '1', 1)
print (s)

print('номер 5...')
s = '2' * 55 + '3' * 44 + '1' * 33
while '222' in s  or '333' in s or '111' in s:
    if '222' in s:
        s = s.replace('222', '11', 1)
    if '222' in s:
        s = s.replace('1111', '1', -1)
    elif '111' in s:
        s = s.replace('111', '3', 1)
    else:
        s = s.replace('333', '1', 1)
print (s)
