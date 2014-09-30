#!/usr/bin/python
'''
Handlers
'''

class NotHandledError(Exception):
  pass

class Handler(object):
  def __init__(self, nextHandler):
    self.nextHandler = nextHandler

  def handle(self, data):
    print 'Falling back to outer context...'
    if self.nextHandler:
      return self.nextHandler.handle(data)
    else:
      raise(NotHandledError)


class OsKeyHandler(Handler):
  def handle(self, keyCombination):
    print 'Handling %s in OS context...' % keyCombination

    # Note that these key -> action mappings could be moved into
    # a dictionary.  This would allow us to define mappings at runtime
    # by passing them into the constructor.  This would allow for much
    # greater flexibility.
    #
    # I have not done this here to keep the example simple

    if keyCombination == 'Three-Finger-Swipe':
      return 'Switching workspaces.'
    elif keyCombination == 'Super':
      return 'Spotlight Search.'
    else:
      return super(OsKeyHandler, self).handle(keyCombination)

class ApplicationKeyHandler(Handler):
  def handle(self, keyCombination):
    print 'Handling %s in Application context...' % keyCombination

    if keyCombination == 'Control-c':
      return 'Kill Application.'
    elif keyCombination == 'Two-Finger-Swipe':
      return 'Reposition Application Window.'
    else:
      return super(ApplicationKeyHandler, self).handle(keyCombination)

class SubcomponentKeyHandler(Handler):
  def handle(self, keyCombination):
    print 'Handling %s in Sub-component context...' % keyCombination

    if keyCombination == 'Control-c':
      return 'Copy Selected Text'
    elif keyCombination == 'Control-v':
      return 'Paste contents of Copy-Buffer.'
    else:
      return super(SubcomponentKeyHandler, self).handle(keyCombination)
