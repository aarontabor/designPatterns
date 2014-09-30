#!/usr/bin/python

'''
Prototype pattern.
This creational pattern is similar to an Abstract Factory.  The difference is that we do not subclass the Factory,
instead initialize the factorty with objects (the prototypes), and then the factory will clone these objects whenever we ask for a new instance.
The magic 'cloning' must be implemented by each of the prototypes themselves. The factory simply calls the clone method.

Our example will use a single type of PrototypeFactory to make a whole breakfast.
'''

from prototypeFactory import PrototypeFactory
from prototypes import Bacon, Eggs, Toast

def main():
  print 'making bacon...'
  protoFac = PrototypeFactory(Bacon())
  prototype = protoFac.make()
  print prototype.describe()

  print 'making eggs...'
  protoFac = PrototypeFactory(Eggs())
  prototype = protoFac.make()
  print prototype.describe()

  print 'making toast...'
  protoFac = PrototypeFactory(Toast())
  prototype = protoFac.make()
  print prototype.describe()
  return 

if __name__ == '__main__':
  main()
