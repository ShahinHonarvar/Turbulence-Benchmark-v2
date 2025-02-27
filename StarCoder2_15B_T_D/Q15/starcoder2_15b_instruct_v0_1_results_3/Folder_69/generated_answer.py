def sum_odd_ints_inclusive(lst):
    """
    Returns the sum of all odd integers from index 32 to index 35, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum = 0
    for i in range(32, 36):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum