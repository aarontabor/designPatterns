#!/usr/bin/python

'''
This is a demonstration of the builder pattern.  The idea behind the builder pattern
is to allow the creation of complex objects in incremental steps by providing 'builders'
that know how assemble object parts that work together.  Because the builders all
extend a common parent, we can build our object by specifying generic opbect parts 
to be built, and configure the concrete parts by using different builder classes.

The Builder pattern hides the internal structure of the complex object from the caller by
keeping an internal state and building the object incrementally.  The caller gets the
finished object by calling 'getProduct()'

In this example we will create a Sports Car and an Old Clunker car with the builder pattern.


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

from builders import SportsCarBuilder, ClunkerCarBuilder



def build(carBuilder):
  print 'building body...'
  carBuilder.buildCar()
  print 'building tires...'
  carBuilder.buildTires()
  print 'building engine...'
  carBuilder.buildEngine()
  print 'building paint job...'
  carBuilder.buildPaintJob()
  print 'car complete!'
  return carBuilder.getProduct()


def main():
  builder = SportsCarBuilder()

  print 'building a sports car...'
  car = build(builder)
  print car.describe()

  print ''

  builder = ClunkerCarBuilder()
  print 'building a clunker car...'
  car = build(builder)
  print car.describe()
  return


if __name__ == '__main__':
  main()
