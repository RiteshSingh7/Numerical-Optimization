# REGION ELIMINATION METHODS
# Interval Halving method
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
	dx = float(input('Enter terminating condition (small number): '))
except:
	print('Enter valid inputs')
	quit()
if b <= a:
	print('Enter again')
	quit()
xm = (a + b) / 2
l = b - a
col = ['Itr', 'a', 'b', 'L', 'x1', 'x2', 'f(x1)', 'f(x2)', 'Xm', 'f(Xm)', 'f(x1)<f(Xm)', 'f(x2)<f(Xm)']
table = pd.DataFrame(columns = col)
row = 0
while l > dx:
	table.loc[row, 'Itr'] = row + 1
	table.loc[row, 'a'] = round(a,3)
	table.loc[row, 'b'] = round(b,3)
	table.loc[row, 'L'] = round(l,3)
	x1 = a + l/4
	x2 = b - l/4
	table.loc[row, 'x1'] = round(x1,3)
	table.loc[row, 'x2'] = round(x2,3)
	table.loc[row, 'f(x1)'] = round(func(x1),3)
	table.loc[row, 'f(x2)'] = round(func(x2),3)
	table.loc[row, 'Xm'] = round(xm,3)
	table.loc[row, 'f(Xm)'] = round(func(xm),3)
	if func(x1) < func(xm):
		table.loc[row, 'f(x1)<f(Xm)'] = 'yes'
		table.loc[row, 'f(x2)<f(Xm)'] = 'no'
		b = xm
		xm = x1
	elif func(x2) < func(xm):
		table.loc[row, 'f(x1)<f(Xm)'] = 'no'
		table.loc[row, 'f(x2)<f(Xm)'] = 'yes'
		a = xm
		xm = x2
	else:
		table.loc[row, 'f(x1)<f(Xm)'] = 'no'
		table.loc[row, 'f(x2)<f(Xm)'] = 'no'
		a = x1
		b = x2
	l = b - a
	row += 1
print(table)
mid = (a+b) / 2
print('Minima lies at',round(mid,3),'with function value',round(func(mid),3))