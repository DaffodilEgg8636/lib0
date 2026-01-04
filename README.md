# Lib0 - Python Dynamic Attribute Wrapper
A lightweight Python library that provides dynamic attribute access and method chaining for dictionary-like objects. Lib0 wraps Python dictionaries (and other types) to enable dot-notation access while maintaining full compatibility with Python's built-in operators and functions.

## Features
* Dot Notation Access: Access nested dictionaries using dot syntax (obj.users.john.age)
* Auto-creation: Automatically creates nested dictionaries when accessing non-existent keys
* Type Conversion Methods: Built-in .int(), .float(), .str(), .bool(), .list(), .dict() methods
* Full Operator Support: Supports all Python operators (+, -, *, /, comparisons, etc.)
* Container Protocol: Implements __getitem__, __setitem__, __len__, __iter__ for dict/list-like behavior
* Type Preserving: Wrapped objects maintain their original type behavior
* Root Tracking: Maintains reference to root object for last-value access

## Installation
No installation required! Simply copy the Lib0 class into your project:
Copy the entire Lib0 class definition from above into your project

## Quick Start
```
from lib0 import Lib0, dict2lib0, lib02dict

#Create a new Lib0 object
obj = Lib0()

#Auto-create nested dictionaries
obj.users.john.age = 30
obj.users.john.city = "New York"

print(obj.users.john.age)  # 30
print(obj.users.john.city)  # "New York"

#Convert existing dict to Lib0
data = {"app": {"version": "1.0", "settings": {"debug": True}}}
wrapped = dict2lib0(data)

print(wrapped.app.version)  # "1.0"
print(wrapped.app.settings.debug)  # True
```

## Core Usage
### Basic Attribute Access
```
obj = Lib0()

### Set values
obj.name = "Lib0"
obj.version = 1.0
obj.meta.tags = ["python", "wrapper", "utility"]
```

### Get values
```
print(obj.name)  # "Lib0"
print(obj.meta.tags[0])  # "python"
```

### Auto-creation of nested structures
```
obj.config.database.host = "localhost"
obj.config.database.port = 5432
```

### Type Conversion Methods
```
obj = Lib0("42")

#Convert wrapped values
print(obj.int())    # 42 (as integer)
print(obj.float())  # 42.0 (as float)
print(obj.str())    # "42" (as string)
print(obj.bool())   # True (as boolean)

#List and dict conversions
obj = Lib0([1, 2, 3])
print(obj.list())  # [1, 2, 3]

obj = Lib0({"a": 1, "b": 2})
print(obj.dict())  # {"a": 1, "b": 2}
```

### Operator Support
```
a = Lib0(10)
b = Lib0(5)

#Arithmetic operations
print(a + b)   # 15
print(a - b)   # 5
print(a * b)   # 50
print(a / b)   # 2.0

#Comparisons
print(a > b)   # True
print(a == 10) # True

#In-place operations
a += 5
print(a)  # 15
```

### Dictionary-like Behavior
```
obj = Lib0({"users": {"john": {"age": 30}}})

#Square bracket access
print(obj["users"]["john"]["age"])  # 30

#Mixed notation
print(obj.users["john"].age)  # 30

#Container methods
print(len(obj.users))  # 1
print("john" in obj.users)  # True

#Iteration
for key in obj.users:
    print(key)  # "john"
```


## API Reference
### Lib0 Class
<b>Initialization</b>
```
Lib0(data=None, root=None)
```
* data: Initial data (dict, list, or any other type)
* root: Root Lib0 object (for internal use)

### Special Methods
<b>All Python special methods are implemented:</b>
* Arithmetic: __add__, __sub__, __mul__, __div__, etc.
* Comparison: __eq__, __lt__, __gt__, etc.
* Container: __getitem__, __setitem__, __len__, __iter__
* Type Conversion: __int__, __float__, __str__, __bool__

<b>Conversion Methods</b>
* .int(): Convert to integer
* .float(): Convert to float
* .str(): Convert to string
* .bool(): Convert to boolean
* .list(): Convert to list
* .dict(): Convert to dictionary

### Helper Functions
```
dict2lib0(data)
```
Recursively converts a nested dictionary to Lib0 objects.
```
data = {"a": {"b": {"c": 1}}}
wrapped = dict2lib0(data)
print(wrapped.a.b.c)  # 1
```

