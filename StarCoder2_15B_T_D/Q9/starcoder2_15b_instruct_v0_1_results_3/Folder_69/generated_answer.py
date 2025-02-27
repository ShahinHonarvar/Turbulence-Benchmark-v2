def all_odd_ints_inclusive(ints):
    """
    Takes a list of integers and returns the list of all odd integers from index 32 to index 35, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [n for i, n in enumerate(ints) if i >= 32 and i <= 35 and (n % 2 == 1)]