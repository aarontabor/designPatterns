#!/usr/bin/python

'''
Command.

The idea of the Command pattern is to separate the decision to perform an action from 
the implementation details. Commands also separate the invoker of the action from the
reciever.  This allows us to have things like context sensitive buttons, etc. Command pattern
is essentially the object oriented version of a callback function, with added benefit (history,
state, ...).  The history (undo/redo) can be accomplished by having a list into which a snapshot
of the command is put when executed (the snapshot is required because the state of command
could changeover time).

The example given in the book is in a text editor, Commands could be paste, save, quit, etc.
These commands could be executed by clicking a menu item, clicking a short cut or a keybinding.

Encapsulating the implementation in a Command object allows us to separate the method of invocation (menu item, button, keybinding)
from the implementation.

I will demonstate with an app that will decide on behavior from command line options
'''

import sys
from command import SaveCommand, ZipCommand, AllMacroCommand
def main():
  args = sys.argv
  if len(args) < 2:
    print "usage: [-s | -a] | [-z <filename = current doc>]"
    sys.exit(1)

  args = args[1:]

  command = None
  if args[0] == '-s':
    command = SaveCommand()

  elif args[0] == '-z':
    if len(args) > 1:
      documentName = args[1]
      command = ZipCommand(documentName)
    else:
      command = ZipCommand()

  elif args[0] == '-a':
    command = AllMacroCommand()

  else:
    print 'unknown option'
    sys.exit(1)

  command.execute()
  return


if __name__ == '__main__':
  main()
