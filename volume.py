#volume.py

import math

print "Calcolo volume cubo o volume sfera"
print "inserire 1 per volume cubo"
print "inserire 2 per volume sfera"

n = input()

if n==1:
    x = input("inserire lato del cubo")
    v = x *x *x
    print "il volume del cubo di lato ", n, "e' ", v
elif n==2:
    x = input("inserire il raggio della sfera")
    v = 4./3. *math.pi *x *x *x
    print "il volume della sfera di raggio ", n, "e' ", v
else:
    print "numero inserito non corretto"
