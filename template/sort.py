#! /usr/bin/env python
import abc

#this is insertion sort
def mysort(src, des, low, high, off):
	for i in range(low+1, high):
		for j in range(i, low, -1):
			if des[j-1].compareTo(des[j]) > 0:
				swap(des, j, j-1)
				j -= 1
def swap(des, i , j):
	temp = des[i]
	des[i] = des[j]
	des[j] = temp

class Comparable(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def compareTo(obj):
		return

class Duck(Comparable):
	def __init__(self, name, weight):
		self.name = name
		self.weight =weight

	def compareTo(self, duck):
		if self.weight < duck.weight:
			return -1
		elif self.weight == duck.weight:
			return 0
		else:
			return 1
	def __repr__(self):
		return self.name

if __name__ == "__main__":
	ducks = [Duck("daffy", 8), Duck("dewey", 2), Duck("howard", 7), Duck("louie", 2), Duck("huey", 2), Duck("donald", 10)]
	mysort(ducks, ducks, 0, len(ducks), 0)

	print ducks
