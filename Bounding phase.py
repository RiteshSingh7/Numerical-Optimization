# BRACKETING METHODS
# Bounding Phase method
# for Unimodal functions only
from math import *
import pandas as pd
def func(x):
	try:
		return x**2 + 54/x
	except:
		return inf
try:
	a = float(input('Enter lower bound: '))
	b = float(input('Enter upper bound: '))
	temp = float(input('Enter initial guess: '))
	dx = float(input('Enter increment: '))
except:
	print('Enter valid inputs')
	quit()
if b <= a or a > (temp-fabs(dx)) or b < (temp+fabs(dx)) :
	print('Enter again')
	quit()
k = 0
x = list()
f = list()
f1 = func(temp - fabs(dx))
f2 = func(temp)
f3 = func(temp + fabs(dx))
if f1>=f2 and f2>=f3:
	if dx < 0: dx = -dx
elif f1<=f2 and f2<=f3:
	if dx > 0: dx = -dx
else:
	print('Enter again')
	quit()
x.append(temp)
f.append(func(x[k]))
col = ['Iter', 'x(k)', 'f(x(k))', 'f(x(k+1)) < f(x(k))']
table = pd.DataFrame(columns = col)
table.loc[k, 'Iter'] = k
table.loc[k, 'x(k)'] = x[k]
table.loc[k, 'f(x(k))'] = f[k]
table.loc[k, 'f(x(k+1)) < f(x(k))'] = ''
while True:
	x.append(x[k] + 2**k * dx)
	f.append(func(x[k+1]))
	table.loc[k+1, 'Iter'] = k+1
	table.loc[k+1, 'x(k)'] = x[k+1]
	table.loc[k+1, 'f(x(k))'] = f[k+1]
	if f[k+1] <= f[k]:
		table.loc[k+1, 'f(x(k+1)) < f(x(k))'] = 'yes'
		k += 1
	else:
		table.loc[k+1, 'f(x(k+1)) < f(x(k))'] = 'no'
		break
print(table)
print('Minimum lies between',x[k-1],'and',x[k+1])