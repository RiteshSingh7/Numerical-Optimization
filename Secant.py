# GRADIENT BASED METHODS
# Secant method
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
try:
	low = float(input('Enter lower bound : '))
	high = float(input('Enter upper bound : '))
	dx = float(input('Enter stopping criteria for f(x) (>0): '))
except:
	print('Enter valid inputs')
	quit()
if high <= low or dx<=0 or func1(low)*func1(high) >= 0:
	print('Enter again')
	quit()
col = ['x[k]', "f'(x[k])"]
table = pd.DataFrame(columns = col)
table.loc[0, 'x[k]'] = low
table.loc[0, "f'(x[k])"] = func1(low)
table.loc[1, 'x[k]'] = high
table.loc[1, "f'(x[k])"] = func(high)
k = 2
while True:
	new = high - func1(high)*(high-low)/(func1(high)-func1(low))
	table.loc[k, 'x[k]'] = new
	table.loc[k, "f'(x[k])"] = func1(new)
	if fabs(func1(new)) < dx: break
	elif func1(high)*func1(new) > 0: high = new
	else: low = new
	k += 1
print(table)
print('Point of minima is',new,'with function value',func(new))