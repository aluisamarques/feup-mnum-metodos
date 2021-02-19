import math
e = 2.718281

def f(x):
    return(x-2*math.log(x)-5)

def d(x):
    return(float(1-(2/x)))

def g1(x):
    return(e**((x-5)/2))

def g(x):
    return (2*math.log(x)+5)

def pp(x):
    xn = g(x)
    xp = g(x)

    while (True):
        xn = g(xp)
        if (abs(((xn-xp)/xn)<=10**-4)) :
            return xn
        print(xn)
        xp = xn
        
def newton(x):
    xn = x - f(x) / d(x)
    xp = xn
    while(True):
        xn = xp - f(xp)/d(xp)
        if(abs((xn-xp)/xn) <= 10**-4):
            return xn
        print(xn)
        xp = xn
        
newton(0.1)

