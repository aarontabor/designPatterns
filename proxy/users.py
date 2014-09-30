#!/usr/bin/python
'''
Users
'''

class AbstractUser(object):
  def getId(self): pass
  def getName(self): pass
  def getData(self): pass


class User(AbstractUser):
  def __init__(self, _id, name):
    self._id = _id
    self.name = name
    self.data = 'copious amounts of data'

  def getId(self):
    return self._id

  def getName(self):
    return self.name

  def getData(self):
    return self.data
  

class UserProxy(AbstractUser):
  def __init__(self, _id):
    self.user = None
    self._id = _id

  def getId(self):
    return self._id

  def getName(self):
    if not self.loaded():
      self.load()
    return self.user.getName()

  def getData(self):
    if not self.loaded():
      self.load()
    return self.user.getData()

  def loaded(self):
    return self.user is not None

  def load(self):
    self.user = UserFinder().load(self._id)


class UserFinder:

  class NotFoundError(Exception): pass

  def __init__(self):
    # would actually set up a db connection
    self.users = {
        1: User(1, 'Stewart'),
        2: User(2, 'George')
    }

  def find(self, id): # for fast response
    if id in self.users:
      return UserProxy(id)
    else:
      raise(NotFoundError)


  def load(self, id): # load data as requested
    print 'loading all user information...'
    if id in self.users:
      return self.users[id]
    else:
      raise(NotFoundError)

class UserFinder:

  class NotFoundError(Exception): pass

  def __init__(self):
    # would actually set up a db connection
    self.users = {
        1: User(1, 'Stewart'),
        2: User(2, 'George')
    }

  def find(self, id): # for fast response
    if id in self.users:
      return UserProxy(id)
    else:
      raise(NotFoundError)


  def load(self, id): # load data as requested
    print 'loading all user information...'
    if id in self.users:
      return self.users[id]
    else:
      raise(NotFoundError)

