# BRACKETING METHODS
# Exhaustive Search method
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
	n = int(input('Enter number of intermediate parts: '))
except:
	print('Enter valid inputs')
	quit()
if b <= a:
	print('Enter again')
	quit()
if n < 2:
	print('Minimum lies between',a,'and',b)
	quit()
dx = (b - a) / n
x1 = a
x2 = x1 + dx
x3 = x2 + dx
col = ['Iter', 'x1', 'x2', 'x3', 'f(x1)', 'f(x2)', 'f(x3)', 'f(x1)>f(x2)>f(x3)']
table = pd.DataFrame(columns = col)
row = 0
while x3 <= b:
	table.loc[row, 'Iter'] = row + 1
	table.loc[row, 'x1'] = x1
	table.loc[row, 'x2'] = x2
	table.loc[row, 'x3'] = x3
	f1 = func(x1)
	f2 = func(x2)
	f3 = func(x3)
	table.loc[row, 'f(x1)'] = f1
	table.loc[row, 'f(x2)'] = f2
	table.loc[row, 'f(x3)'] = f3
	if f1 > f2 and f2 > f3:
		table.loc[row, 'f(x1)>f(x2)>f(x3)'] = 'yes'
	else:
		table.loc[row, 'f(x1)>f(x2)>f(x3)'] = 'no'
	if f2<=f1 and f2<=f3:
		break
	else:
		x1 = x2
		x2 = x3
		x3 = x3 + dx
		row += 1
print(table)
if x3 > b:
	print('Minimum is at boundary points')
else: 
	print('Minimum lies between',x1,'and',x3)