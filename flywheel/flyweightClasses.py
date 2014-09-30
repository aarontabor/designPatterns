#!/usr/bin/python
'''
Flyweight Classes
'''

class CatClass(object):
  def __init__(self):
    # intrinsic information
    self.class_type = 'CatClass'

  def new(self, fur): # the context information is passed in (fur)
    '''
    The CatClass knows how to build CatInstances
    '''
    catInstance = CatInstance()
    catInstance.fur = fur

    def speakMethod(self):
      print 'I am a %s cat. I am an instance of %s.' % (self.fur, self.class_type)
    catInstance.speak = speakMethod

    return catInstance


class CatInstance(CatClass):
  pass
