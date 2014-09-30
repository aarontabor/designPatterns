#!/usr/bin/python
'''
SubComponents

A complex(ish) subsystem that defines how a
car can be interacted with
'''

class Ignition(object):
  def turnOn(self):
    print 'turning key to on...'

  def turnOff(self):
    print 'turning key to off...'

class SteeringWheel(object):
  def turn(self, degrees):
    print 'turning steering wheel %d degrees...' % degrees

class GasPedal(object):
  def accelerate(self):
    print 'applying gas, speeding up...'

class Brakes(object):
  def decelerate(self):
    print 'applying brakes, slowing down...'

class SignalLights(object):
  def signalLeft(self):
    print 'signaling for a left turn...'

  def signalRight(self):
    print 'signaling for a right turn...'
