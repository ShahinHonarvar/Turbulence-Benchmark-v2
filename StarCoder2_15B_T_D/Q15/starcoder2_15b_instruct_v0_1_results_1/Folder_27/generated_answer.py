def sum_odd_ints_inclusive(ints):
    """
    Return the sum of all odd integers from index 66 to index 93, both inclusive.
    If no odd integers exist in the specified range, return 0.
    """
    return sum((i for i in ints[66:94] if i % 2 == 1))