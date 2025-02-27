def sum_even_ints_inclusive(lst):
    """
    Returns the sum of all even integers from index 64 to 66, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    sum = 0
    for i in range(64, 67):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum