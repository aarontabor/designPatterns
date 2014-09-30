#!/usr/bin/python

'''
Factories.  
These factories know how to build all of the parts
we need to make cars. Furthermore, they will ensure
that we use parts that are 'compatible' with each other.

As long as we use the factory to create the parts we need,
we know that we are getting the parts for the same kind of car.

i.e. Our SportsCarFactory will give us all the parts we need to create
a Sports Car. We only need to ask for them by their generic names.  It is 
the factories job to keep track of which specific parts those are.
'''

from widgets import *

class CarFactory:
  def makeCar(self):
    pass

  def makeTires(self):
    pass

  def makeEngine(self):
    pass

  def makePaintJob(self):
    pass


class SportsCarFactory:
  def makeCar(self):
    return SportsCar()

  def makeTires(self):
    return SportyTires()

  def makeEngine(self):
    return RacingEngine()

  def makePaintJob(self):
    return HotPaintJob()


class ClunkerCarFactory:
  def makeCar(self):
    return ClunkerCar()

  def makeTires(self):
    return OldTires()

  def makeEngine(self):
    return OldEngine()

  def makePaintJob(self):
    return OldPaintJob()
