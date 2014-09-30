#!/usr/bin/python
'''
Observers
'''

class Observer(object):
  def __init__(self, subject):
    self.subject = subject

  def update(self):
    pass


class CatalogObserver(Observer):
  def __init__(self, subject):
    super(CatalogObserver, self).__init__(subject)
    self.posts = []

class NotifiesFacebook(CatalogObserver):
  def update(self):
    self.posts = self.subject.posts
    print 'Facebook: Newest post -- %s' % self.posts[-1]

class NotifiesTwitter(CatalogObserver):
  def update(self):
    self.posts = self.subject.posts
    print 'Twitter: Newest post -- %s' % self.posts[-1]
