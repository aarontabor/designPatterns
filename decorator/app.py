#!/usr/bin/python
'''
Decorator Pattern.
This structural pattern allows us to add functionality
to a component by wrapping it in a transparent wrapper.
This wrapper adheres to the same interface that the component
does, the client need not know if they are dealing with a bare component, or 
one wrapped in several decorators.  The decorator serves
to add functionality to the component, by executing it's
added functionality, and the delegating to the component.

When using the decorator pattern, it is ideal to have a
lightweight component (not many data fields), as each decorator will inherit all
of the data.  A heavy weight component could start making a difference with an
arbitrarily large number of decorator classes wrapping  it.

The decorator pattern and strategy pattern are comparable. The decorator can
be thought of as adding a 'skin' around a component.  The strategy pattern,
on the other hand, allows you to change the 'guts' of a component (it is also better
suited for a heavywieght component, as it need not inherit all attributes).

In this example, I will make a toy test running framework that allows the client
to add an arbitrary number of set-up and tear down callbacks transparently.
'''

from components import Test
from decorators import SetupDecorator, TeardownDecorator

def main():

  def testCallback():
    print 'running test...'
    return

  def setupCallback():
    print 'this is setup code...'
    return

  def teardownCallback():
    print 'this is teardown code...'
    return


  print 'bare test...'
  component = Test(testCallback)
  component.run()

  print
  print 'adding setup...'
  component = SetupDecorator(component, setupCallback)
  component.run()

  print 
  print 'adding teardown...'
  component = TeardownDecorator(component, teardownCallback)
  component.run()


if __name__ == '__main__':
  main()
