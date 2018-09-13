#coding:utf-8
import  math
def Jie(a,b,c):
	deta = math.pow(b,2)-4*a*c
	if a == 0:
		result = -b/c
		print '解为：%.2f'%result
	elif deta>=0:
		result1 = (-b+math.sqrt(deta))/(2*a)
		print '解1为：%.2f'%result1
		result2 = (-b-math.sqrt(deta))/(2*a)
		print '解2为：%.2f' % result2
	else:
		print '无解'

print'请输入一元二次方程的系数a,b,c'
a=input()
b=input()
c=input()
Jie(a,b,c)
