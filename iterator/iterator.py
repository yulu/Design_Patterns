#! /usr/bin/env python

import abc

class Iterator(object):
	__classmeta__ = abc.ABCMeta

	@abc.abstractmethod
	def hasNext(self):
		return

	@abc.abstractmethod
	def next(self):
		return

	@abc.abstractmethod
	def remove(self):
		return

class DinerMenuIterator(Iterator):
	def __init__(self, items):
		self.items = items
		self.position = 0

	def hasNext(self):
		if self.position >= len(self.items) or self.items[self.position] == None:
			return False
		else:
			return True

	def next(self):
		item = self.items[self.position]
		self.position += 1
		return item

	def remove(self):


		if self.position <= 0:
			print "error"

		elif not self.items[self.position-1] == None:
			print self.position
			for i in range(self.position-1, len(self.items)-1):
				self.items[i] = self.items[i+1]

			self.position -= 1 #should we move the cursor one step forward??
			self.items[-1]=None	
			
class DinerMenu(object):
	def __init__(self):
		self.items = []
		self.items.append("bacon with lettuce")
		self.items.append("soup of the day")
		self.items.append("a hot dog")

	def createIterator(self):
		return DinerMenuIterator(self.items)

if __name__ == '__main__':

	menu = DinerMenu()
	ite = menu.createIterator()
	
#	while ite.hasNext():
#		print ite.next() 
	
	ite.next()
	ite.remove()
	
	while ite.hasNext():
		print ite.next()
