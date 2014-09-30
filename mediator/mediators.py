#!/usr/bin/python
'''
Mediators.
'''

from widgets import Tap, Spout

class Mediator(object):
  def widgetChanged(self, widget):
    pass

class SinkMediator(Mediator):
  def __init__(self):
    self.tap = Tap(self)
    self.spout = Spout(self)

  def widgets(self):
    return (self.tap, self.spout)

  def widgetChanged(self, widget):
    # this is the meat of the logic
    if type(widget) is Tap:
      print 'mediator: recieved message from tap, updating spout.'
      self.spout.flowing = self.tap.on

    elif type(widget) is Spout:
      pass # spout doesn't currently affect anything

    else:
      print 'unrecognized widget'
