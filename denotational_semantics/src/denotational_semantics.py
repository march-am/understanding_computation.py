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

