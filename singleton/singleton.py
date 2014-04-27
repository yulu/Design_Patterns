#! /usr/bin/env python

'''
A demo to define singleton class in python: from stackoverflow
'''

class Singleton:
	'''
	A non-thread-safe helper class to ease implementation singletons
	This should be used as a decorator -- not a metaclass -- to the class
	that should be a singleton
	
	The decorated class can define one '__init__' function that takes only
	the 'self' argument. Other than that, there are no restrictions that apply
	to the decorated class
	
	To get the singleton instance, use the 'Instance' method. Trying to use '__call__'
	will result in a 'TypeError' being raised

	Limitations: The decorated class cannot be inherited from

	Two class attributes:
	_decorated: the class that being wrapped
	_instance: the only object that being instantiated from the _decorated class.
	'''

	def __init__(self, decorated):
		self._decorated = decorated

	def Instance(self):
		'''
		Returns the singleton instance. Upon its first call, it creates a 
		new instance of the decorated class and calls its '__init__' method.
		On all subsequent calls, the already created instance is returned.
		'''
		try:
			return self._instance
		except AttributeError:
			self._instance = self._decorated()
			'''
			_decorated is a class that has been passed in to the wrapper
			_decorated() instantiates a object from the class, and assign it to
			_instance. For the first time Instance() is called, the instantiation 
			is performed. The following times, the only _instance will be returned
			'''
			return self._instance

	def __call__(self):
		raise TypeError('Singletons must be accessed through `Instance()`.')

if __name__ == '__main__':
	@Singleton
	class Foo:
		def __init__(self):
			print 'Foo created'

	#f = Foo() #Error, this isn't how you get the instance of a singleton

	f = Foo.Instance() #Good, Being explicit is in line with the Python zen
	g = Foo.Instance() #Returns already created instance

	print f is g #True
	
