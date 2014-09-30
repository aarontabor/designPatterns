#!/usr/bin/python
'''
Adapters.py
'''

from externalAPI import ExternalPizzaAPI
class Oven(object):
  def cook(self):
    pass


class BreadOven(Oven):
  def cook(self):
    return 'baking bread...'


class PizzaOvenAdapter(Oven, ExternalPizzaAPI):
  def cook(self):
    return self.warmPizzaStones() +\
      self.putPizzaIn() +\
      self.takePizzaOut()


  def warmPizzaStones(self):
    return 'notice I can override functionality...'


class CookieOvenAdapter(Oven):
  def __init__(self, cookieAPI):
    # this could really be done with a factory or something?
    self.cookieAPI = cookieAPI()
    super(CookieOvenAdapter, self).__init__()

  def cook(self):
    return self.cookieAPI.heatOven() +\
    self.cookieAPI.cookCookies()


