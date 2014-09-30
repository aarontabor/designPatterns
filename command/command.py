#!/usr/bin/python

class Command(object):
  def execute(self):
    pass


class SaveCommand(Command):
  def execute(self):
    # Notice we can let the command take care of the reciever (staticly bind)
    print 'Saving current Document'


class ZipCommand(Command):
  # Or have it be configurable (dynamically bind)
  def __init__(self, filename='current Document', *args, **kwargs):
    self.filename = filename
    super(ZipCommand, self).__init__(*args, **kwargs)

  def execute(self):
    print 'Zipping %s' % self.filename



class MacroCommand:
  def __init__(self, commands):
    self.commands = commands

  def execute(self):
    for command in self.commands:
      command.execute()


class AllMacroCommand(MacroCommand):
  def __init__(self):
    self.commands = [SaveCommand(), ZipCommand()]

