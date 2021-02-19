import math

def f0(x):
    return(2*x + 1)**2 - 5* math.cos(10*x)

def aurea(x1,x2):

    b = (5**(1/2) - 1)/2
    a = b**2
    
    while(True):
        x3 = x1 + a * (x2-x1)
        x4 = x1 + b * (x2-x1)
        if f(x3)> f(x4):
            x2 = x4
        elif f(x3) < f(x4):
            x1 = x3    
        if(abs(x2-x1)<=0.001):
            return x1, f(x1)


#x(n+1) = xn - h*gradiente(xn)
def gradiente(x0,y0,h):
    xn = x0 - h * dgdx(x0,y0)
    yn = y0 - h * dgdy(x0,y0)
    i =0
    while(True):
        xn1 = xn - h * dgdx(xn,yn)
        yn1 = yn - h * dgdy(xn,yn)
        if(f(xn1,yn1)>f(xn,yn)):
            h = h * 2
        else:
            h = h / 2
    
        if (abs(xn1-xn) <= 0.001 or abs(yn1-yn) <=0.001):
            return xn, yn, f(xn,yn)
        i+=1
        print("i",i,"xn",xn,h,1/h,dgdx(xn,yn),dgdy(xn,yn),"f(x)",f(xn,yn))
        yn = yn1
        xn = xn1


def g(x,y):
    return math.sin(x/2)+x**2-math.cos(y)

def dgdx(x,y):
    return math.cos(x/2)/2 + 2*x

def dgdy(x,y):
    return math.sin(y)

def inv_hes_y_vezes_gradiente(yn):
    return math.sin(yn)/math.cos(yn)

def inv_hes_x_vezes_gradiente(xn):
    return ((2*xn +(math.cos(xn/2)/2))/(2-math.sin(xn/2)/4))

def quadrica(x,y):
    xn = x 
    yn = y 
    i = 0
    while(True):
        xn1 = xn - inv_hes_x_vezes_gradiente(xn)
        yn1 = yn - inv_hes_y_vezes_gradiente(yn)
    
        i+=1
        if (abs(xn1-xn) < 0.001 and abs(yn1-yn) <0.001):
            return xn1, yn1

        yn = yn1
        xn = xn1
        print(xn, yn)

def luisa_marq(x,y,l):
    i = 0
    xn = x
    yn = y
    while(True):
        xn1 = xn-  l*dgdx(xn,yn) - inv_hes_x_vezes_gradiente(xn)
        yn1 = yn  - l*dgdy(xn,yn) - inv_hes_y_vezes_gradiente(yn)
        i+=1

        if(g(xn1,yn1)>g(xn,yn)):
            l/= 2
        elif(g(xn1,yn1)<g(xn,yn)):
            l*=2


        print('x: ',xn,'y: ',yn,'l: ',l,"f",g(xn,yn))
        if(abs(xn1-xn)<0.001 and abs(yn1-yn)<0.001):
            return xn1, yn1
        yn = yn1
        xn = xn1
        
        
       
    

luisa_marq(-10,-1,0.01)
    
    
    
