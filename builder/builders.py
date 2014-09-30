#!/usr/bin/python

'''
Builders
These builders know how to construct cars.  I am using the same code from the factory example on purpose.
Builders and factories are very similar.  The main difference is that the concrete factories know how to
create widgets of the same family and return those widgets immediately, builders keep the state of the object.
The caller gets the end product by calling 'getProduct()' on the builder.

The implications of this are that the caller must know the internal structure of the widgets when using a concrete
factory, but can ignore this knowledge when using a builder.  The builder allows the caller to simply interact with the created product
through it's defined interface after retrieving it from the builder.

The downside to this is that our builders store state, meaning that the order in which the methods are called can matter, i.e. we must create a car
before creating tires or engine.
'''

from widgets import *

class CarBuilder:
  def __init__(self):
    self.car = None

  def buildCar(self):
    pass

  def buildTires(self):
    pass

  def buildEngine(self):
    pass

  def buildPaintJob(self):
    pass

  def getProduct(self):
    return self.car


class SportsCarBuilder(CarBuilder):
  def buildCar(self):
    self.car = SportsCar()

  def buildTires(self):
    self.car.tires = SportyTires()

  def buildEngine(self):
    self.car.engine = RacingEngine()

  def buildPaintJob(self):
    self.car.paintJob = HotPaintJob()


class ClunkerCarBuilder(CarBuilder):
  def buildCar(self):
    self.car = ClunkerCar()

  def buildTires(self):
    self.car.tires = OldTires()

  def buildEngine(self):
    self.car.engine = OldEngine()

  def buildPaintJob(self):
    self.car.paintJob = OldPaintJob()

