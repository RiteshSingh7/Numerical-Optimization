# GRADIENT BASED METHODS
# Cubic Search method
# for Unimodal functions only
from math import *
import pandas as pd
def func(x):
	try:
		return x**2 + 54/x
	except:
		return inf
def func1(x):
	try:
		return 2*x - 54/x**2
	except:
		return inf
try:
	x1 = float(input('Enter initial point: '))
	h = float(input('Enter step size: '))
	dx = float(input('Enter stopping criteria for x (>0): '))
	eps = float(input('Enter stopping criteria for f(x) (>0): '))
except:
	print('Enter valid inputs')
	quit()
if dx<=0 or eps<=0 or h==0:
	print('Enter again')
	quit()
if func1(x1) > 0:
	h = -fabs(h)
else:
	h = fabs(h)
col1 = ['x[k]', "f'(x[k])"]
tab1 = pd.DataFrame(columns = col1)
k = 0
tab1.loc[k, 'x[k]'] = x1
tab1.loc[k, "f'(x[k])"] = func1(x1)
while True:
	x2 = x1 + 2**k*h
	tab1.loc[k+1, 'x[k]'] = x2
	tab1.loc[k+1, "f'(x[k])"] = func1(x2)
	if func1(x1)*func1(x2) <= 0:
		k = 0
		break
	x1 = x2
	k += 1
print(tab1)
col2 = ['x1', 'x2', 'z', 'w', 'mu', 'x`', 'x``']
tab2 = pd.DataFrame(columns = col2)
while True:
	tab2.loc[k, 'x1'] = x1
	tab2.loc[k, 'x2'] = x2
	z = 3*(func(x1)-func(x2))/(x2-x1) + func1(x1) + func1(x2)
	tab2.loc[k, 'z'] = z
	w = sqrt(z**2-func1(x1)*func1(x2)) * (x2-x1) / fabs(x2-x1)
	tab2.loc[k, 'w'] = w
	mu = (func1(x2)+w-z) / (func1(x2)-func1(x1)+2*w)
	tab2.loc[k, 'mu'] = mu
	xbar = x2 - mu*(x2-x1)
	tab2.loc[k, 'x`'] = xbar
	while func(xbar) >= func(x1):
		xbar = xbar - (xbar-x1)/2
	tab2.loc[k, 'x``'] = xbar
	if fabs(func1(xbar)) <= eps or fabs(xbar-x1)/2 <= dx: break
	if func1(xbar)*func1(x1) < 0: x2 = xbar
	else: x1 = xbar
	k += 1
print(tab2)
print('Point of minima is',xbar,'with function value',func(xbar))