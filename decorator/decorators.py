#!/usr/bin/python
'''
Decorators
'''

from components import Component

class Decorator(Component):
  def __init__(self, component):
    super(Decorator, self).__init__()
    self.component = component

  def run(self):
    self.component.run()


class SetupDecorator(Decorator):
  def __init__(self, component, setupCallback):
    super(SetupDecorator, self).__init__(component)
    self.setupCallback = setupCallback

  def run(self):
    self.setupCallback()
    super(SetupDecorator, self).run()

class TeardownDecorator(Decorator):
  def __init__(self, component, teardownCallback):
    super(TeardownDecorator, self).__init__(component)
    self.teardownCallback = teardownCallback

  def run(self):
    super(TeardownDecorator, self).run()
    self.teardownCallback()

