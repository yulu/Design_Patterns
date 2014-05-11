#! /usr/bin/env python

import abc

class State(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def insertQuarter(self):
		return	
	
	@abc.abstractmethod
	def ejectQuarter(self):
		return

	@abc.abstractmethod
	def turnCrank(self):
		return

	@abc.abstractmethod
	def dispense(self):
		return

class NoQuarterState(State):
	def __init__(self, gumballMachine):
		self.gumballMachine = gumballMachine

	def insertQuarter(self):
		print "You inserted a quarter"
		self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

	def ejectQuarter(self):
		print "You haven't inserted a quarter"

	def turnCrank(self):
		print "You turned, but there's no quarter"

	def dispense(self):
		print "You need to pay first"

class HasQuarterState(State):
	def __init__(self, gumballMachine):
		self.gumballMachine = gumballMachine

	def insertQuarter(self):
		print "You can't insert another quarter"

	def ejectQuarter(self):
		print "Quarter returned"
		self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

	def turnCrank(self):
		print "You turned"
		self.gumballMachine.setState(self.gumballMachine.getSoldState())

	def dispense(self):
		print "No gumball dispensed"


class SoldState(State):
	def __init__(self, gumballMachine):
		self.gumballMachine = gumballMachine

	def insertQuarter(self):
		print "Please wait, we're already giving you a gumball"

	def ejectQuarter(self):
		print "Sorry, you already turned the crank"

	def turnCrank(self):
		print "Turning twice doesn't get you another gumball"

	def dispense(self):
		self.gumballMachine.releaseBall()

		if self.gumballMachine.getCount > 0:
			self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
		else:
			print "Oops, out of gumballs"
			self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

class SoldOutState(State):
	def __init__(self, gumballMachine):
		self.gumballMachine = gumballMachine

	def insertQuarter(self):
		print "not accepted, since we are run out of gumball"

	def ejectQuarter(self):
		print "no quarter inserted"

	def turnCrank(self):
		print "You turned the crank, but there's no quarter inserted"
	
	def dispense(self):
		print "Nothing to dispense"

class GumballMachine(object):
	def __init__(self, numberGumballs):
		self.noQuarterState = NoQuarterState(self)
		self.hasQuarterState = HasQuarterState(self)
		self.soldState = SoldState(self)
		self.soldOutState = SoldOutState(self)

		self.count = numberGumballs
		if numberGumballs > 0:
			self.state = self.noQuarterState
		else:
			self.state = self.soldOutState

	def insertQuarter(self):
		self.state.insertQuarter()
	
	def ejectQuarter(self):
		self.state.ejectQuarter()

	def turnCrank(self):
		self.state.turnCrank()
		self.state.dispense()

	def setState(self, state):
		self.state = state

	#getters
	def getCount(self):
		return self.count

	def getNoQuarterState(self):
		return self.noQuarterState

	def getHasQuarterState(self):
		return self.hasQuarterState
	
	def getSoldState(self):
		return self.soldState

	def getSoldOutState(self):
		return self.soldOutState

	def releaseBall(self):
		print "A gumball comes rolling out the slot..."
		if not self.count == 0:
			self.count = self.count - 1

if __name__ == '__main__':
	gumballMachine = GumballMachine(10)

	gumballMachine.insertQuarter()
	gumballMachine.turnCrank()

	gumballMachine.turnCrank()
