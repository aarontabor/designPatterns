#!/usr/bin/python

'''
This is a demonstration of the iterator pattern.  I've defined two maps, one that uses a
dict internally, another that uses 2 aligned lists.  They inherit from the Map class, whose
iterator method simply returns a NoneIterator (always returns None).  The iterator pattern
gives us a way to iterate over the elements of each map, without needing knowledge of their
internal structure.  We can simply use the iterators interface.
'''

from maps import Map, DictMap, WackyMap

def main():
  print 'Creating an "abstract" map...'
  m = Map()
  i = m.iterator()
  while i.hasNext():
    print i.getNext()

  print 'Creating a dict map...'
  m = DictMap()
  m.add(1, 'hello')
  m.add(2, 'goodbye')
  i = m.iterator()
  while i.hasNext():
    print i.getNext()

  print 'Creating a wacky map...'
  m = WackyMap()
  m.add(1, 'hello')
  m.add(2, 'goodbye')
  print 'iterating forwards...'
  i = m.iterator()
  while i.hasNext():
    print i.getNext()

  print 'iterating backwards...'
  i = m.reverseIterator()
  while i.hasNext():
    print i.getNext()


if __name__ == '__main__':
  main()

