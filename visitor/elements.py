#!/usr/bin/python

'''
The elements that will accept the visitors.
Notice that all of the visitors do not necessarily
have to extend the same parent class.  They must only implement the accept() function.

It is relatively hard to add new elements, all of the visitors will have be updated to 
carry out their task on this new element.
'''

class FarmAnimal:
  def greet(self):
    print 'Hi, Im a farm animal'

  def accept(self, visitor):
    pass


class Cow(FarmAnimal):
  def greet(self):
    print 'Moo! Im a cow'

  def accept(self, visitor):
    visitor.visitCow(self)


class Chicken(FarmAnimal):
  def greet(self):
    print 'Buck buck, Im a chicken'

  def accept(self, visitor):
    visitor.visitChicken(self)


class Tractor:
  def greet(self):
    print 'Chug-a-chug-a, Im a tractor'

  def accept(self, visitor):
    visitor.visitTractor(self)

