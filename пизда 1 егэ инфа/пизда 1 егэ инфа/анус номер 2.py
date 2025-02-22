print ('номер 1')
print('x,y,z')
for x in range (2):
    for y in range (2):
        for z in range (2):
            f = (x <= z) and (y <= x)
            if f == 1:
                print(x,y,z)

print ('номер 2')
print ('x,y,z,w')
for x in range (2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not w and ((y or z) <= (y and not x)))
                if f == 1:
                    print (x,y,z,w)

print ('номер 3')
print ('z,y,x,w')
for z in range (2):
    for y in range(2):
        for x in range(2):
            for w in range(2):
                f = (not x and not y) or (x == z) or w
                if f == 0:
                    print (z,y,x,w)
print ('номер 4')
print ('x,y,z,w')
for x in range (2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = ((x and (not y)) <= (z and w)) and ((y <= z) or (w <= x))
                if f == 0:
                    print (x,y,z,w)

print ('номер 5')
print ('x,y,z,w')
for x in range (2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (x or not y) and not (x == z) and w
                if f == 1:
                    print(x,y,z,w)