#! /usr/bin/env python

import abc

'''
Creator abstract interfaces and its implementations
'''
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
		_ingridientFacotry = NYPizzaIngredientFactory()

		if type == 'cheese':
			pizza = CheesePizza(_ingridientFacotry)
			pizza.name = "New York Cheese Pizza"
		elif type == 'clam':
			pizza = ClamPizza(_ingridientFacotry)
			pizza.name = "Chicago Clam Pizza"

		return pizza

class ChicagoPizzaStore(PizzaStore):
	def createPizza(self, type):
		_ingridientFacotry = ChicagoPizzaIngredientFactory()

		if type == 'cheese':
			pizza = CheesePizza(_ingridientFacotry)
			pizza.name = "Chicago Cheese Pizza"
		elif type == 'clam':
			pizza = ClamPizza(_ingridientFacotry)
			pizza.name = "Chicago Clam Pizza"

		return pizza

'''
Product abstract class and concrete classes
'''
class Pizza(object):
	__metaclass__ = abc.ABCMeta

	name =""
	dough =""
	sauce = ""
	toppings =[]

	@abc.abstractmethod
	def prepare(self):
		return

	def bake(self):
		print "Bake for 25 minutes at 350"

	def cut(self):
		print "Cutting the pizza into diagonal slices"

	def box(self):
		print "Place pizza in official PizzaStore box"

class CheesePizza(Pizza):

	def __init__(self, IngridientFactory):
		self._ingridientFacotry = IngridientFactory

	def prepare(self):
		print "Preparing ", self.name
		self.dough = self._ingridientFacotry.createDough()
		self.sauce = self._ingridientFacotry.createSause()
		self.cheese = self._ingridientFacotry.createCheese()
		self.toppings = self._ingridientFacotry.createVeggies()

		print "dough: " ,self.dough
		print "sauce: " ,self.sauce
		print "cheese: " , self.cheese
		print "toppings: " , self.toppings

class ClamPizza(Pizza):
	def __init__(self, IngridientFactory):
		self._ingridientFacotry = IngridientFactory

	def prepare(self):
		print "Preparing ", self.name
		self.dough = self._ingridientFacotry.createDough()
		self.sauce = self._ingridientFacotry.createSause()
		self.cheese = self._ingridientFacotry.createCheese()
		self.toppings = self._ingridientFacotry.createVeggies()
		self.clam = self._ingridientFacotry.createClam()

		print "dough: " ,self.dough
		print "sauce: " ,self.sauce
		print "cheese: " , self.cheese
		print "toppings: " , self.toppings
		print "clam: " , self.clam


'''
abstract interface as abstract factory and its implementations~~~~~~~
'''
class PizzaIngredientFactory(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def createDough(self):
		return

	@abc.abstractmethod
	def createSause(self):
		return

	@abc.abstractmethod
	def createCheese(self):
		return

	@abc.abstractmethod
	def createVeggies(self):
		return 

	@abc.abstractmethod
	def createPepperoni(self):
		return

	@abc.abstractmethod
	def createClam(self):
		return

class NYPizzaIngredientFactory(PizzaIngredientFactory):
	def createDough(self):
		return "Thin Crust Dough"

	def createSause(self):
		return "Marinara Sauce"

	def createCheese(self):
		return "Reggiano Cheese"

	def createVeggies(self):
		return ["galic", "onino", "mushroom", "redpepper"]

	def createPepperoni(self):
		return "Sliced Pepperoni"

	def createClam(self):
		return "Fresh Clams"

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
	def createDough(self):
		return "Thick Crust Dough"

	def createSause(self):
		return "Plum Tomato Sauce"

	def createCheese(self):
		return "Mozzarella"

	def createVeggies(self):
		return ["eggplant", "black olives", "spinach"]

	def createPepperoni(self):
		return "Sliced Pepperoni"

	def createClam(self):
		return "Frozen Clams"


if __name__ == '__main__':
	nyStore = NYPizzaStore()
	chicagoStore = ChicagoPizzaStore()

	pizza = nyStore.orderPizza("cheese")
	print "Ethan ordered a " + pizza.name, "\n"

	pizza = chicagoStore.orderPizza("clam")
	print "Joel ordered a " + pizza.name, "\n"

	pizza = chicagoStore.orderPizza("cheese")
	print "I ordered a " + pizza.name, 