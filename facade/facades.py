#!/usr/bin/python
'''
Facades

A simple, unified way for a client to perform
basic interactions with all of the components
of the Car subsystem.  Although flexibility is
lost, these default operations are what most
users will be doing.
'''

from subComponents import Ignition, SteeringWheel, GasPedal, Brakes, SignalLights

class CarFacade(object):
  def __init__(self):
    self.ignition = Ignition()
    self.steeringWheel = SteeringWheel()
    self.gasPedal = GasPedal()
    self.brakes = Brakes()
    self.signalLights = SignalLights()

  def drive(self):
    self.ignition.turnOn()
    self.gasPedal.accelerate()

  def turnLeft(self):
    self.signalLights.signalLeft()
    self.steeringWheel.turn(-90)

  def stop(self):
    self.brakes.decelerate()
    self.ignition.turnOff()

