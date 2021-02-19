

def f(x,y):
    return(x**2 + y**2)


#método de 1 ordem, se o passo for adequado Qc = 2
def euler(x0, xf,y0, h):
    n = int ((xf-x0)/h)
    print(n)
    yn = y0 + f(x0, y0)*h
    xn = x0 + h
    
    for i in range(0,n):
        xp = xn + h
        yp = yn + f(xn,yn) * h
        xn = xp
        yn = yp
        
        
    return yn, xn

def rk2(x0, xf, y0, h):
    n = int((xf-x0)/h)
    yn = y0 + h * f(x0+(h/2), y0+(h/2)*f(x0,y0))
    xn = x0 + h
    for i in range(0,n):
        yp = yn + h * f(xn+(h/2), yn+(h/2)*f(xn,yn))
        xp = xn + h
        xn = xp
        yn =  yp

def f1(x,y,h):
    return(h*f(x,y))

def f2(x,y,h):
    return(h * f(x+(h/2),y+(f1(x,y,h)/2)))

def f3(x,y,h):
    return (h*f(x+(h/2), y+f2(x,y,h)/2))

def f4(x,y,h):
    return(h * f(x+h, y+f3(x,y,h)))

def rk4(x0, xf, y0,h):
    n = int((xf-x0)/h)
    yn = y0 + (f1(x0,y0,h)/6)+f2(x0,y0,h)/3 + f3(x0,y0,h)/3 + f4(x0,y0,h)/6  
    xn = x0 + h
    for i in range(0,n):
        yp = yn + (f1(xn,yn,h)/6)+f2(xn,yn,h)/3 + f3(xn,yn,h)/3 + f4(xn,yn,h)/6  
        xp = xn + h
        xn = xp
        yn = yp
    return round(yn,5)

def y(x,y,z):
    #return(z*y+x)
    return z

def z(x,y,z):
    #return(z*x+y)
    return 0.5*z - y
    

def euler_sup(x0,xf,y0,z0,h):
    n = int((xf-x0)/h)
    for i in range (0,n):
        xn = x0 + h
        yn = y0 + y(x0,y0,z0)*h
        zn = z0 + z(x0,y0,z0)*h
        z0 = zn
        x0 = xn
        y0 = yn
    return zn, yn, xn


def rk2_sup(x0, xf, y0,z0, h):
    n = int((xf-x0)/h)
    for i in range(0,n):
        yp = y0 + h * y(x0+(h/2), y0+(h/2)*y(x0,y0,z0), z0+(h/2)*z(x0,y0,z0))
        xp = xn + h
        zp = zn + h * z(x0+(h/2), y0+(h/2)*y(x0,y0,z0), z0+(h/2)*z(x0,y0,z0))
        x0 = xp 
        y0 =  yp
        z0 = zp
    return zn, yn, xn

def d1y(x,y,z):
    return(z)

def d1z(x, y, z):
    return(-8*y - 0.6*z)

def l1(x,y,z,h):
    return(h*d1y(x,y,z))

def m1(x,y,z,h):
    return(h*d1z(x,y,z))

def l2(x,y,z,h):
    return(h*d1y(x+(h/2),y+ l1(x,y,z,h)/2,z + (m1(x,y,z,h)/2)))

def m2(x,y,z,h):
    return( h* d1z(x+(h/2),y+ l1(x,y,z,h)/2,z + (m1(x,y,z,h)/2)))

def l3(x,y,z,h):
    return(h* d1y(x+(h/2), y + l2(x,y,z,h)/2, z +m2(x,y,z,h)/2))

def m3(x,y,z,h):
    return(h* d1z(x+(h/2), y + l2(x,y,z,h)/2, z +m2(x,y,z,h)/2))

def l4(x,y,z,h):
    return(h*d1y(x+h, y + l3(x,y,z,h), z +m3(x,y,z,h)))

def m4(x,y,z,h):
    return(h*d1z(x+h, y + l3(x,y,z,h), z +m3(x,y,z,h)))

def rk4_sup(x0, xf, y0, z0, h):
    n = int((xf-x0)/h)
    for i in range(0,n):
        xn = x0 + h
        yn = y0 + l1(x0,y0,z0,h)/6 + l2(x0,y0,z0,h)/3 + l3(x0,y0,z0,h)/3 + l4(x0,y0,z0,h)/6
        zn = z0 + m1(x0,y0,z0,h)/6 + m2(x0,y0,z0,h)/3 + m3(x0,y0,z0,h)/3 + m4(x0,y0,z0,h)/6
        z0 = zn
        y0 = yn
        x0 = xn
    return zn, yn, xn
    
    

print(rk4_sup(0,0.5,4,0,0.1))
    
    
    
    
