import re

def all_odd_ints_inclusive(ints):
    """
    Returns the list of all odd integers from index 0 to index 6, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [i for i in ints if i % 2 == 1][0:7]