#!/usr/bin/python
'''
Subjects
'''

class Subject(object):
  def __init__(self):
    self.observers = []

  def attach(self, observer):
    self.observers.append(observer)

  def detach(self, observer):
    if observer in self.observers:
      self.observers.remove(observer)

  def notify(self):
    for observer in self.observers:
      observer.update()

class Catalog(Subject):
  def __init__(self):
    super(Catalog, self).__init__()
    self.posts = []

  def add(self, blogPost):
    print 'Adding "%s" to catalog.' % blogPost
    self.posts.append(blogPost)
    self.notify()
