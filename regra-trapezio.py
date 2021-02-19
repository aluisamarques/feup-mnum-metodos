
import math

def regra_trapezios(n, lim1, lim2):
    area = 0
    h = float((lim2 - lim1)/n)
    y0 = 0
    y1 = 0

    for i in range(0,n):
        y0 = math.sin(lim1)
        y1 = math.sin(lim1 + h)
        area += (h/2)*(y0+y1)
        lim1 =  lim1 + h
    return (area, h)

def regra_simpson(n, lim1, lim2):
    area = 0
    h = float(float(lim2 - lim1)/(n*2))
    for i in range(0,n):
        y0 = math.sin(lim1)
        y1 = math.sin(lim1 + h)
        y2 = math.sin(lim1 + 2*h)
        area += (h/3)*(y0 + 4*y1 + y2)
        lim1 = lim1 + 2*h
    return (area, h)


def cubatura():
    

print(regra_simpson(4,0,math.pi))
    
