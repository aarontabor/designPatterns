#!/usr/bin/python

'''
Demonstration of the Visitor pattern
Each element knows how to accept visitors (telling them to perform their
element-specific version of the task).  Each visitor knows how to perform its
task on each of the various elements types.

The idea of the Visitor pattern is to encapsulate all task related activities
in a visitor class.  This is useful when you want to perform a task on many different
types of elements, without spreading the knowledge of that task over many classes.
This will also help reduce interface bloat.  In our example, the cow doesn't have to know
it can be fed and cleaned.  Subsequently, this makes it very easy to add a new task: We
simply must add a new concrete visitor that shares a common interface with the abstract visitor.

This pattern makes it more difficult to add a concrete element type.  Doing so would require us
to add functionality to each of the Visitor classes.
'''

from elements import Cow, Chicken, Tractor
from visitors import FeederVisitor, CleanerVisitor

def feed(thing, feeder):
  thing.accept(feeder)

def clean(thing, cleaner):
  thing.accept(cleaner)


def main():
  things = [Cow(), Chicken(), Tractor()]

  feeder = FeederVisitor()
  cleaner = CleanerVisitor()

  for thing in things:
    thing.greet()
    feed(thing, feeder)
    clean(thing, cleaner)
    print '\n'

  print 'Done!'


if __name__ == '__main__':
  main()
