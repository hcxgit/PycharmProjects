# -*- coding: utf-8 -*-
import numpy as np

#                 第一章 1
l = [93,95,106,108,110]

mean = np.mean(l)
var = np.var(l,ddof=1)
print mean         #平均值
print var          #样本方差

#         4
l = [76,54,58,38,69]
median = np.median(l)     #中位数
mean = np.mean(l)
var = np.var(l,ddof=1)
ptp = np.ptp(l)         #极差
std = np.std(l,ddof=1)         #标准差
print median
print mean
print var
print ptp
print std

#           5
l = [2.066,2.063,2.068,2.060,2.067]
ptp = np.ptp(l)
print ptp

#			48
x = [-2,0,2]
Pk = [0.4,0.3,0.3]
Ex = 0
for i in range(3):
	Ex += x[i] * Pk[i]
print Ex                 #  E(x)
Dx = np.var(x)
Ex2 =3*(Dx + np.square(Ex) )+5  #  E(3X^2+5)
print Ex2

                 #  86
x = [198,201,199,200,203,196,202,198,204,199]
x.sort()
for i in x:
	if i < x[0]:
		fn = 0
		print '%d %f' % (x[0], fn)
	elif i>=x[9]:
		fn = 1
		print '%d %f'%(x[9],fn)
	else:
		for k in range(1,9):
			x[k] <= i < x[k + 1]
			fn = float(k %10)
			print '%d=<x<%d   %0.1f'%(x[k],x[k+1],fn)
		'''
		print '当x <196 时，fn（x）等于0'
	elif 196 <= x[i] and x[i] <198:
		fn = (i + 1) / 10
		print '当196 <= x <198 时，fn（x）等于%f' % fn
	elif 198 <= x[i] and x[i] <199:
		fn = (i + 1) / 10
		print '当198 <= x <199 时，fn（x）等于%f' % fn
	elif 199 <= x[i] and x[i] <200:
		fn = (i + 1) / 10
		print '当199 <= x <200 时，fn（x）等于%f' % fn
	elif 200 <= x[i] and x[i] <201:
		fn = (i + 1) / 10
		print '当200 <= x <201 时，fn（x）等于%f' % fn
	elif 201 <= x[i] and x[i] <202:
		fn = (i + 1) / 10
		print '当201 <= x <202 时，fn（x）等于%f' % fn
	elif 202 <= x[i] and x[i] <203:
		fn = (i + 1) / 10
		print '当202 <= x <203 时，fn（x）等于%f' % fn
	elif 203 <= x[i] and x[i] <204:
		fn = (i + 1) / 10
		print '当203 <= x <204 时，fn（x）等于%f' % fn
	elif 204 <= x[i]:
		fn = (i + 1) / 10
		print '当204 <= x  时，fn（x）等于%f' % fn
	'''
x=[2,4,6]
mean = np.mean(x)
def X(mean):
	2*0.2+4*(0.6-p)+6*p==mean
	print p
x=[2752,2843,2836,2741,2890]
u=np.mean(x)
S2=np.var(x,ddof=1)
