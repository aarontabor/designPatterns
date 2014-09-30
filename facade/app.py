#!/usr/bin/python
'''
Facade Pattern.

The purpose of this pattern is to provide a simplified interface to
a more complex subsystem.  It will tie the subsystem components together,
and provide a default set of functionality that the majority of clients
will use.  The facade may reduce the flexibility of usage, but if needed, the
clint can still access the components individually.

Facades can be used as a simplified interface between subsystem-client relationships,
but also between subsystem-subsystem relationships.  The latter creates subsystems that
are more modular, and hence should be more reusable (easier to plug-and-play).

A facade can also be extended several ways. One way is through inheritance: subclasses
of the facade can provide different default sets of functionality.  Another way is to
allow the Facade to be given instances of the components it should use (similar to a prototype
or builder).  Functionality can then be customized through subclasses of the components.
'''

from facades import CarFacade

def main():
  car = CarFacade()
  print 'Going for a drive:'
  car.drive()
  print
  print 'Turning left:'
  car.turnLeft()
  print
  print 'Stopping:'
  car.stop()



if __name__ == '__main__':
  main()
