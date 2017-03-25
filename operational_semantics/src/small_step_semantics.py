# -*- coding: utf-8 -*-
#small-step semantics

class Expression:
  def __str__(self):
    return '«{}»'.format(self.str())

  def __repr__(self):
    return '«{}»'.format(self.str())


class Number(Expression):
  def __init__(self, value):
    self.value = value
    self.reducible = False

  def str(self):
    return str(self.value)


class Add(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right
    self.reducible = True

  def str(self):
    return '{} + {}'.format(self.left.str(), self.right.str())

  def reduce_exp(self):
    if self.left.reducible:
      return Add(self.left.reduce_exp(), self.right)
    elif self.right.reducible:
      return Add(self.left, self.right.reduce_exp())
    else:
      return Number(self.left.value + self.right.value)


class Multiply(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right
    self.reducible = True

  def str(self):
    return '{} * {}'.format(self.left.str(), self.right.str())

  def reduce_exp(self):
    if self.left.reducible:
      return Add(self.left.reduce_exp(), self.right)
    elif self.right.reducible:
      return Add(self.left, self.right.reduce_exp())
    else:
      return Number(self.left.value * self.right.value)
