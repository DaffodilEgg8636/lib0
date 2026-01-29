# Lib0 : Dynamic Python Attribute Wrapper

## **Important : This readme might not be up to date, this is the snapshot branch, use its code only if you know what you're doing** 

## Overview
Lib0 is a Python wrapper class that provides JavaScript-style dot notation access to nested dictionaries and other data structures. It automatically creates missing nested dictionaries and provides comprehensive type conversion methods while maintaining full Python operator compatibility.

## Core Philosophy
* Dot notation for intuitive access
* Auto-creation of missing nested structures
* Transparent wrapping - behaves like wrapped data
* Full Python compatibility - all operators work
* Type-safe conversions with clear error messages

## Installation
```
# Copy the entire Lib0 class and helper functions into your project
from lib0 import Lib0, dict2lib0, lib02dict
```

## 1. Basic Usage
### Creating Objects
```
# Empty Lib0 object
obj = Lib0()

# From existing dict (non-recursive)
obj = Lib0({"x": 1, "y": {"z": 2}})

# From existing dict (recursive - preferred)
obj = dict2lib0({"x": 1, "y": {"z": 2}})

# With None handling
obj = Lib0(None)                    # Creates empty dict {}
obj = Lib0(None, PRESERVE_NONE=True)  # Creates Lib0(None) - rarely needed
```

### Attribute Access
```
obj = Lib0()

# Set values
obj.name = "Lib0"
obj.config.database.host = "localhost"
obj.config.database.port = 5432

# Get values
print(obj.name)                    # "Lib0"
print(obj.config.database.host)    # "localhost"

# Auto-creation of nested dicts
obj.a.b.c = "value"                # Creates a, b as empty dicts
```

### Index Access (Brackets)
```
obj = Lib0()

# Dict-style access
obj["x"] = 1
print(obj["x"])                    # 1

# Auto-creation works here too
print(obj["new"]["nested"])        # Creates and returns empty Lib0

# Mixed notation
obj.data["users"].john.age = 30
```

## 2. Type Conversion System
### Mutation Methods (Change the value)
```
obj = Lib0("42")
obj._int()                         # obj._data becomes 42 (int)
obj._float()                       # obj._data becomes 42.0 (float)
obj._str()                         # obj._data becomes "42.0" (str)

# Chaining supported
obj = Lib0("3.14")._float()._int() # obj._data becomes 3 (int)
```

### Conversion Methods (Return converted value)
```
obj = Lib0("42")
print(obj.int())                   # 42 (returns int)
print(obj.float())                 # 42.0 (returns float)
print(obj.str())                   # "42" (returns str)
print(obj.bool())                  # True (returns bool)
```

### Python Protocol Conversions
```
obj = Lib0("42")
print(int(obj))                    # 42 (calls __int__)
print(float(obj))                  # 42.0 (calls __float__)
print(str(obj))                   # "42" (calls __str__)
print(bool(obj))                  # True (calls __bool__)
```

### List and Dict Conversions
```
# To list
obj = Lib0((1, 2, 3))
print(obj.list())                  # [1, 2, 3]

obj = Lib0("hello")
print(obj.list())                  # ['h', 'e', 'l', 'l', 'o']

# To dict
obj = Lib0({"a": 1, "b": 2})
print(obj.dict())                  # {"a": 1, "b": 2}
```

## 3. Container Operations
### Sequence Types Support
```
# Lists
obj = Lib0([10, 20, 30, 40, 50])
print(obj[1])                      # 20
print(obj[1:4])                    # [20, 30, 40]
print(obj[-1])                     # 50

# Strings
obj = Lib0("hello")
print(obj[1])                      # 'e'
print(obj[1:4])                    # "ell"

# Tuples, ranges, bytes
obj = Lib0((1, 2, 3))
print(obj[0])                      # 1

obj = Lib0(range(10))
print(obj[5])                      # 5
print(obj[2:5])                    # range(2, 5)
```

### Mutable vs Immutable
```
# Mutable - can modify
obj = Lib0([1, 2, 3])
obj[0] = 99                        # OK: [99, 2, 3]
obj[1:3] = [88, 77]                # OK: [99, 88, 77]

obj = Lib0(bytearray(b"abc"))
obj[0] = 122                       # OK: bytearray(b"zbc")

# Immutable - cannot modify
obj = Lib0("hello")
# obj[0] = "H"                     # TypeError: 'str' object does not support item assignment

obj = Lib0((1, 2, 3))
# obj[0] = 99                      # TypeError: 'tuple' object does not support item assignment

obj = Lib0(b"abc")
# obj[0] = 122                     # TypeError: 'bytes' object does not support item assignment
```

### Container Methods
```
obj = Lib0({"a": 1, "b": 2, "c": 3})

print(len(obj))                    # 3
print("a" in obj)                  # True

# Iteration
for key in obj:
    print(key, obj[key])           # a 1, b 2, c 3

# Deletion
del obj["b"]                       # Removes key "b"
del obj.a                          # Removes attribute "a"
```

## 4. Operator Overloading
### Arithmetic Operations
```
a = Lib0(10)
b = Lib0(5)

print(a + b)                       # 15
print(a - b)                       # 5
print(a * b)                       # 50
print(a / b)                       # 2.0
print(a // b)                      # 2
print(a % b)                       # 0
print(a ** b)                      # 100000

# In-place operations
a += 5                            # a becomes Lib0(15)
a *= 2                            # a becomes Lib0(30)
```

### Comparison Operations
```
a = Lib0(10)
b = Lib0(5)

print(a > b)                       # True
print(a < b)                       # False
print(a == 10)                     # True
print(a != b)                      # True
print(a >= 10)                     # True
print(a <= 20)                     # True
```

