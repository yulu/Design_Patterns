class OutdoorLight(object):
	def on(self):
		print "Outdoor Light on"
	def off(self):
		print "Outdoor Light off"

class GardenLight(object):
	def setDuskTime(self):
		print "Garden Light set dusk time"
	def setDawnTime(self):
		print "Garden Light set dawn time"
	def manualOn(self):
		print "Garden Light manual on"
	def manualOff(self):
		print "Garden Light manual off"

class CeilingFan(object):
	def high(self):
		print "Ceiling Fan high"
	def medium(self):
		print "Ceiling Fan medium"
	def low(self):
		print "Ceiling Fan low"
	def off(self):
		print "Ceiling Fan off"

class GarageDoor(object):
	def up(self):
		print "Garage Door up"
	def down(self):
		print "Garage Door down"
	def stop(self):
		print "Garage Door stop"

class Stereo(object):
	def on(self):
		print "Stereo on"
	def off(self):
		print "Stereo off"
	def setCd(self):
		print "Stereo set CD"
	def setRadio(self):
		print "Stereo set radio"


