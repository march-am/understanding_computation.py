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

  def reduce_exp(self, environment):
    if self.left.reducible:
      return Add(self.left.reduce_exp(environment), self.right)
    elif self.right.reducible:
      return Add(self.left, self.right.reduce_exp(environment))
    else:
      return Number(self.left.value + self.right.value)


class Multiply(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right
    self.reducible = True

  def str(self):
    return '{} * {}'.format(self.left.str(), self.right.str())

  def reduce_exp(self, environment):
    if self.left.reducible:
      return Add(self.left.reduce_exp(environment), self.right)
    elif self.right.reducible:
      return Add(self.left, self.right.reduce_exp(environment))
    else:
      return Number(self.left.value * self.right.value)


class Boolean(Expression):
  def __init__(self, value):
    self.value = value
    self.reducible = False

  def str(self):
    return str(self.value)


class LessThan(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right
    self.reducible = True

  def str(self):
    return '{} < {}'.format(self.left.str(), self.right.str())

  def reduce_exp(self, environment):
    if self.left.reducible:
      return LessThan(self.left.reduce_exp(environment), self.right)
    elif self.right.reducible:
      return LessThan(self.left, self.right.reduce_exp(environment))
    else:
      return Boolean(self.left.value < self.right.value)


class Variable(Expression):
  def __init__(self, name):
    self.name = name
    self.reducible = True

  def str(self):
    return str(self.name)

  def reduce_exp(self, environment):
    return environment[self.name]


class Machine:
  def __init__(self, expression, environment):
    self.expression = expression
    self.environment = environment

  def step(self):
    self.expression = self.expression.reduce_exp(self.environment)

  def run(self):
    while self.expression.reducible:
      print(self.expression)
      self.step()
    print(self.expression)
