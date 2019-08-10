# POINT ESTIMATION METHOD
# Successive Quadratic Estimation method
# for Unimodal functions only
from math import *
import pandas as pd
from random import shuffle
def func(x):
	try:
		return x**2 + 54/x
	except:
		return inf
x = [0 for i in range(3)]
f = [0 for i in range(3)]
try:
	dx = float(input('Enter minimum function separation (>0): '))
	dx1 = float(input('Enter minimum point separation (>0): '))
	x[0] = float(input('Enter initial guess point: '))
	delta = float(input('Enter step size: '))
except:
	print('Enter valid inputs')
	quit()
if dx <= 0 or dx1 <= 0 or delta == 0:
	print('Enter again')
	quit()
col = ['x1,f(x1)', 'x2,f(x2)', 'x3,f(x3)', 'Xmin,Fmin', 'a0', 'a1', 'a2', 'x`,f(x`)']
table = pd.DataFrame(columns = col)
row = 0
x[1] = x[0] + delta
if func(x[0]) > func(x[1]):
	x[2] = x[0] + 2*delta
else:
	x[2] = x[0] - delta
for i in range(3):
	f[i] = func(x[i])
while True:
	table.loc[row, 'x1,f(x1)'] = (round(x[0],2),round(f[0],2))
	table.loc[row, 'x2,f(x2)'] = (round(x[1],2),round(f[1],2))
	table.loc[row, 'x3,f(x3)'] = (round(x[2],2),round(f[2],2))
	fmin = min(f)
	k = f.index(fmin)
	xmin = x[k]
	table.loc[row, 'Xmin,Fmin'] = (round(xmin,2),round(fmin,2))
	while True:
		a0 = f[0]
		a1 = (f[1]-f[0]) / (x[1]-x[0])
		a2 = ((f[2]-f[0])/(x[2]-x[0]) - a1) / (x[2]-x[1])
		if a2 > 0: break
		shuffle(x)
		for i in range(3):
			f[i] = func(x[i])
	table.loc[row, 'a0'] = round(a0,2)
	table.loc[row, 'a1'] = round(a1,2)
	table.loc[row, 'a2'] = round(a2,2)
	xbar = (x[0] + x[1] - a1/a2) / 2
	x.append(xbar)
	f.append(func(xbar))
	table.loc[row, 'x`,f(x`)'] = (round(x[3],2),round(f[3],2))
	if fabs(fmin-f[3]) < dx or fabs(xmin-x[3]) < dx1: break
	x.sort()
	for i in range(4):
		f[i] = func(x[i])
	k = f.index(min(f))
	if k == 1:
		x.pop()
		f.pop()
	elif k == 2:
		x.pop(0)
		f.pop(0)
	else:
		l = f.index(max(f))
		x.pop(l)
		f.pop(l)
	row += 1
print(table)
if fmin < f[3]:
	print('Point of minima is',xmin,'with func value',fmin)
else:
	print('Point of minima is',x[3],'with func value',f[3])