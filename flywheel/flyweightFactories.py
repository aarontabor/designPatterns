#!/usr/bin/python
'''
Flyweight Factories
'''

class ClassFactory:
  def __init__(self):
    self.classes = {}

  def getFlyweight(self, a_class):
    if a_class not in self.classes:
      # the flyweight instance
      self.classes[a_class] = a_class()

    return self.classes[a_class]

