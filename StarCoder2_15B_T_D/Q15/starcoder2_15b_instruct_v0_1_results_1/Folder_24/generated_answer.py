def sum_odd_ints_inclusive(ints):
    """
    Returns the sum of all odd integers in the range from index 74 to 95, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((i for i in ints[74:96] if i % 2 == 1))