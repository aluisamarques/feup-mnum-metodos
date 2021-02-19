import math
e = 2.718281

def f(x):
    return(2*math.log(x)-5)

def g1(x):
    return(e**((x-5)/2))

def g(x):
    return (2*math.log(x)+5)

def pp(x):
    xn = g(x)
    xp = g(x)

    while (True):
        xn = g(xn)
        if (abs(((xn-xp)/xn)<=10**-4)) :
            return xn
        print(xn)
        xp = xn
        
    
pp(9)

