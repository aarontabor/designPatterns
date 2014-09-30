#!/usr/bin/python
'''
Widgets.
'''

class Widget(object):
  def __init__(self, mediator):
    self.mediator = mediator

  def changed(self):
    # this could be accomplished using the Observer pattern
    self.mediator.widgetChanged(self)

class Tap(Widget):
  def __init__(self, mediator):
    super(Tap, self).__init__(mediator)
    self.on = False

  def turnOn(self):
    self.on = True
    print 'tap: On'
    self.changed()

  def turnOff(self):
    self.on = False
    print 'tap: Off'
    self.changed()

class Spout(Widget):
  def __init__(self, mediator):
    super(Spout, self).__init__(mediator)
    self.flowing = False

  def isFlowing(self):
    return self.flowing
