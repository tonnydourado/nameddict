nameddict
=========

Python dictionaries with optional dot like attributes access.

This is a simple module to provide namedtuple-like funcionality, but with dictionaries.
It's basically a metaclass that returns as intance a custom class. You can define required attributes, to be passed to the constructor. Those attributes will then be accessible both by dictionary notation (d[key]) and dot notation (d.key). Also, any attribute you add, both in dictionary and dit notation, will be available on the oposite notation.

Use
=========

Just import the metaclass (yep, the repetition annoys me too. Sugestions are welcome):

```python
from nameddict import nameddict
```

and create your custom classes:

```python
Test = nameddict('Test', ['a', 'b', 'c'])
test = Test(1, 2, c=3)
```

Tests
=========

I also wrote some tests using konira. Just run:

```
konira
```

in the directory with both the source and the tests.
