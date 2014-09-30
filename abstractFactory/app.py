#!/usr/bin/python

'''
This is a demonstration of the abstract factory pattern.
The abstract factory provides an interface to make all of the
required 'widgits' for a paticular item.  Each concrete factory
will implement this interface, taking care of the exact widget
needed for that concrete implementation.  This allows us to 
ask for widgets by their generic name, and depending on the factory
we use, we will get different concrete 'widgits'. Factories ensure that
all of the components of an object will be compatible.

In this example we will create a Sports Car and an Old Clunker car with Factories,
simply by asking for generic car parts from the SportsCarFactory and ClunkerCarFactory

--------------------------------------------------
Abstract Factories and Builders are very similar.  

I have used basically the same code idea for both  examples.
The key difference is that Abstract factories take care of the details about compatibility and uniformity between components of
an object.  By asking a factory to create all of the object parts we need, we can be sure that the parts will be uniform and compatible. It is, however,
still left up to the caller to assemble these parts in the correct order.  This means that as the caller, we must know the internal structure of the object we are creating.
i.e. we must know that the wheels are an element of a car.

The Builder still ensures that all of the individual parts of an object are compatible and uniform, but it hides the internal structure of the object from us.  The builder stores the state
of the object we are building, and we do not get this object until we explicitly ask the Builder for it by calling 'getProduct()'.  This allows us to simply communicate with the product through
its public interface. We need not know any internal details of it's structure. The downside (potentially) is that, because the Builder stores state, the order in which its methods are called could matter. i.e. we must build the car before we can build the tires.

In short, the Factory pattern leaves the knowledge of the product's internal structure with the caller, while the Builder pattern encapsulates this knowledge, leaving the caller unaware of the products internals.
--------------------------------------------------
'''

from factories import SportsCarFactory, ClunkerCarFactory



def build(carFactory):
  print 'constructing body...'
  car = carFactory.makeCar()
  print 'adding tires...'
  car.tires = carFactory.makeTires()
  print 'adding engine...'
  car.engine = carFactory.makeEngine()
  print 'adding paint job...'
  car.paintJob = carFactory.makePaintJob()
  print 'car complete!'
  return car


def main():
  factory = SportsCarFactory()

  print 'building a sports car...'
  car = build(factory)
  print car.describe()

  print ''

  factory = ClunkerCarFactory()
  print 'building a clunker car...'
  car = build(factory)
  print car.describe()
  return


if __name__ == '__main__':
  main()
