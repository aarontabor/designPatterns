#!/usr/bin/python

'''
The vistors to be passed to concrete elements.  Each visitor class
encapsulates a certain task, and knows how to preform it on each of the concrete
types. i.e. Feeder knows how to feed Cows, Chickens, and Tractors.

It is relatively easy to add a new task: simply add a new visitor who knows 
how to carry out their task on each concrete element.
'''

class Visitor:
  def visitCow(self, cow):
    pass

  def visitChicken(self, chicken):
    pass

  def visitTractor(self, tractor):
    pass

class FeederVisitor(Visitor):
  def visitCow(self, cow):
    print 'Feeding Cow: Giving him oats.'
    
  def visitChicken(self, chicken):
    print 'Feeding Chicken: Giving him some seeds.'
    
  def visitTractor(self, tractor):
    print 'Feeding Tractor: Filling it up with gas.'
    

class CleanerVisitor(Visitor):
  def visitCow(self, cow):
    print 'Cleaning Cow: Shoveling poop, collecting milk.'
    
  def visitChicken(self, chicken):
    print 'Cleaning Chicken: Fixing nest, collection eggs.'
    
  def visitTractor(self, tractor):
    print 'Cleaning Tractor: Washing tires, shining rims.'
    