### Unary Operations
```
obj = Lib0(5)
print(-obj)                        # -5
print(+obj)                        # 5
print(abs(Lib0(-5)))               # 5
print(~Lib0(5))                    # -6 (bitwise NOT)
```

## 5. Special Features
### _last Tracking
```
obj = Lib0()
obj.x = 10
print(obj._last)                   # 10 (last assigned value)

obj.y.z = {"a": 1}
print(obj._last)                   # {"a": 1} (last assigned value)

obj.a.b.c = "deep"
print(obj._last)                   # "deep"
```

### Root Reference System
```
root = Lib0()
branch = Lib0({"x": 1}, ROOT=root)
leaf = Lib0({"y": 2}, ROOT=root)

leaf.value = 100
print(root._last)                  # 100 (updated through root chain)
```

## 6. Helper Functions
### dict2lib0() - Recursive Conversion
```
data = {"app": {"name": "MyApp", "version": "1.0", "settings": {"debug": True}}}
obj = dict2lib0(data)

print(obj.app.name)                # "MyApp"
print(obj.app.settings.debug)      # True
print(type(obj.app.settings))      # <class 'Lib0'>
```

### lib02dict() - Reverse Conversion
```
obj = Lib0()
obj.config.host = "localhost"
obj.config.port = 8080

data = lib02dict(obj)
print(data)                        # {"config": {"host": "localhost", "port": 8080}}
print(type(data))                  # <class 'dict'>
```

### Round-trip Conversion
```
original = {"a": {"b": {"c": [1, 2, 3]}}}
wrapped = dict2lib0(original)
unwrapped = lib02dict(wrapped)
print(original == unwrapped)       # True
```

## 7. Advanced Usage
### Configuration Management
```
config = dict2lib0({
    "app": {
        "name": "MyApp",
        "version": "1.0.0"
    },
    "database": {
        "host": "localhost",
        "port": 5432,
        "credentials": {
            "username": "admin",
            "password": "secret"
        }
    }
})

# Easy access
if config.database.credentials.username == "admin":
    print("Admin access granted")

# Dynamic updates
config.database.pool_size = 20
config.features.new_feature.enabled = True
```

### Data Validation Pipeline
```
def process_user_data(raw_data):
    user = dict2lib0(raw_data)
    
    # Type conversions with validation
    user.age = user.age.int()      # Convert to int
    if user.age < 18:
        raise ValueError("Must be 18 or older")
    
    user.email = user.email.str().lower().strip()
    if "@" not in user.email:
        raise ValueError("Invalid email")
    
    return lib02dict(user)
```

### API Response Wrapping
```
import requests

response = requests.get("https://api.example.com/users/1")
data = dict2lib0(response.json())

print(f"User: {data.user.name}")
print(f"Email: {data.user.email}")
print(f"Joined: {data.user.created_at}")

# Safe access with defaults
posts = data.user.recent_posts or []
```

### Context Manager Usage
```
with Lib0() as session:
    session.user.id = 123
    session.user.name = "John"
    session.cart.items = ["item1", "item2"]
    
    # __exit__ called automatically here
```

## 8. Error Handling
### Clear Error Messages
```
obj = Lib0("not_a_number")
try:
    obj._int()
except TypeError as e:
    print(e)  # "Cannot convert str to int."

obj = Lib0([1, 2, 3])
try:
    obj.dict()
except TypeError as e:
    print(e)  # "Cannot convert list to dict."
```

### Index Errors
```
obj = Lib0([1, 2, 3])
try:
    print(obj[10])
except IndexError as e:
    print(e)  # "Index out of range: 10, length: 3"
```

### Attribute Errors
```
obj = Lib0()
try:
    print(obj.nonexistent.deep.value)
except AttributeError as e:
    print(e)  # "No attribute 'nonexistent'"
```

## 9. Performance Considerations
### When to Use Lib0
* Good for: Configuration, API responses, data transformation, prototyping
* Less ideal for: High-performance numeric computing, large-scale data processing

### Memory Usage
* Each value is wrapped in a Lib0 object
* Root tracking adds minor overhead
* Use lib02dict() for serialization/storage

## 10. Complete API Reference
### Lib0 Class Methods

* __init__(DATA=None, ROOT=None, PRESERVE_NONE=False)
* _int(), _float(), _bool(), _str(), _list(), _dict() - Mutation methods
* int(), float(), bool(), str(), list(), dict() - Conversion methods
* repr(), format() - Representation methods

### Special Methods (Dunder)
* All arithmetic: __add__, __sub__, __mul__, etc.
* All comparison: __eq__, __lt__, __gt__, etc.
* Container: __getitem__, __setitem__, __len__, __iter__
* Conversion: __int__, __float__, __str__, __bool__

### Helper Functions
* dict2lib0(data) - Recursively convert dict to Lib0
* lib02dict(lib_obj) - Recursively convert Lib0 to dict

## 11. Examples Repository
### Quick Examples
```
# 1. Build nested config
config = Lib0()
config.server.host = "0.0.0.0"
config.server.port = 8000
config.features.api.enabled = True

# 2. Process form data
form = dict2lib0(request.form)
user_age = form.age.int()
user_name = form.name.str().title()

# 3. JSON manipulation
import json
data = Lib0(json.loads(json_string))
data.timestamp = data.timestamp.int()  # Convert string timestamp to int

# 4. Data transformation pipeline
results = [
    item.score.float() * 1.1  # 10% bonus
    for item in data.scores
    if item.score.float() > 50
]
```
