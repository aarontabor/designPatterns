#!/usr/bin/python

class State(object):
  def draw(self):
    pass

class PencilState(State):
  def draw(self):
    print 'drawing with pencil.'

class EraserState(State):
  def draw(self):
    print 'erasing with eraser.'

class RectangleState(State):
  def draw(self):
    print 'drawing a rectangle'
