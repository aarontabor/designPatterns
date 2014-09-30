#!/usr/bin/python
'''
Abstract Interface for our collections
'''


class Collection:
  def __init__(self, imp):
    self.imp = imp()

  def add(self, item):
    self.imp.add(item)

  def remove(self, item):
    # notice that the interfaces do not have to align
    self.imp.delete(item)

  def contains(self, item):
    return self.imp.contains(item)



