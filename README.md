# database
Miscellaneous classes I use to store data

## Examples

### class Signal
```python
import numpy as np
from signal_class import Signal

s = Signal(np.arange(10), color="black", label="iris")

print(s.color)  # black
print(s.label)  # iris

print(s.mean().color)  # black
print(s[1:6].label)  # iris

print(s._meta)  # ['color', 'label']
```

### class Database

```python
from database import Database

class Apple:
  def __init__(self, color):
    self.color = color

db = Database([Apple("green"), Apple("red"), Apple("blue"), Apple("red")])

# db acts like a list
print(len(db))
print(db[-1].color)
print([a.color for a in db[1:3]])

print(list(db.groupby("color")))
```
