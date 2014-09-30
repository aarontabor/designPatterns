#!/usr/bin/python

class Singleton:

  _instance = None

  @classmethod
  def instance(cls):
    if not cls._instance:
      cls._instance = cls.makeSingleton()
    return cls._instance

  @staticmethod
  def makeSingleton():
    return Singleton()

class SpecializedSingleton(Singleton):

  @staticmethod
  def makeSingleton():
    return SpecializedSingleton()
