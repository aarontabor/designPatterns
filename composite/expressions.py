#!/usr/bin/python
'''
expressions.py
'''

class Expression:
  def __init__(self, data):
    self.data = data

  def add(self, elem):
    raise(CannotAddToPrimitiveError)

  def show(self):
    print self.data,


class NumberElement(Expression):
  pass

class SymbolElement(Expression):
  pass

class Composite(Expression):
  def __init__(self):
    self.elements = []

  def add(self, elem):
    # it is important to append, not extend
    # we want to keep nesting
    self.elements.append(elem)

  def show(self):
    print '(',
    for elem in self.elements:
      elem.show()
    print ')',


class CannotAddToPrimitiveError(Exception):
  pass
