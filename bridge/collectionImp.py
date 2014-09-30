#!/usr/bin/python

class CollectionImp:

  def add(): pass
  def delete(): pass
  def contais(): pass


class ListCollectionImp(CollectionImp):
  def __init__(self):
    self.collection = []

  def add(self, item):
    print 'In list.add'
    self.collection.extend([item])

  def delete(self, item):
    print 'In list.delete'
    self.collection.remove(item)

  def contains(self, item):
    print 'In list.contains'
    return item in self.collection


class DictCollectionImp(CollectionImp):
  def __init__(self):
    self.collection = {}

  def add(self, item):
    print 'In dict.add'
    self.collection[item] = True

  def delete(self, item):
    print 'In dict.delete'
    if self.contains(item):
      del(self.collection[item])

  def contains(self, item):
    print 'In dict.contains'
    if self.collection.get(item):
      return True
    else:
      return False
