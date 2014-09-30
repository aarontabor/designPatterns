#!/usr/bin/python

'''
This is an example of the Bridge design pattern.  
The Bridge pattern sepates abstraction from implementation
by delegating the implementation specific details to an "Imp"lementor.

This allows an abstraction to change its implementation, simply by changing its linking.
Notice that although the abstraction delegates to the Implementation, their interfaces
not have to be identical.

In this example I will make a collection by using an implementation that uses a list, and then
with another implementation that uses a dictionary. (kind of sill, but fast look up)
'''

from collectionImp import ListCollectionImp, DictCollectionImp
from collection import Collection

def example(collection):
  print 'adding 1 to collection...'
  collection.add(1)
  print 'does collection contain 1?'
  collection.contains(1)
  print 'removing 1 from collection...'
  collection.remove(1)
  return

def main():
  print 'Creating a List-Implemented Collection...'
  collection = Collection(ListCollectionImp)
  example(collection)

  print 'Creating a Dict-Implemented Collection...'
  collection = Collection(DictCollectionImp)
  example(collection)

if __name__ == '__main__':
  main()
