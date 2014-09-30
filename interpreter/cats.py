#!/usr/bin/python
'''
Cats.
'''

class Cat(object):
  def __init__(self, name, furType, color):
    self.name = name
    self.furType = furType
    self.color = color

  def __repr__(self):
    return '%s %s %s' % (self.furType, self.color, self.name)

  def __str__(self):
    return '%s %s %s' % (self.furType, self.color, self.name)

