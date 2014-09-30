#!/usr/bin/python
'''
Composite Pattern.

This structural pattern allows us to compose complex
tree structures out of primitives, treating a structure composed
of multiple primitives the same as a primitive.  This provides a transparent
interface to the client, regardless of whether they are dealing with a 
composite or a primitive.

This is implemented by giving both primitives and composites the
same interface, and the defining the composites operations in terms
of its primitives:

  composite.operation():
    for c in children:
      c.operation()

This example will show how mathematical expressions can be stored in this way
'''

from expressions import Composite, NumberElement, SymbolElement

def main():
  print 'a single element...'
  elem = NumberElement(2)
  elem.show()
  print

  print 'a simple expression...'
  expr = Composite()
  expr.add(NumberElement(5))
  expr.add(SymbolElement('+'))
  expr.add(NumberElement(4))
  expr.show()
  print

  print 'a more complex expression...'
  nestedExpr = expr
  expr = Composite()
  expr.add(NumberElement(9))
  expr.add(SymbolElement('-'))
  expr.add(nestedExpr)
  expr.show()
  print 

if __name__ == '__main__':
  main()


