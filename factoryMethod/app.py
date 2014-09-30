#!/usr/bin/python

'''
The factory method is essentially the core functionality encapsulated in the AbstractFactory.
The difference is that by definition, the Abstract Factory is a class whose sole responsibility is to
create Products.  A factory method, however, can be added to any class that instantiates another object.
The factory method removes the hard coding of the class to instantiate, allowing subclasses to change it,
modifying behavior.
'''

from sundaeMachines import HotFudgeSundaeMachine, BananaSplitSundaeMachine

# notice that in the abstract factory example, we had a 'build' function
# defined. This was because the Abstract Factories do not include this functionality
# In this example, we will build IceCreamSundaeMachines that implement factory methods.

def main():
  print 'Making hot fudge sundae...'
  icsMachine = HotFudgeSundaeMachine()
  sundae = icsMachine.createSundae()
  sundae.describe()

  print 'Making banana split...'
  icsMachine = BananaSplitSundaeMachine()
  sundae = icsMachine.createSundae()
  sundae.describe()
  return


if __name__ == '__main__':
  main()
