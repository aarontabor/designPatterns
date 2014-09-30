#!/usr/bin/python

class Iterator:
  def getNext(self):
    pass

  def hasNext(self):
    pass

  def current(self):
    pass
  

class NoneIterator(Iterator):
  def getNext(self):
    return None

  def hasNext(self):
    return False

  def current(self):
    return None


class DictIterator(Iterator):
  def __init__(self, dictMap):
    self.dictMap = dictMap
    self.cur = -1

  def getNext(self):
    self.cur += 1
    return self.current()

  def hasNext(self):
    # notice that this could be simplified by augmenting the Map
    # interface with things like '__len__', 'keys', 'vals', ...
    return self.cur < len(self.dictMap.map) - 1

  def current(self):
    keys = self.dictMap.map.keys()
    currentKey = keys[self.cur]
    return self.dictMap.map[currentKey]


class WackyDictIterator(DictIterator):
  def __init__(self, wackyMap):
    self.wackyMap = wackyMap
    self.cur = -1

  def getNext(self):
    self.cur += 1
    return self.current()

  def hasNext(self):
    return self.cur < len(self.wackyMap.keys) - 1

  def current(self):
    return self.wackyMap.vals[self.cur]


class WackyDictReverseIterator(WackyDictIterator):
  def __init__(self, wackyMap):
    self.wackyMap = wackyMap
    self.cur = len(wackyMap.keys)

  def getNext(self):
    self.cur -= 1
    return self.current()

  def hasNext(self):
    return self.cur > 0
