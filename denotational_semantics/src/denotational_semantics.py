# -*- coding: utf-8 -*-
# denotational semantics

import sys,os
sys.path.append(os.path.abspath('../../'))
from definitions import *


class Number(Number):
  def to_py(self):
    return 'lambda e: {}'.format(self.value)


class Boolean(Boolean):
  def to_py(self):
    return 'lambda e: {}'.format(self.value)


class Variable(Variable):
  def to_py(self):
    return "lambda e: e['{}']".format(self.name)


class Add(Add):
  def to_py(self):
    return 'lambda e: ({})(e) + ({})(e)' \
    .format(self.left.to_py(), self.right.to_py())


class Multiply(Multiply):
  def to_py(self):
    return 'lambda e: ({left})(e) * ({right})(e)' \
    .format(left=self.left.to_py(), right=self.right.to_py())


class LessThan(LessThan):
  def to_py(self):
    return 'lambda e: ({left})(e) < ({right})(e)' \
    .format(left=self.left.to_py(), right=self.right.to_py())


class DoNothing(DoNothing):
  def to_py(self):
    return 'lambda e: e'


class Assign(Assign):
  def to_py(self):
    return "lambda e: dict(e.items() + [('{name}', ({exp})(e))])" \
    .format(name=self.name, exp=self.expression.to_py())


class If(If):
  def to_py(self):
    return 'lambda e: ({cons})(e) if ({cond})(e) else ({alt})(e)' \
    .format(cons=consequence.to_py, cond=condition.to_py, alt=alternative.to_py)


class Sequence(Sequence):
  def to_py(self):
    return 'lambda e: ({second})(({first})(e))' \
    .format(first=self.first.to_py(), second=self.secont.to_py())


class While(While):
  def to_py(self):
    return 'lambda e: inline_while({cond}, {body}, e)' \
    .format(cond=self.condition.to_py(), body=self.body.to_py())


def inline_while(cond, body, e):
  while cond(e):
    e = body(e)
  return e
