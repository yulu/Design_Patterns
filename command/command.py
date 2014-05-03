#! /usr/bin/env python

import abc
from vendor import *

class Command(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def execute(self):
		return
	@abc.abstractmethod
	def undo(self):
		return

class noCommand(Command):
	def execute(self):
		return
	def undo(self):
		return

class LightOnCommand(Command):
	def __init__(self, light):
		self.light = light

	def execute(self):
		self.light.on()
	def undo(self):
		self.light.off() #undo is just turn off the light

class LightOffCommand(Command):
	def __init__(self, light):
		self.light = light
	def execute(self):
		self.light.off()
	def undo(self):
		self.light.on()

class StereoOnWithCDCommand(Command):
	def __init__(self, stereo):
		self.stereo = stereo

	def execute(self):
		self.stereo.on()
		self.stereo.setCd()
		self.stereo.setRadio()
	def undo(self):
		return

class StereoOffCommand(Command):
	def __init__(self, stereo):
		self.stereo = stereo
	
	def execute(self):
		self.stereo.off()
	def undo(self):
		return


class GarageDoorUpCommand(Command):
	def __init__(self, garagedoor):
		self.garagedoor = garagedoor
	
	def execute(self):
		self.garagedoor.up()
	def undo(self):
		return


class GarageDoorDownCommand(Command):
	def __init__(self, garagedoor):
		self.garagedoor = garagedoor
	
	def execute(self):
		self.garagedoor.down()
	def undo(self):
		return


class CeilingFanHighCommand(Command):
	def __init__(self, ceilingfan):
		self.ceilingfan = ceilingfan

	def execute(self):
		self.ceilingfan.high()
	def undo(self):
		return



class CeilingFanOffCommand(Command):
	def __init__(self, ceilingfan):
		self.ceilingfan = ceilingfan

	def execute(self):
		self.ceilingfan.off()
	def undo(self):
		return

class MacroCommand(Command):
	def __init__(self, commandList):
		self.commandList = commandList

	def execute(self):
		for k in self.commandList:
			k.execute()

	def undo(self):
		return

class RemoteControl(object):
	def __init__(self):
		self.onCommands = []
		self.offCommands = []
		noComm = noCommand()
		for i in range(0,7):
			self.onCommands.append(noComm)
			self.offCommands.append(noComm)
		self.undoCommand = noComm

	def setCommand(self, slot, onCommand, offCommand):
		self.onCommands[slot] = onCommand
		self.offCommands[slot] = offCommand

	def onButtonWasPressed(self, slot):
		self.onCommands[slot].execute()
		self.undoCommand = self.onCommands[slot]

	def offButtonWasPressed(self, slot):
		self.offCommands[slot].execute()
		self.undoCommand = self.offCommands[slot]

	def undoButtonWasPressed(self):
		self.undoCommand.undo()
	def display(self):
		for k in self.onCommands:
			print "[", self.onCommands.index(k), "]", k
		for k in self.offCommands:
			print "[", self.offCommands.index(k), "]", k

if __name__ == "__main__":

	#all the receivers (devices)
	light = OutdoorLight()
	gardenLight = GardenLight()
	ceilingFan = CeilingFan()
	garageDoor = GarageDoor()
	stereo = Stereo()

	#all the command
	lightOnCommand = LightOnCommand(light)
	lightOffCommand = LightOffCommand(light)
	
	stereoOnWithCDCommand = StereoOnWithCDCommand(stereo)
	stereoOffCommand = StereoOffCommand(stereo)

	garageDoorUpCommand = GarageDoorUpCommand(garageDoor)
	garageDoorDownCommand = GarageDoorDownCommand(garageDoor)

	ceilingFanHighCommand = CeilingFanHighCommand(ceilingFan)
	ceilingFanOffCommand = CeilingFanOffCommand(ceilingFan)

	macroCommand = MacroCommand([lightOffCommand, stereoOnWithCDCommand, ceilingFanHighCommand])

	#set the remote control
	remote = RemoteControl()
	remote.setCommand(0, lightOnCommand, lightOffCommand)
	remote.setCommand(1, stereoOnWithCDCommand, stereoOffCommand)
	remote.setCommand(2, garageDoorUpCommand, garageDoorDownCommand)
	remote.setCommand(3, ceilingFanHighCommand, ceilingFanOffCommand)
	remote.setCommand(4, macroCommand, macroCommand)

	remote.display()

	print "test buttons"

	remote.onButtonWasPressed(0)
	remote.offButtonWasPressed(0)
	remote.undoButtonWasPressed()
	remote.onButtonWasPressed(1)
	remote.offButtonWasPressed(1)
	remote.onButtonWasPressed(2)
	remote.offButtonWasPressed(2)
	remote.onButtonWasPressed(3)	
	remote.offButtonWasPressed(3)	

	print "party mode"
	remote.onButtonWasPressed(4)
