from random import randint
a = randint(1,10)
print 'guss what i think'
b = input()
while b != a:
	if b<a:
		print  '%d is too small'%b
	if b>a:
		print '%d is too big'%b
	b = input()
if b==a:
	print 'Bingo!!!!'

