#! /usr/bin/env python

import abc

class CaffeineBeverageWithHook(object):
	__metaclass__ = abc.ABCMeta
	
	def prepareRecipe(self):
		self.boildWater()
		self.brew()
		self.pourInCup()
		if self.customerWantsCondiments():
			self.addCondiments()

	@abc.abstractmethod
	def brew(self):
		return

	@abc.abstractmethod
	def addCondiments(self):
		return

	def boildWater(self):
		print "boiling water"

	def pourInCup(self):
		print "pouring into cup"

	def customerWantsCondiments(self):
		return True

class CoffeeWithHook(CaffeineBeverageWithHook):
	def brew(self):
		print "dripping coffee through filter"

	def addCondiments(self):
		print "add sugar and milk"

	def customerWantsCondiments(self):
		print "Would you like milk and sugar with your coffee (y/n)?"

		answer = raw_input()
		if answer.lower()[0] == 'y':
			return True
		else: 
			return False
		
if __name__ == "__main__":
	coffeeHook = CoffeeWithHook()
	coffeeHook.prepareRecipe()
