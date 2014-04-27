#! /usr/bin/env python

import abc

class PizzaStore(object):
	__metaclass__ = abc.ABCMeta

	def orderPizza(self, type):

		'''This is the trick:
		createPizza method is impelemented by the concrete 
		subclasses spesified to its type of product
		'''
		pizza = self.createPizza(type)

		'''here we actually work on different types of pizza alr
		depends on what type of pizza is created by the subclasses
		'''
		pizza.prepare()
		pizza.bake()
		pizza.cut()
		pizza.box()

		return pizza

	@abc.abstractmethod
	def createPizza(self, type):
		return

class NYPizzaStore(PizzaStore):
	def createPizza(self, type):
		if type == 'cheese':
			return NYStyleCheesePizza()

class ChicagoPizzaStore(PizzaStore):
	def createPizza(self, type):
		if type == 'cheese':
			return ChicagoStyleCheesePizza()

class Pizza(object):
	__metaclass__ = abc.ABCMeta

	name =""
	dough =""
	sauce = ""
	toppings =[]

	def prepare(self):
		print "Preparing ", self.name
		print "Tossing dough ..."
		print "Adding sauce ..."
		print "Adding toppings: ", 
		for i in self.toppings:
			print i, " ",
		print 

	def bake(self):
		print "Bake for 25 minutes at 350"

	def cut(self):
		print "Cutting the pizza into diagonal slices"

	def box(self):
		print "Place pizza in official PizzaStore box"

class NYStyleCheesePizza(Pizza):
	def __init__(self):
		self.name = "NY Style Sause and Cheese Pizza"
		self.dough = "Thin Crust Dough"
		self.sauce = "Marinara Sauce"

		self.toppings =["Grated Reggiano Cheese"]

class ChicagoStyleCheesePizza(Pizza):
	def __init__(self):
		self.name = "Chicago Style Deep Dish Cheese Pizza"
		self.dough = "Extra Thick Crust Dough"
		self.sauce = "Plum Tomato Sauce"

		self.toppings =["Shredded Mozzarella Cheese"]

	def cut(self):
		print "Cutting the pizza into square slices"


if __name__ == '__main__':
	nyStore = NYPizzaStore()
	chicagoStore = ChicagoPizzaStore()

	pizza = nyStore.orderPizza("cheese")
	print "Ethan ordered a " + pizza.name, "\n"

	pizza = chicagoStore.orderPizza("cheese")
	print "Joel ordered a " + pizza.name, 