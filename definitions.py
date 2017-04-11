# -*- coding: utf-8 -*-
# Class definitions

class Expression:
  def __str__(self):
    return '«{}»'.format(self.str())
  def __repr__(self):
    return '«{}»'.format(self.str())
  def __eq__(self, other):
    if other is None or type(self) != type(other): return False
    return self.__dict__ == other.__dict__


class Statement(Expression):
  pass


class Number(Expression):
  def __init__(self, value):
    self.value = value

  def str(self):
    return str(self.value)


class Boolean(Expression):
  def __init__(self, value):
    self.value = value

  def str(self):
    return str(self.value)


class Variable(Expression):
  def __init__(self, name):
    self.name = name

  def str(self):
    return str(self.name)


class Add(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def str(self):
    return '{} + {}'.format(self.left.str(), self.right.str())


class Multiply(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def str(self):
    return '{} * {}'.format(self.left.str(), self.right.str())


class LessThan(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def str(self):
    return '{} < {}'.format(self.left.str(), self.right.str())


class DoNothing(Statement):
  def __eq__(self, other):
    if other is None or type(self) != type(other): return False

  def str(self):
    return 'Do-Nothing'


class Assign(Statement):
  def __init__(self, name, expression):
    self.name = name
    self.expression = expression

  def str(self):
    return '{} = {}'.format(self.name, self.expression.str())


class If(Statement):
  def __init__(self, condition, consequence, alternative):
    self.condition = condition
    self.consequence = consequence
    self.alternative = alternative

  def str(self):
    return 'If ({}) {{ {} }} else {{ {} }}'.format(self.condition.str(), self.consequence.str(), self.alternative.str())


class Sequence(Statement):
  def __init__(self, first, second):
    self.first = first
    self.second = second

  def str(self):
    return '{}; {}'.format(self.first.str(), self.second.str())


class While(Statement):
  def __init__(self, condition, body):
    self.condition = condition
    self.body = body

  def str(self):
    return 'While ({}) {{ {} }}'.format(self.condition.str(), self.body.str())
