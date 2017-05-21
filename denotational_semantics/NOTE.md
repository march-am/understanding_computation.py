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

