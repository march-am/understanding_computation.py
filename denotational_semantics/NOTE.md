##  p.47~ Denotational Semantics

### p.48 式の実装 Number

```Python
Number(5).to_py()
# 'lambda e: 5'
Boolean(False).to_py()
# 'lambda e: False'
```

```Python
la = eval(Number(5).to_py())
print la
# <function <lambda> at 0x10adb7410>
la({})
# 5
la = eval(Boolean(False).to_py())
print la
# <function <lambda> at 0x10ae155f0>
la({})
# False
```

### p.49 式の実装 Variable

```Python
exp = Variable('x')
print exp
# «x»
exp.to_py()
# 'lambda e: e[x]'
la = eval(exp.to_py())
print la
# <function <lambda> at 0x10dd6b410>
la({ 'x': 7 })
# 7
```

### p.50 式の実装 Add/LessThan

```Python
Add(Variable('x'), Number(1)).to_py()
# "lambda e: (lambda e: e['x'])(e) + (lambda e: 1)(e)"
LessThan(Add(Variable('x'), Number(1)), Number(3)).to_py()
# "lambda e: (lambda e: (lambda e: e['x'])(e) + (lambda e: 1)(e))(e) < (lambda e: 3)(e)"
```

#### 検算

```Python
environment = { 'x': 3 }
print environment
# {'x': 3}
la = eval(Add(Variable('x'), Number(1)).to_py())
print la
# <function <lambda> at 0x10c8926e0>
la(environment)
# 4
la = eval(
  LessThan(Add(Variable('x'), Number(1)), Number(3)).to_py()
)
print la
# <function <lambda> at 0x10c834410>
la(environment)
# False
```

