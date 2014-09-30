#!/usr/bin/python

class CookieAPI():
  def heatOven(self):
    return 'heating cookie oven...'

  def cookCookies(self):
    return 'cooking cookies...'


class ChocolateChipCookieAPI(CookieAPI):
  def cookCookies(self):
    return 'cooking CHOCOLATE-CHIP cookies(notice we overroode functionality through subclassing)...'

