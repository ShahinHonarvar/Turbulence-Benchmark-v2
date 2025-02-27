def sum_odd_ints_inclusive(ints):
    """
    Returns the sum of all odd integers from index 0 to index 0, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum = 0
    for i in ints:
        if i % 2 != 0:
            sum += i
    return sum