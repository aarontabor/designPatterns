#!/usr/bin/python
'''
Adapter Pattern.

The adapter pattern is meant to allow a class or object that must adhere
to a given interface (the client) to make use of an existing class which does not adhere (the adaptee).
The adapter will implement the client's interface using the adaptee's.

There are 2 type of adapter:

  Class Adapter:
    Adapts by using multiple inheritance

    Benefit: Can modify the adaptees functionality
    Downside: Can not directly make use of subclasses of adaptee

  Instance Adapter:
    Adapts by delegating to an instance of the adaptee

    Benefit: Can make use of subclasses of adaptee to add more functionality
    Downside: Can not directly override functionality in adaptee class

'''

from adapters import BreadOven, PizzaOvenAdapter, CookieOvenAdapter
from cookieAPI import ChocolateChipCookieAPI

def main():
  print 'class adapter...'
  oven = PizzaOvenAdapter()
  print oven.cook()

  print 'instance adapter...'
  oven = CookieOvenAdapter(ChocolateChipCookieAPI)
  print oven.cook()


if __name__ == '__main__':
  main()



