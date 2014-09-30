#!/usr/bin/python

class PrototypeFactory:
  def __init__(self, prototype):
    self.prototype = prototype

  def make(self):
    return self.prototype.clone()
