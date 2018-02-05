from sympy import *

x = symbols('x')

a = Integral(((x*x*x)*(sin(x)**2))/(x**4+2*x*x+1),(x,-5,5))
pprint(a)
print("结果是:"+str(a.evalf()))


