# -*- coding: utf-8 -*-
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        long_name = self.restaurant_name + '做的是' + self.cuisine
        return long_name

    def open_restaurant(self):
        print('餐馆正在营业')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment_number):
        self.number_served += increment_number


class IceCreamStand(Restaurant):  # 冰淇淋餐馆
    def __init__(self, restaurant_name, cuisine_type='甜品'):
        super.__init__(restaurant_name, cuisine_type)
        self.flavors = []  # 存储各种口味冰淇淋组成的列表

    def show_iceCream(self):
        print('这些冰淇淋有：')
        for flaovr in self.flavors:
            print('-' + ' ' + flaovr)


iceCreamStand = IceCreamStand('C')
iceCreamStand.flavors = ['草莓味', '芒果味']
iceCreamStand.show_iceCream()

restaurant = Restaurant('A', '四川菜')
restaurant.set_number_served(4)
print ('餐馆就餐人数为：' + str(restaurant.number_served))
restaurant.increment_number_served(2)
print ('餐馆就餐人数为：' + str(restaurant.number_served))
