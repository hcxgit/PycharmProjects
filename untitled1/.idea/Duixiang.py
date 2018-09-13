#coding:utf-8
class Vehicle:
	def __init__(self,speed):
		self.speed = speed

	def drive(self,distance):
		print '需要%f小时'%(distance/self.speed)

class Bike(Vehicle):
	pass

class Car(Vehicle):
	def __init__(self,speed,fuel):
		Vehicle.__init__(self,speed)
		self.fuel = fuel
	def drive(self,distance):
		Vehicle.drive(self,distance)
		print '需要%f油'%(distance*self.fuel)

b = Bike(15.0)
c = Car(80.0,0.012)
b.drive(100.0)
c.drive(100.0)