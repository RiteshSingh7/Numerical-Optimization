# REGION ELIMINATION METHODS
# Golden Section Search method
# for Unimodal functions only
from math import *
import pandas as pd
def func(x):
	try:
		return x**2 - 2.6*x + 2
	except:
		return inf
try:
	low = float(input('Enter lower bound: '))
	high = float(input('Enter upper bound: '))
	l = float(input('Enter level of uncertainity (>0): '))
except:
	print('Enter valid inputs')
	quit()
if high <= low or l <= 0:
	print('Enter again')
	quit()
col = ['k', 'a[k]', 'b[k]', 'lam[k]', 'mu[k]', 'f(lam[k])', 'f(mu[k])', 'f(lam[k])>f(mu[k])']
table = pd.DataFrame(columns = col)
alpha, k = 0.618, 1
a, b, lam, mu = ([0] for i in range(4))
a.append(low)
b.append(high)
lam.append(low + (1-alpha)*(high-low))
mu.append(low + alpha*(high-low))
while (b[k]-a[k]) > l:
	table.loc[k-1, 'k'] = k
	table.loc[k-1, 'a[k]'] = round(a[k],2)
	table.loc[k-1, 'b[k]'] = round(b[k],2)
	table.loc[k-1, 'lam[k]'] = round(lam[k],2)
	table.loc[k-1, 'mu[k]'] = round(mu[k],2)
	table.loc[k-1, 'f(lam[k])'] = round(func(lam[k]),3)
	table.loc[k-1, 'f(mu[k])'] = round(func(mu[k]),3)
	if func(lam[k]) > func(mu[k]):
		table.loc[k-1, 'f(lam[k])>f(mu[k])'] = 'yes'
		a.append(lam[k])
		b.append(b[k])
		lam.append(mu[k])
		mu.append(a[k+1] + alpha*(b[k+1]-a[k+1]))
	else:
		table.loc[k-1, 'f(lam[k])>f(mu[k])'] = 'no'
		a.append(a[k])
		b.append(mu[k])
		mu.append(lam[k])
		lam.append(a[k+1] + (1-alpha)*(b[k+1]-a[k+1]))
	k = k + 1
table.loc[k-1, 'k'] = k
table.loc[k-1, 'a[k]'] = round(a[k],2)
table.loc[k-1, 'b[k]'] = round(b[k],2)
table.loc[k-1, 'lam[k]'] = ''
table.loc[k-1, 'mu[k]'] = ''
table.loc[k-1, 'f(lam[k])'] = ''
table.loc[k-1, 'f(mu[k])'] = ''
table.loc[k-1, 'f(lam[k])>f(mu[k])'] = ''
print(table)
min = (a[k] + b[k]) / 2
print('The minimal value of x may be taken as',round(min,3),'with f(x) =',round(func(min),4))