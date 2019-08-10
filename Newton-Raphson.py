# GRADIENT BASED METHODS
# Newton-Raphson method
# for Unimodal functions only
from math import *
import pandas as pd
def func(x):
	try:
		return 0.25*x**4 - x**2 - 5*x + 1
	except:
		return inf
def func1(x):
	try:
		return x**3 - 2*x - 5
	except:
		return inf
def func2(x):
	try:
		return 3*x**2 - 2
	except:
		return inf
try:
	x = float(input('Enter initial estimate: '))
	dx = float(input('Enter stopping criteria for x (>0): '))
	eps = float(input('Enter stopping criteria for f(x) (>0): '))
except:
	print('Enter valid inputs')
	quit()
if dx<=0 or eps<=0:
	print('Enter again')
	quit()
col = ['x[k]', "f'(x[k])", 'f"(x[k])', 'x[k+1]', 'x[k+1]-x[k]', '|f"(x[k])|']
table = pd.DataFrame(columns = col)
k = 0
while fabs(func1(x)) >= eps:
	table.loc[k, 'x[k]'] = x
	table.loc[k, "f'(x[k])"] = func1(x)
	table.loc[k, 'f"(x[k])'] = func2(x)
	new = x - func1(x)/func2(x)
	table.loc[k, 'x[k+1]'] = new
	table.loc[k, 'x[k+1]-x[k]'] = new - x
	table.loc[k, '|f"(x[k])|'] = fabs(func2(x))
	if fabs(new-x) < dx:
		x = new
		break
	else:
		x = new
		k += 1
print(table)
print('Point of minima is',x,'with function value',func(x))