# -*- coding: utf-8 -*-
# big-step semantics

import sys,os
sys.path.append(os.path.abspath('../../'))
from definitions import *


class Number(Number):
  def evaluate(self, environment):
    return self


class Boolean(Boolean):
  def evaluate(self, environment):
    return self


class Variable(Variable):
  def evaluate(self, environment):
    return environment[self.name]


class Add(Add):
  def evaluate(self, environment):
    return Number(self.left.evaluate(environment).value + self.right.evaluate(environment).value)


class Multiply(Multiply):
  def evaluate(self, environment):
    return Number(self.left.evaluate(environment).value * self.right.evaluate(environment).value)


class LessThan(LessThan):
  def evaluate(self, environment):
    return Boolean(self.left.evaluate(environment).value < self.right.evaluate(environment).value)


class DoNothing(DoNothing):
  def evaluate(environment):
    return environment


class Assign(Assign):
  def evaluate(self, environment):
    return dict(environment.items() + [(self.name, self.expression.evaluate(environment))])


class If(If):
  def evaluate(self, environment):
    cond = self.condition.evaluate(environment)
    if cond == Boolean(True):
      return self.consequence.evaluate(environment)
    elif cond == Boolean(False):
      return self.alternative.evaluate(environment)


class Sequence(Sequence):
  def evaluate(self, environment):
    return self.second.evaluate(self.first.evaluate(environment))


class While(While):
  def evaluate(self, environment):
    cond = self.condition.evaluate(environment)
    if cond == Boolean(True):
      return self.evaluate(self.body.evaluate(environment))
    elif cond == Boolean(False):
      return environment
