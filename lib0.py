
class Lib0:
    def __init__(self, data=None, root=None):
        self._data = data if data is not None else {}
        self._last = None
        self._root = self if root is None else root

    def __getattr__(self, key):
        if key == "_last":
            return self._root._last

        if hasattr(self._data, key):
            attr = getattr(self._data, key)
            if callable(attr):
                return attr  # Let method like append(), pop() work
            else:
                return attr

        if isinstance(self._data, dict):
            if key not in self._data:
                # Auto-create a new dict (wrapped by Lib0) if key does not exist
                self._data[key] = {}
            value = self._data[key]
            if isinstance(value, dict):
                wrapped = Lib0(value, root=self._root)
                self._data[key] = wrapped
                return wrapped
            return value
        raise AttributeError(f"No attribute '{key}'")

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        elif isinstance(self._data, dict):
            if isinstance(value, dict):
                self._data[key] = Lib0(value, root=self._root)
            elif not isinstance(value, Lib0):
                self._data[key] = Lib0(value, root=self._root)
            else:
                self._data[key] = value
            super(Lib0, self._root).__setattr__('_last', self._data[key])
        else:
            raise AttributeError(f"Cannot set attribute '{key}' on non-dict value.")

    def __repr__(self):
        return f"Lib0({self._data})"

    def __delattr__(self, key):
        if key.startswith('_'):
            super().__delattr__(key)
        elif isinstance(self._data, dict) and key in self._data:
            del self._data[key]
        else:
            raise AttributeError(f"No such attribute '{key}' to delete.")


    def int(self):
        try:
            return int(self._data)
        except (ValueError, TypeError):
            raise TypeError(f"Cannot convert {type(self._data).__name__} to int.")

    def float(self):
        try:
            return float(self._data)
        except (ValueError, TypeError):
            raise TypeError(f"Cannot convert {type(self._data).__name__} to float.")

    def bool(self):
        try:
            return bool(self._data)
        except Exception:
            raise TypeError(f"Cannot convert {type(self._data).__name__} to bool.")

    def str(self):
        try:
            return str(self._data)
        except Exception:
            raise TypeError(f"Cannot convert {type(self._data).__name__} to str.")

    def list(self):
        if isinstance(self._data, (list, tuple, set, dict, str)):
            return list(self._data)
        raise TypeError(f"Cannot convert {type(self._data).__name__} to list.")

    def dict(self):
        if isinstance(self._data, dict):
            return dict(self._data)
        raise TypeError(f"Cannot convert {type(self._data).__name__} to dict.")



    # String & Representation
    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return repr(self._data)

    def __format__(self, format_spec):
        return format(self._data, format_spec)

    # Conversions
    def __bool__(self):
        return bool(self._data)

    def __int__(self):
        return int(self._data)

    def __float__(self):
        return float(self._data)

    def __complex__(self):
        return complex(self._data)

    def __bytes__(self):
        return bytes(self._data)

    def __hash__(self):
        return hash(self._data)

    # Comparison Operators
    def __eq__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return self._data == other_val

    def __ne__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return self._data != other_val

    def __lt__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return self._data < other_val

    def __le__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return self._data <= other_val

    def __gt__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return self._data > other_val

    def __ge__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return self._data >= other_val

    # Arithmetic Operators
    def __add__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return self._data + other_val

    def __sub__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return self._data - other_val

    def __mul__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return self._data * other_val

    def __truediv__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return self._data / other_val

    def __floordiv__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return self._data // other_val

    def __mod__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return self._data % other_val

    def __pow__(self, other, modulo=None):
        other_val = other._data if isinstance(other, Lib0) else other
        if modulo is None:
            return pow(self._data, other_val)
        else:
            return pow(self._data, other_val, modulo)

    # Right-side arithmetic operators
    def __radd__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return other_val + self._data

    def __rsub__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return other_val - self._data

    def __rmul__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return other_val * self._data

    def __rtruediv__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return other_val / self._data

    def __rfloordiv__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return other_val // self._data

    def __rmod__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return other_val % self._data

    def __rpow__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        return pow(other_val, self._data)

    # In-place arithmetic operators
    def __iadd__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        self._data += other_val
        return self

    def __isub__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        self._data -= other_val
        return self

    def __imul__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        self._data *= other_val
        return self

    def __itruediv__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        self._data /= other_val
        return self

    def __ifloordiv__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        self._data //= other_val
        return self

    def __imod__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        self._data %= other_val
        return self

    def __ipow__(self, other):
        other_val = other._data if isinstance(other, Lib0) else other
        self._data **= other_val
        return self

    # Unary operators
    def __neg__(self):
        return -self._data

    def __pos__(self):
        return +self._data

    def __abs__(self):
        return abs(self._data)

    def __invert__(self):
        return ~self._data

    # Container methods (if you want to support indexing like dict/list)
    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        value = self._data[key]
        if isinstance(value, dict):
            return Lib0(value)
        return value

    def __setitem__(self, key, value):
        if isinstance(value, dict):
            self._data[key] = Lib0(value)
        else:
            self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __contains__(self, item):
        return item in self._data

    # Iterator support
    def __iter__(self):
        return iter(self._data)

    def __next__(self):
        return next(self._data)

    # Context management (optional)
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __round__(self, ndigits=None):
        try:
            # Try to get the underlying float/int value for rounding
            value = self._data
            if ndigits is None:
                return round(value)
            else:
                return round(value, ndigits)
        except Exception:
            # If conversion fails, just return 0 or some fallback value
            return 0




def dict2lib0(data):
    if isinstance(data, dict):
        return Lib0({k: dict2lib0(v) for k, v in data.items()})
    else:
        # wrap every non-dict value into Lib0 so it supports .int(), .float(), etc.
        return Lib0(data)




def lib02dict(lib_obj):
    """
    Recursively convert a Lib0 object into a standard Python dict.
    """
    result = {}
    for key, value in lib_obj._data.items():
        if isinstance(value, Lib0):
            result[key] = lib02dict(value)
        else:
            result[key] = value
    return result
