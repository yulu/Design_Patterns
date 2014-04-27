#! /usr/bin/env python

import abc

#an abstract subject class
class Subject(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def registerObserver(self, o):
		return

	@abc.abstractmethod
	def removeObserver(self, o):
		return

	@abc.abstractmethod
	def notifyObservers(self):
		return

#an abstract observer class
class Observer(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def update(self, temp, humidity, pressure):
		return


#an abstract display class
class Display(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def display(self):
		return

#conceret class implements subject
class WeatherData(Subject):
	pressure = 80.0 #a default value

	def __init__(self):
		self.observers = [] #init a list to store all observers

	def registerObserver(self, o):
		self.observers.append(o)

	def removeObserver(self, o):
		self.observers.remove(o)

	def notifyObservers(self):
		for o in self.observers:
			o.update(self.temp, self.humidity, self.pressure)

	def measurementChanged(self):
		self.notifyObservers()

	def setMeasurements(self, temp, humidity, pressure):
		self.temp = temp
		self.humidity = humidity
		self.measurementChanged()

#concrete class implements observers and display
class CurrentConditionsDisplay(Observer, Display):
	def __init__(self, weatherData):
		self.weatherData = weatherData
		self.weatherData.registerObserver(self)
	
	def update(self, temp, humidity, pressure):
		self.temp = temp
		self.humidity = humidity
		self.pressure = pressure
		self.display()

	def display(self):
		print "Current conditions: ", self.temp, " F degrees and ", self.humidity, " % humidity"

#another concrete class implements observers and display
class AnotherConditionsDisplay(Observer, Display):
	def __init__(self, weatherData):
		self.weatherData = weatherData
		self.weatherData.registerObserver(self)
	
	def update(self,temp, humidity, pressure):
		self.temp = temp
		self.humidity = humidity
		self.pressure = pressure
		self.display()

	def display(self):
		print "Another conditions: ", self.pressure, " pressure data"		

if __name__ == '__main__':
	weatherData = WeatherData()

	currentDisplay = CurrentConditionsDisplay(weatherData)
	anotherDisplay = AnotherConditionsDisplay(weatherData)
	weatherData.setMeasurements(80, 65, 30.4)

	#remvoe the another from the subject, so it will on longer be notified.	
	weatherData.removeObserver(anotherDisplay)
	weatherData.setMeasurements(100, 20, 45.0)
	
