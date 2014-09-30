#!/usr/bin/python
from iterator import Iterator, NoneIterator, DictIterator, WackyDictIterator, WackyDictReverseIterator

class Map:
  def iterator(self):
    return NoneIterator()
    pass

  def add(self, key, val):
    pass

  def drop(self, key):
    pass

  def contains(self, key):
    pass


class DictMap(Map):
  def __init__(self):
    self.map = {}
    
  def iterator(self):
    print "Here's a dict iterator ->"
    return DictIterator(self)

  def add(self, key, val):
    self.map[key] = val

  def drop(self, key):
    if self.map.get(key):
      del self.map[key]

  def contains(self, key):
    return key in self.map.keys()


class WackyMap(Map):
  def __init__(self):
    self.keys = []
    self.vals = []

  def iterator(self):
    print "Here's a wacky iterator ->"
    return WackyDictIterator(self)

  def reverseIterator(self):
    print "Here's a reverse wacky iterator ->"
    return WackyDictReverseIterator(self)

  def add(self, key, val):
    self.keys.append(key);
    self.vals.append(val);

  def drop(self, key):
    if key in self.keys:
      i = self.keys.index(key)
      del self.keys[i]
      del self.vals[i]

  def contains(self, key):
    return key in self.keys

