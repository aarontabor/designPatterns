#!/usr/bin/python
'''
Mediator.

This behavioral pattern applies when many objects of a subsystem interact in two way communication.
This sort of communication typically leads to a highly coupled subsystem; objects know about
most of the other objects.  To reduce the coupling, we can introduce a mediator (or director).
This objects job is essentially to orchestrate the communication.  All protocol specific logic is
stored in the mediator, leaving the other objects with the simple job of communication with only the mediator.

In this example, I'll create a water sink subsystem, with a Tap and a Spout.  The mediator will take care of the
interaction between them, making them less coupled and hence more reusable.
'''

from mediators import SinkMediator

def main():
  mediator = SinkMediator()
  tap, spout = mediator.widgets()

  print 'is the water flowing? %s' % spout.isFlowing()

  print 
  print 'turning tap on...'
  tap.turnOn()
  print 'is the water flowing? %s' % spout.isFlowing()

  print
  print 'turning tap off...'
  tap.turnOff()
  print 'is the water flowing? %s' % spout.isFlowing()


if __name__ == '__main__':
  main()
