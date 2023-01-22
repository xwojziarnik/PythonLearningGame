dict_methods = {
    "clear": """ D.clear() -> None.  Remove all items from D. """,
    "copy": """ D.copy() -> a shallow copy of D """,
    "fromkeys": """ Create a new dictionary with keys from iterable and values set to value. """,
    "get": """ Return the value for key if key is in the dictionary, else default. """,
    "items": """ D.items() -> a set-like object providing a view on D's items """,
    "keys": """ D.keys() -> a set-like object providing a view on D's keys """,
    "pop": """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        
        If the key is not found, return the default if given; otherwise,
        raise a KeyError.
        """,
    "popitem": """
        Remove and return a (key, value) pair as a 2-tuple.
        
        Pairs are returned in LIFO (last-in, first-out) order.
        Raises KeyError if the dict is empty.
        """,
    "setdefault": """
        Insert key with a value of default if key is not in the dictionary.
        
        Return the value for key if key is in the dictionary, else default.
        """,
    "update": """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """,
    "values": """ D.values() -> an object providing a view on D's values """,
}
