#! /usr/bin/env python

import abc

#an abstract class as Beverage
class Beverage(object):
	__metaclass__ = abc.ABCMeta

	description = "Unknown Beverage"

	def getDescription(self):
		return self.description

	@abc.abstractmethod
	def cost(self):
		return

#an abstract class as decorator
class CondimentDecorator(Beverage):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def getDescription(self):
		return

#concrete class for espresso
class Espresso(Beverage):
	def __init__(self):
		self.description = "Espresso"

	def cost(self):
		return 1.99

#concrete class for HouseBlend
class HouseBlend(Beverage):
	def __init__(self):
		self.description = "House Blend Coffee"

	def cost(self):
		return 0.89

#concrete decorator for Mocha
class Mocha(CondimentDecorator):
	def __init__(self, beverage):
		self.beverage = beverage

	def getDescription(self):
		return self.beverage.getDescription() + ", Mocha"

	def cost(self):
		return 0.20 + self.beverage.cost()

#concrete decorator for Soy
class Soy(CondimentDecorator):
	def __init__(self, beverage):
		self.beverage = beverage

	def getDescription(self):
		return self.beverage.getDescription() + ", Soy"

	def cost(self):
		return 0.15 + self.beverage.cost()

#concrete decorator for whip
class Whip(CondimentDecorator):
	def __init__(self, beverage):
		self.beverage = beverage

	def getDescription(self):
		return self.beverage.getDescription() + ", Whip"

	def cost(self):
		return 0.10 + self.beverage.cost()


if __name__ == '__main__':
	beverage = Espresso()
	print beverage.getDescription() + " $", beverage.cost()

	beverage2 = HouseBlend()
	beverage2 = Mocha(beverage2)
	beverage2 = Mocha(beverage2)
	beverage2 = Whip(beverage2)
	print beverage2.getDescription() + " $", beverage2.cost()

	beverage3 = Espresso()
	beverage3 = Soy(beverage3)
	print beverage3.getDescription() + " $", beverage3.cost()
