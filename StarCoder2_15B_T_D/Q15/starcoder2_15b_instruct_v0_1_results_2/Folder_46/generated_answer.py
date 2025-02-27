def sum_odd_ints_inclusive(ints):
    """
    Returns the sum of all odd integers in `ints` from index 30 to index 87, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    total = 0
    for i in range(30, 88):
        if ints[i] % 2 == 1:
            total += ints[i]
    return total