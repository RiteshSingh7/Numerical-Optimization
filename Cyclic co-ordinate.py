# MULTI DIMENSIONAL SEARCH
# Cyclic Co-ordinate Method
from math import *
import pandas as pd
def func(x):
	try:
		return (x[0]-2)**4 + (x[0]-2*x[1])**2
	except:
		return inf
def fun1(x):
	try:
		return 4*(x[0]-2)**3 + 2*(x[0]-2*x[1])
	except:
		return inf
def fu1(x):
	try:
		return 12*(x[0]-2)**2 + 2
	except:
		return inf
def fun2(x):
	try:
		return -4*(x[0]-2*x[1])
	except:
		return inf
def fu2(x):
	return 8
x = [0 for i in range(2)]
print('Enter initial estimate')
try:
	for i in range(2):
		print('Enter',i+1,'th dimension: ')
		x[i] = float(input())
	dx = float(input('Enter stopping criteria (>0): '))
except:
	print('Enter valid inputs')
	quit()
if dx <= 0:
	print('Enter again')
	quit()
def add(x, lam, i):
	x[i] = x[i] + lam
	return x
col = ['k', 'X(k),f(X(k))', 'j', 'Y(j)', 'e(j)', 'lambda(j)', 'Y(j+1)']
table = pd.DataFrame(columns = col)
row = 0
while True:
	table.loc[row, 'k'] = row/2 + 1
	table.loc[row+1, 'k'] = ''
	table.loc[row, 'X(k),f(X(k))'] = [round(a,2) for a in x]
	table.loc[row+1, 'X(k),f(X(k))'] = round(func(x),2)
	lam = 0
	y1 = x.copy()
	table.loc[row, 'j'] = 1
	table.loc[row, 'Y(j)'] = [round(a,2) for a in y1]
	table.loc[row, 'e(j)'] = (1,0)
	while True:
		y1 = add(y1, lam, 0)
		if fabs(fun1(y1)) < dx: break
		new = lam - fun1(y1)/fu1(y1)
		if fabs(new-lam) < dx:
			lam = new
			y1 = x.copy()
			y1 = add(y1, lam, 0)
			break
		else:
			lam = new
			y1 = x.copy()
	table.loc[row, 'lambda(j)'] = round(lam,2)
	table.loc[row, 'Y(j+1)'] = [round(a,2) for a in y1]
	lam = 0
	y2 = y1.copy()
	table.loc[row+1, 'j'] = 2
	table.loc[row+1, 'Y(j)'] = [round(a,2) for a in y2]
	table.loc[row+1, 'e(j)'] = (0,1)
	while True:
		y2 = add(y2, lam, 1)
		if fabs(fun2(y2)) < dx: break
		new = lam - fun2(y2)/fu2(y2)
		if fabs(new-lam) < dx:
			lam = new
			y2 = y1.copy()
			y2 = add(y2, lam, 1)
			break
		else:
			lam = new
			y2 = y1.copy()
	table.loc[row+1, 'lambda(j)'] = round(lam,2)
	table.loc[row+1, 'Y(j+1)'] = [round(a,2) for a in y2]
	if (y2[0]-x[0])**2 + (y2[1]-x[1])**2 < dx:
		x = y2.copy()
		break
	else:
		x = y2.copy()
		row += 2
print(table)
print('Optimal solution is',[round(a,2) for a in x])
print('Objective function value is',round(func(x),2))