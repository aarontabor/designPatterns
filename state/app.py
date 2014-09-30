#!/usr/bin/python
'''
State Pattern.

The state pattern applies when an object's behavior should change based on it's current state.
Flags for this include long conditional statements or switch-cases within method definitions. This
pattern moves the 'state specific' behavior into newly defined state classes, which the original
(called the 'context' object) will delegate to.  

The state operations may also be required to change the state of the context.  This can be accomplished
in at least 2 ways:
  have the context in charge of state transitions (the method that invokes the state object will also
  change the state)

  allow the state objects to take care of transitions (this increases coupling between them. the context
  must be passed in as a param)


In this example, I will demonstrate how the state pattern could apply to a drawing editor.  Imagine that
the user can select a drawing tool from a tool bar, and then by clicking within the drawing area, the user
invokes the tools draw() method. ( TODO: This example does not demonstrate implicit state transitions)
'''

from context import DrawingTool
from states import PencilState, EraserState, RectangleState

def main():
  tool = DrawingTool()

  print 'User selects a pencil...'
  tool.setState(PencilState())
  tool.draw()

  print
  print 'User selects an eraser...'
  tool.setState(EraserState())
  tool.draw()

  print
  print 'User selects rectangle tool...'
  tool.setState(RectangleState())
  tool.draw()


if __name__ == '__main__':
  main()
