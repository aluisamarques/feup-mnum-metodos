
import math
e = 2.718281

def f(x):
    return(x - 2*math.log(x)-5)

def corda(a,b):
    a = float(a)
    b = float(b)
    d = (a*f(b) - b*f(a))/(f(b)-f(a))
    while(True):
        if(abs((b-a)/a) <= 10**-4):
            return(d)
        if((f(a) * f(d) < 0)):
            b = d
        else:
            a = d
        d = (a*f(b) - b*f(a))/(f(b)-f(a))
        print(d)

corda(0.0005,3)
