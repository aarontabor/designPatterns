#!/usr/bin/python
'''
Chain of Responsibility.

The Chain of Responsibility design pattern allows us to decouple the link between
an event and its handler. This is useful in a case where the event may occur in
one level of context, and we do not know which context will handle the event.
Using this pattern we can post-pone the decision until runtime.

Take for example a program that handles key combinations that may or may not
be bound to behavior in various contexts (In our example we consider, OS level, application
level...).  These key combinations may mean different actions in different contexts, or
may not have a meaning at all in a given context.  We solve this by making a chain of the
context specific handlers, letting the most specific handlers fall back on the more general.

At the context where the event occurs, the handler tries to handle the event.  If it can not,
it delegates to the next in line.

This is very much how exception handling is done in many programming languages.
'''

from handlers import \
    OsKeyHandler, ApplicationKeyHandler, SubcomponentKeyHandler

def main():
  osKeyHandler = OsKeyHandler(None)
  applicationKeyHandler = ApplicationKeyHandler(osKeyHandler)
  subcomponentKeyHandler = SubcomponentKeyHandler(applicationKeyHandler)

  print 'Performing Control-c:'
  print subcomponentKeyHandler.handle('Control-c')

  print
  print 'Performing Two-Finger-Swipe:'
  print subcomponentKeyHandler.handle('Two-Finger-Swipe')

  print
  print 'Performing Three-Finger-Swipe:'
  print subcomponentKeyHandler.handle('Three-Finger-Swipe')
  return
  
if __name__ == '__main__':
  main()
