def sum_even_ints_inclusive(lst):
    """
    Returns the sum of all even integers from index 75 to index 85, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    sum_even_ints = 0
    for i in range(75, 86):
        if lst[i] % 2 == 0:
            sum_even_ints += lst[i]
    return sum_even_ints