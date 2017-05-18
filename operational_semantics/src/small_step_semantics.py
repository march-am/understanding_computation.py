# -*- coding: utf-8 -*-
# small-step semantics

import sys,os
sys.path.append(os.path.abspath('../../'))
from definitions import *


class Number(Number):
  def reducible(self):
    return False


class Add(Add):
  def reducible(self):
    return True

  def reduce_exp(self, environment):
    if self.left.reducible():
      return Add(self.left.reduce_exp(environment), self.right)
    elif self.right.reducible():
      return Add(self.left, self.right.reduce_exp(environment))
    else:
      return Number(self.left.value + self.right.value)


class Multiply(Multiply):
  def reducible(self):
    return True

  def reduce_exp(self, environment):
    if self.left.reducible():
      return Add(self.left.reduce_exp(environment), self.right)
    elif self.right.reducible():
      return Add(self.left, self.right.reduce_exp(environment))
    else:
      return Number(self.left.value * self.right.value)


class Boolean(Boolean):
  def reducible(self):
    return False


class LessThan(LessThan):
  def reducible(self):
    return True

  def reduce_exp(self, environment):
    if self.left.reducible():
      return LessThan(self.left.reduce_exp(environment), self.right)
    elif self.right.reducible():
      return LessThan(self.left, self.right.reduce_exp(environment))
    else:
      return Boolean(self.left.value < self.right.value)


class Variable(Variable):
  def reducible(self):
    return True

  def reduce_exp(self, environment):
    return environment[self.name]


class DoNothing(DoNothing):
  def reducible(self):
    return False

  def __eq__(self, other):
    return isinstance(self, type(DoNothing()))


class Assign(Assign):
  def reducible(self):
    return True

  def reduce_exp(self, environment):
    if self.expression.reducible():
      return [Assign(self.name, self.expression.reduce_exp(environment)), environment]
    else:
      # updateすると元配列を破壊するのでdictコンストラクタで新しいdictを返す
      return [DoNothing(), dict(environment.items() + [(self.name, self.expression)])]


class If(If):
  def reducible(self):
    return True

  def reduce_exp(self, environment):
    if self.condition.reducible():
      return [If(self.condition.reduce_exp(environment), self.consequence, self.alternative), environment]
    else:
      if self.condition == Boolean(True):
        return [self.consequence, environment]
      elif self.condition == Boolean(False):
        return [self.alternative, environment]


class Sequence(Sequence):
  def reducible(self):
    return True

  def reduce_exp(self, environment):
    if self.first == DoNothing():
      return [self.second, environment]
    else:
      reduced_first, reduced_environment = self.first.reduce_exp(environment)
      return [Sequence(reduced_first, self.second), reduced_environment]


class While(While):
  def reducible(self):
    return True

  def reduce_exp(self, environment):
    return [If(self.condition, Sequence(self.body, self), DoNothing()), environment]


class Machine:
  def __init__(self, statement, environment):
    self.statement = statement
    self.environment = environment

  def step(self):
    self.statement, self.environment = self.statement.reduce_exp(self.environment)

  def run(self):
    while self.statement.reducible():
      print('{}, {}'.format(self.statement, self.environment))
      self.step()
    print('{}, {}'.format(self.statement, self.environment))
