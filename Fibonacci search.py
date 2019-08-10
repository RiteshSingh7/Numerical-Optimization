# REGION ELIMINATION METHODS
# Fibonacci Search method
# for Unimodal functions only
from math import *
import pandas as pd
def func(x):
	try:
		return x**2 - 2.6*x + 2
	except:
		return inf
def fib(n):
	if n==0 or n==1: result = 1
	else: result = fib(n-1) + fib(n-2)
	return result
try:
	low = float(input('Enter lower bound: '))
	high = float(input('Enter upper bound: '))
	dx = float(input('Enter minimum permissible separation (dx>0): '))
	l = float(input('Enter minimum allowable length (>= 2*dx): '))
except:
	print('Enter valid inputs')
	quit()
if high <= low or dx <= 0 or l < 2*dx:
	print('Enter again')
	quit()
n = 0
while fib(n) < (high-low)/l :
	n += 1
col = ['k', 'a[k]', 'b[k]', 'lam[k]', 'mu[k]', 'f(lam[k])', 'f(mu[k])']
table = pd.DataFrame(columns = col)
k = 1
a, b, lam, mu = ([0] for i in range(4))
a.append(low)
b.append(high)
lam.append(low + (high-low)*fib(n-2)/fib(n))
mu.append(low + (high-low)*fib(n-1)/fib(n))
table.loc[0, 'k'] = k
table.loc[0, 'a[k]'] = a[k]
table.loc[0, 'b[k]'] = b[k]
table.loc[0, 'lam[k]'] = lam[k]
table.loc[0, 'mu[k]'] = mu[k]
table.loc[0, 'f(lam[k])'] = func(lam[k])
table.loc[0, 'f(mu[k])'] = func(mu[k])
while k < n-1:
	if func(lam[k]) > func(mu[k]):
		a.append(lam[k])
		b.append(b[k])
		lam.append(mu[k])
		mu.append(a[k+1] + (b[k+1]-a[k+1])*fib(n-k-1)/fib(n-k))
	else:
		a.append(a[k])
		b.append(mu[k])
		mu.append(lam[k])
		lam.append(a[k+1] + (b[k+1]-a[k+1])*fib(n-k-2)/fib(n-k))
	table.loc[k, 'k'] = k + 1
	table.loc[k, 'a[k]'] = a[k+1]
	table.loc[k, 'b[k]'] = b[k+1]
	table.loc[k, 'lam[k]'] = lam[k+1]
	table.loc[k, 'mu[k]'] = mu[k+1]
	table.loc[k, 'f(lam[k])'] = func(lam[k+1])
	table.loc[k, 'f(mu[k])'] = func(mu[k+1])
	k += 1
lam.append(lam[n-1])
mu.append(mu[n-1] + dx)
if func(lam[n]) > func(mu[n]):
	a.append(lam[n])
	b.append(b[n-1])
else:
	a.append(a[n-1])
	b.append(lam[n])
table.loc[k, 'k'] = k + 1
table.loc[k, 'a[k]'] = a[k+1]
table.loc[k, 'b[k]'] = b[k+1]
table.loc[k, 'lam[k]'] = ''
table.loc[k, 'mu[k]'] = ''
table.loc[k, 'f(lam[k])'] = ''
table.loc[k, 'f(mu[k])'] = ''
print(table)
min = (a[n] + b[n]) / 2
print('The optimal solution is at',round(min,4),'with objective value',round(func(min),4))