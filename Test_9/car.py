class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0        #汽车里程

	def get_descriptive_name(self):      #汽车信息
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def get_raed_odometer(self):		#车走的里程数
		print('这辆车已经走了' +' ' + str(self.odometer_reading) + ' '  + '里程')

	def update_odometer(self,milleage):		#更新里程数
		if milleage >=self.odometer_reading:
			self.odometer_reading = milleage
		else:
			print('不能将里程表回调')

	def increment_odometer(self,milles):	#增加里程数
		self.odometer_reading += milles

# my_new_car = Car('audi','a4',2016)        #输出信息
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(23)			#更新里程并显示
# my_new_car.get_raed_odometer()
#
# my_new_car.increment_odometer(20)			#增加里程并显示
# my_new_car.get_raed_odometer()