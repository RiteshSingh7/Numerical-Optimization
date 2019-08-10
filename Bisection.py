# GRADIENT BASED METHODS
# Bisection method
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
	low = float(input('Enter lower bound: '))
	high = float(input('Enter upper bound: '))
	dx = float(input('Enter stopping criteria for x (>0): '))
	eps = float(input('Enter stopping criteria for f(x) (>0): '))
except:
	print('Enter valid inputs')
	quit()
if high <= low or dx<=0 or eps<=0 or func1(low)*func1(high) >= 0:
	print('Enter again')
	quit()
k = 1
x = [low, high]
col = ['k', 'x[k-1]', 'x[k]', "f'(x[k-1])", "f'(x[k])", 'x[k+1]', "f'(x[k+1])"]
table = pd.DataFrame(columns = col)
while True:
	table.loc[k-1, 'k'] = k
	table.loc[k-1, 'x[k-1]'] = x[k-1]
	table.loc[k-1, 'x[k]'] = x[k]
	table.loc[k-1, "f'(x[k-1])"] = func1(x[k-1])
	table.loc[k-1, "f'(x[k])"] = func1(x[k])
	mid = (x[k-1]+x[k]) / 2
	table.loc[k-1, 'x[k+1]'] = mid
	table.loc[k-1, "f'(x[k+1])"] = func1(mid)
	if fabs(func1(mid)) < eps:
		print(table)
		print('Point of minima is', mid)
		break
	elif fabs(mid - x[k]) < dx:
		print(table)
		mid = (x[k]+mid) / 2
		print('Point of minima is',mid)
		break
	elif func1(x[k])*func1(mid) > 0:
		x[k] = x[k-1]
		x.append(mid)
	else:
		x.append(x[k])
		x[k] = mid
	k += 1
print('Minimum value is', func(mid))