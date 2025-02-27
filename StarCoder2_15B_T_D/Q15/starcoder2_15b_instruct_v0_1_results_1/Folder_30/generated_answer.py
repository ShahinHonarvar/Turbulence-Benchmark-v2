def sum_odd_ints_inclusive(ints):
    """
    Returns the sum of all odd integers from index 55 to index 98, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    result = 0
    for i in range(len(ints)):
        if i >= 55 and i <= 98 and (ints[i] % 2 == 1):
            result += ints[i]
    return result