#secgrado.py

import math

print "inserire equazione di secono grado in forma ax^2 + bx + c = 0"

a = input("a = ")
b = input("b = ")
c = input("c = ")

if a==0 and b==0 and c==0:
    print "l'equazione ammette infinite soluzioni"

elif a==0 and b==0:
    print "l'equazione non ammette soluzioni"

elif a==0:
    r = -float(c) / float(b)
    print "x = ", r

else:
    d = b *b - 4 *a *c
    
    if d < 0:
        print "l'equazione non ha soluzioni reali"
    elif d == 0:
        x = -b / 2 *a
        print "x1 = x2 = ", x
    else:
        x1 = (-b + math.sqrt(d)) / 2 *a
        x2 = (-b - math.sqrt(d)) / 2 *a
        print "x1 = ", x1, "x2 = ", x2

