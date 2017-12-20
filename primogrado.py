#primogrado.py

print "dare equazione in forma Ax + B = 0"

a = input("equazione A:")
b = input("equazione B:")

if a==0 and b==0:
    print "l'equazione ammette infinite soluzioni"
elif a==0:
    print "l'equazione non ammette soluzioni"
else:
    x = -float(b) / float(a)
    print "x = ", x
