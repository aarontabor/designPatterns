#!/usr/bin/python
'''
Criteria.

These classes allow the user to create an abstract syntax tree roughly
modelling the following grammer rules:

criteria  := and | or | not | terminal
and       := criteria & criteria
or        := criteria | criteria
not       := ! criteria
terminal  := attribute => value

Since we can always treat the 'composite' structure as a criteria, we
can have an arbitrarily deep tree, and still have a simple calling syntax.
'''

class Criteria(object):
  def __init__(self, attr, value):
    self.attr = attr
    self.value = value

  def find(self, aList):
    return [ 
        element 
        for element in aList 
        if element.__getattribute__(self.attr) == self.value 
    ]


class OrCriteria(Criteria):
  def __init__(self, thisCriteria, thatCriteria):
    self.thisCriteria = thisCriteria
    self.thatCriteria = thatCriteria

  def find(self, aList):
    thisSet = set(self.thisCriteria.find(aList))
    thatSet = set(self.thatCriteria.find(aList))
    return list(thisSet | thatSet)


class AndCriteria(Criteria):
  def __init__(self, thisCriteria, thatCriteria):
    self.thisCriteria = thisCriteria
    self.thatCriteria = thatCriteria

  def find(self, aList):
    thisSet = set(self.thisCriteria.find(aList))
    thatSet = set(self.thatCriteria.find(aList))
    return list(thisSet & thatSet)


class NotCriteria(Criteria):
  def __init__(self, criteria):
    self.criteria = criteria

  def find(self, aList):
    criteriaSet = set(self.criteria.find(aList))
    listSet = set(aList)
    return list(listSet - criteriaSet)


