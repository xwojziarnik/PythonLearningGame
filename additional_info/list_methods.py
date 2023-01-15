liat_methods = {
    "append": """ Append object to the end of the list. """,
    "clear": """ Remove all items from list. """,
    "copy": """ Return a shallow copy of the list. """,
    "count": """ Return number of occurrences of value. """,
    "extend": """ Extend list by appending elements from the iterable. """,
    "index": """
        Return first index of value.
        
        Raises ValueError if the value is not present.
        """,
    "insert": """ Insert object before index. """,
    "pop": """
        Remove and return item at index (default last).
        
        Raises IndexError if list is empty or index is out of range.
        """,
    "remove": """
        Remove first occurrence of value.
        
        Raises ValueError if the value is not present.
        """,
    "reverse": """ Reverse *IN PLACE*. """,
    "sort": """
        Sort the list in ascending order and return None.
        
        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).
        
        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.
        
        The reverse flag can be set to sort in descending order.
        """,
}
