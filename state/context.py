#!/usr/bin/python
'''
The contexts
'''
class DrawingTool():

  def __init__(self):
    self.state = None

  def setState(self, state):
    self.state = state

  def draw(self):
    if self.state:
      self.state.draw()
    else:
      raise(NoStateDefinedError)


class NoStateDefinedError(Exception):
  pass


