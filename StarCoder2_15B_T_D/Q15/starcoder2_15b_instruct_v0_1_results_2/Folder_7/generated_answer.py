def sum_odd_ints_inclusive(ints):
    """
    Returns the sum of all odd integers from index 661 to index 924, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum_of_odd_ints = 0
    for i in range(661, 925):
        if ints[i] % 2 != 0:
            sum_of_odd_ints += ints[i]
    return sum_of_odd_ints