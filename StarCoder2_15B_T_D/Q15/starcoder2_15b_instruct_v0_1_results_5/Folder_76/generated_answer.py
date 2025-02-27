def sum_odd_ints_inclusive(lst):
    """
    Returns the sum of all odd integers from index 686 to index 987, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    result = 0
    for i in range(686, 988):
        if lst[i] % 2 == 1:
            result += lst[i]
    return result