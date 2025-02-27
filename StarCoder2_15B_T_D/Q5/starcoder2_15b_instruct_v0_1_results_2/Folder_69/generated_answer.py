def all_neg_ints_inclusive(lst):
    """Return the list of all negative integers from index 32 to index 35, both inclusive.
    If no negative integers exist in the specified range, return an empty list."""
    return [x for x in lst[32:36] if x < 0]