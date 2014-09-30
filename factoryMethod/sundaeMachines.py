#!/usr/bin/python

'''
Sundae Machines that implement factory methods

Notice how the 'createSundae()' method is only
defined in the parent class.  This is the whole
point of the factory methods. They let us dynamically
change the behavior of this method, through subclassing
'''

class Sundae:
  def __init__(self):
    self.iceCream = None
    self.sauce = None
    self.topping = None

  def describe(self):
    print 'IceCream: %s\nSauce: %s\nTopping: %s' %\
        (self.iceCream, self.sauce, self.topping)


class SundaeMachine:

  def createSundae(self):
    sundae = Sundae()
    # calling factory methods, notice how we do not have to hard code the assignment
    sundae.iceCream = self.doMakeIceCream()
    sundae.sauce = self.doMakeSauce()
    sundae.topping = self.doMakeTopping()
    return sundae


  def doMakeIceCream(self):
    pass

  def doMakeSauce(self):
    pass

  def doMakeTopping(self):
    pass

class HotFudgeSundaeMachine(SundaeMachine):

  # because we used factory methods, we can override behavior here
  def doMakeIceCream(self):
    return 'Vanilla'

  def doMakeSauce(self):
    return 'Hot Fudge'

  def doMakeTopping(self):
    return 'Cherry'


class BananaSplitSundaeMachine(SundaeMachine):

  # and here
  def doMakeIceCream(self):
    return 'Neopoliton'

  def doMakeSauce(self):
    return 'Strawberry'

  def doMakeTopping(self):
    return 'Banana and Coconut'
