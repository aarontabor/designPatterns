#!/usr/bin/python
'''
Flyweight Patern.
The concept of the flyweight design pattern is to share
object instances in circumstances where many objects 
would be needed and the overhead of having all of these
objects is unfeasible (think character objects in a word doc).
The flyweight pattern allows you to share similar instances.

To work, you must be able to seperate intrinsic and extrensic
attributes of the instances.  The intrinsic information can
be stored in the shared 'flyweight' object, while the extrensic
must be passed in as a 'context'.  From the word doc example,
the ASCII letter could be seen as intrinsic attribute (it will
be shared for all uses of that instance) while font and style 
could be seen as the extrensic context that would have to be passed
in as needed.

The Python type/class/instance system is an example of the flyweight
pattern.  Classes are actually objects in Python; objects that simply
know how to create other objects.  All of the intrinsic information about
the class is stored in the class object (ex. its name, its parent class ...)
while the instance specific 'context information' is passed into the constructor.

I will model the class/instance flyweight system in this example.
'''

from flyweightFactories import ClassFactory
from flyweightClasses import CatClass

def main():
  classFactory = ClassFactory()

  catClass = classFactory.getFlyweight(CatClass)

  fluffyCat = catClass.new('fluffy')
  sleekCat = catClass.new('sleek')

  fluffyCat.speak(fluffyCat) # python magic automatically hands in self as first arg
  sleekCat.speak(sleekCat)
  return


if __name__ == '__main__':
  main()
