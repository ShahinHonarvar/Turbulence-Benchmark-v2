def all_odd_ints_inclusive(lst):
    """Returns the list of all odd integers from index 40 to index 80, both inclusive. If no odd integers exist in the specified range, returns an empty list."""
    return [num for i, num in enumerate(lst) if i >= 40 and i <= 80 and (num % 2 == 1)]