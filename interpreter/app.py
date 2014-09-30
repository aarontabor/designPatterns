#!/usr/bin/python
'''
Interpreter Pattern.

This pattern allows us to respresent simple grammers used to solve problems
using objects.  Examples of this are the Apache Struts 'Criteria' objects and
Regular Expressions.  Each non-terminal of the grammer is represented by a class
that knows how to 'interpret' itself on a context.

In this example, I will demonstrate using using a criteria system that can filter
results from a list of objects based on their attributes.
'''

from cats import Cat
from criteria import Criteria, OrCriteria, AndCriteria, NotCriteria

def main():
  cats = [
      Cat('Princess', 'Fluffy', 'White'), 
      Cat('Daisy', 'Smooth', 'White'), 
      Cat('Bo', 'Smooth', 'Black'),
  ]

  print 'finding cats who are Daisy || Fluffy...'
  criteria = OrCriteria(Criteria('name', 'Daisy'), Criteria('furType', 'Fluffy'))
  print criteria.find(cats)

  print
  print 'finding cats who are Smooth && Black ...'
  criteria = AndCriteria(Criteria('furType', 'Smooth'), Criteria('color', 'Black'))
  print criteria.find(cats)

  print
  print 'finding cats who are ! Princess ...'
  criteria = NotCriteria(Criteria('name', 'Princess'))
  print criteria.find(cats)


if __name__ == '__main__':
  main()

