#!/usr/bin/python

'''
Widgets to be built up by our builders
A car needs tires, an engine, and a paint job. Our builders will be
able to create racecars and clunkercars
'''

class Car(object):
  def __init__(self):
    self.tires = None
    self.engine = None
    self.paintJob = None
    self.carType = 'Regular Car'

  def describe(self):
    return 'This is a %s. Specs:\nTires: %s\nEngine: %s\nPaintJob: %s' % \
        (self.carType,\
        self.tires.describe(),\
        self.engine.describe(),\
        self.paintJob.describe())

class SportsCar(Car):
  def __init__(self):
    super(SportsCar, self).__init__()
    self.carType = 'Sporty Whip'

class ClunkerCar(Car):
  def __init__(self):
    super(ClunkerCar, self).__init__()
    self.carType = 'Old Jalopy'


class Tires:
  def describe(self):
    return 'Plain tires'

class SportyTires(Tires):
  def describe(self):
    return 'Fast Tires'

class OldTires(Tires):
  def describe(self):
    return 'Flat Tires'


class Engine:
  def describe(self):
    return 'Standard Engine'

class RacingEngine(Engine):
  def describe(self):
    return 'V8 Engine with 900 HP'

class OldEngine(Engine):
  def describe(self):
    return 'Similar to that on a lawn-mower'


class PaintJob:
  def describe(self):
    return 'Standard Paint Job'

class HotPaintJob(PaintJob):
  def describe(self):
    return 'Racing Stripes'

class OldPaintJob(PaintJob):
  def describe(self):
    return 'Rust Spots'

