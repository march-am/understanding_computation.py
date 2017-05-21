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

