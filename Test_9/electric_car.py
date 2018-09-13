from car import Car

class Battery():
	def __init__(self,battery_size=70):    # 这个 = 旁边不用加空格
		self.battery_size = battery_size 	  #电瓶容量

	def describe_battery(self):
		print('电瓶的容量是:' + str(self.battery_size))

	def get_range(self):					#根据电瓶容量来报告汽车续航里程
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = '这辆车可以续航' + str(range) +'里程'
		print(message)

	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
			print('升级电池容量为85')
		else:
			print('已经升级过了')
class ElectricCar(Car):  		#电动车
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()

my_ElectricCar = ElectricCar('速派奇','小型',2017)
print(my_ElectricCar.get_descriptive_name())
my_ElectricCar.battery.describe_battery()
my_ElectricCar.battery.upgrade_battery()
my_ElectricCar.battery.describe_battery()

my_tesla = ElectricCar('tesla','model s',2017)
print(my_tesla.get_descriptive_name())
my_tesla.battery.battery_size = 85
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()