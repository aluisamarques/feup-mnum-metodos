
import math
def g(x,y):
	return 0.7 + x
        #return 1 - x**2

def f(x,y):
	return - math.sqrt(1-y)
        #return y-0.7


def picard_peano(x,y):
	yp = g(x,y)
	xp = f(x,y)
	i= 0
	while(True):
		yn = g(xp,yp)
		xn = f(xp,yp)
		if(abs(yn-yp)<10**-3 and abs(xn-xp)<10**-3):
			return(xn,yn,i)
		i+=1
		yp = yn
		xp = xn
		print(xp,yp)
		
print(picard_peano(0,0.5))
