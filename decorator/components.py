#!/usr/bin/python
'''
Components
'''

class Component(object):
  def run(self):
    pass

class Test(Component):
  def __init__(self, testCallback):
    super(Component, self).__init__()
    self.testCallback = testCallback

  def run(self):
    self.testCallback()
