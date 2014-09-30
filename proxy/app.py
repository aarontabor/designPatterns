#!/usr/bin/python
'''
Proxy Pattern

The proxy pattern allows us to get away without loading
large objects, especially all at startup.  Assume we had to
load a bunch of large images for a word doc.  This would take a long
time, and furthermore, most of them would not be seen at the same time anyway.
The proxy pattern allows us to load a place holder that holds minimal data (including where to find the real object) unitl
we need more data.  This is very similar to lazy init, and many databases uses this technique.

In this example. I model a database utility, that finds objects by id, but only loads proxys until we need more information.
'''

from users import UserFinder

def main():
  user = UserFinder().find(1)
  print 'Although we can treat it as a user, this is a user-proxy: %s' % type(user)
  print 'The proxy can store information...'
  print 'user.id: %s' % user.getId()
  print 'but then the proxies are populated as needed...'
  print 'user.name: %s' % user.getName()
  print 'user.data %s' % user.getData()
  return



if __name__ == '__main__':
  main()
