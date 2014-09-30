#!/usr/bin/python
'''
Observer Pattern.

The observer pattern is used when you have a notify-subscribers type problem.
It is useful when updates in one object should propogate to many others. This
is done by having a central 'subject' object who can attach and detach 'observers'
that listen to it.  When the subject's state changes, it will notify all currently
attached observers.

In this example, I will model a system that can push notifications to multiple 
platforms (facebook, twitter, ...) when a new blog post is added to a catalog.
'''

from subjects import Catalog
from observers import NotifiesFacebook, NotifiesTwitter
def main():
  catalog = Catalog()

  print 'No notifications sent without attaching observers...'
  catalog.add('A blog post')

  print
  print 'Attaching observers...'
  catalog.attach(NotifiesFacebook(catalog))
  catalog.attach(NotifiesTwitter(catalog))

  print 'Adding another blog post...'
  catalog.add('Another blog post')
  

if __name__ == '__main__':
  main()
