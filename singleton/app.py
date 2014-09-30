#!/usr/bin/python

'''
Singleton Pattern.
The concept here is to have only one instance of an object (ex. a connection manager).
Concept:
  private constructor
  public static instance(method)

'''

from singleton import Singleton, SpecializedSingleton

def main():
  instance = Singleton.instance()
  print type(instance)
  instance = SpecializedSingleton.instance()
  print type(instance)
  return


if __name__ == '__main__':
  main()
