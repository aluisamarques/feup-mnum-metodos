
import math
e = 2.718281

def f(x):
    return(5.5*x**2 + 6.2*x - 2.1)

def bissetriz(a,b):
    a = float(a)
    b = float(b)
    med = (a+b)/2.0
    medp = med
    count = 0
    while(True):
        if(f(a)*f(med)<0):
            b = med
        else:
            a = med
        med = (a+b)/2
        if(abs((med-medp))<=(10**(-3))):
            return count
        medp = med
        count+=1

            
print(bissetriz(-2,-1))