```
lib02dict(lib_obj)
```
Recursively converts a Lib0 object back to a standard Python dictionary.
```
obj = Lib0({"x": 1, "y": {"z": 2}})
regular_dict = lib02dict(obj)
print(regular_dict)  # {"x": 1, "y": {"z": 2}}
```


## Advanced Examples
### Configuration Management
```
config = Lib0()

#Build configuration with dot notation
config.app.name = "MyApp"
config.app.version = "1.0.0"
config.database.host = "localhost"
config.database.port = 5432
config.database.credentials.username = "admin"
config.database.credentials.password = "secret"

#Access nested values easily
if config.database.credentials.username == "admin":
    print("Admin access")

#Convert to dict for serialization
config_dict = lib02dict(config)
import json
json.dump(config_dict, open("config.json", "w"))
```

### Data Transformation Pipeline
```
#Process data with method chaining
data = dict2lib0({
    "values": ["10", "20.5", "30", "not_a_number"]
})

#Convert and filter numeric values
numeric_values = [
    val.float() for val in data.values 
    if val.float()  # Will raise TypeError for non-convertible
]

print(sum(numeric_values))  # 60.5
```

### Last Value Tracking
```
root = Lib0()
root.a.b.c = 10
root.x.y.z = 20

print(root._last)  # 20 (last assigned value)
```


## Error Handling
Lib0 provides clear error messages:
```
obj = Lib0("not_a_number")
try:
    print(obj.int())
except TypeError as e:
    print(e)  # "Cannot convert str to int."

obj = Lib0([1, 2, 3])
try:
    print(obj.dict())
except TypeError as e:
    print(e)  # "Cannot convert list to dict."
```


## Performance Considerations
* Overhead: Lib0 adds minimal overhead compared to raw dictionaries
* Memory: Each Lib0 object maintains reference to wrapped data and root
* Use Cases: Best for configuration, data transformation, and APIs where dot notation improves readability

## Limitations
* Only works with dictionary-like structures for attribute access
* Auto-creation only works with dictionaries (not lists or other types)
* Not designed for high-performance numeric computing
* _last attribute tracks last assignment in the entire object tree

## Examples in the Wild
```
#API Response Wrapper
response = dict2lib0(api_response)
print(response.data.users[0].name)

#Configuration Builder
cfg = Lib0()
cfg.server.host = "0.0.0.0"
cfg.server.port = 8000
cfg.features.auth.enabled = True
cfg.features.cache.ttl = 3600

#Data Validation
def validate_user(user_data):
    user = Lib0(user_data)
    assert user.age.int() >= 18, "Must be 18 or older"
    assert len(user.email.str()) > 0, "Email required"
    return True
```


## ⚠️ Common Pitfalls: Auto-Creation Side Effects
### The "Undefined to Defined" Problem
Lib0's auto-creation feature (__getattr__) automatically creates nested dictionaries for non-existent attributes. While convenient, this can lead to unexpected type errors:

### Problem Scenario 1: Missing Attributes in Expressions
```
data = Lib0()
data.x = 5  # Integer value

#data.y doesn't exist - auto-creates as empty dict wrapped in Lib0
print(data.x + data.y)  # ❌ TypeError: unsupported operand type(s) for +: 'int' and 'dict'

#What happens:
#1. data.y → creates {} → wraps as Lib0({})
#2. data.x + Lib0({}) → 5 + {
#3. TypeError! Cannot add integer to dictionary
```

### Problem Scenario 2: Function Call on Missing Attribute
```
config = Lib0()
config.database.connect()  # ❌ AttributeError: 'Lib0' object is not callable

#What happens:
#1. config.database doesn't exist → creates {} → wraps as Lib0({})
#2. .connect() tries to call Lib0({}) as a function
#3. Lib0 instances aren't callable → AttributeError
```

### Why This Happens
When you access a non-existent attribute:
1. Lib0 automatically creates an empty dictionary for that key
2. Wraps it in a new Lib0 instance
3. Returns this empty Lib0-wrapped dict
The result: You get a valid Lib0 object instead of an AttributeError, but it's probably not what you expected for the operation you're trying to perform.
