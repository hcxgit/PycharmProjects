from collections import OrderedDict
from random import randint

favorite_languages = OrderedDict()

favorite_languages['jeb'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name,language in favorite_languages.items():
	print(name.title() + '最喜欢的语言是：' + language.title())

class Die():
	def __init__(self,sides=6):
		self.sides = sides

	def roll_die(self):
		return randint(1,self.sides)

die = Die()
results = []
for i in range(10):
	results.append(die.roll_die())
print(results)
