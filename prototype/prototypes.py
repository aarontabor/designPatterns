#!/usr/bin/python

class Prototype:
  def clone(self):
    pass

  def describe(self):
    pass

class Bacon(Prototype):
  def clone(self):
    # note -> does this have to be cast to a prototype?
    # is this even a thing in python?
    return Bacon()

  def describe(self):
    return 'Crispy Bacon'

class Eggs(Prototype):
  def clone(self):
    #note -> if an object had state, we would replicate that here.
    # ex:
    #   newEggs = Eggs()
    #   newEggs.style = self.style
    #   return newEggs

    return Eggs()

  def describe(self):
    return 'Eggs over-easy'

class Toast(Prototype):
  def clone(self):
    return Toast()

  def describe(self):
    return 'Whole Grain Toast'
