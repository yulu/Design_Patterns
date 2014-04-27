#! /usr/bin/env python

def is_even(value):
	'''Return true if *value* is even'''
	return (value %2) == 0

def count_occurrences(target_list, predicate):
	'''Return the number of times applying the callable *predicate* to a 
	list element return True.'''
	return sum([1 for e in target_list if predicate(e)])

def surround_with(surrounding):
	'''Return a function that takes a single argument and.'''
	def surround_with_value(word):
		return '{}{}{}'.format(surrounding, word, surrounding)
	return surround_with_value

def transform_words(content, targets, transform):
	'''Return a string based on *content* but with each occurrence
	of words in *target* replaced with the result of applying *transform* to it'''
	result = ''
	for word in content.split():
		if word in targets:
			result += ' {}'.format(transform(word))
		else:
			result += ' {}'.format(word)

	return result

class Product(object):
	
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def price_with_tax(self, tax_rate_percentage):
		return self.price * (1 + (tax_rate_percentage * .01))
'''
how the decorator is defined
the general approach is to use the wrapper function with arbitary input parameters as follows
'''
def currency(f):
	def wrapper(*args, **kwargs):
		return '$' + str(f(*args, **kwargs))
	return wrapper

class Product_deco():
	def __init__(self, name, price):
		self.name = name
		self.price = price

	@currency #here the decorator is called
	def price_with_tax(self, tax_rate_percentage):
		return self.price * (1 + (tax_rate_percentage * 0.01))


p = Product("a book", 18.0)
print p.price_with_tax(7)

p_deco = Product_deco("another book", 18.0)
print p_deco.price_with_tax(7)
