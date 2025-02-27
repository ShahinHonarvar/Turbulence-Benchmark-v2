def sum_even_ints_inclusive(lst):
    """
    Returns the sum of all even integers from index 29 to index 29, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    sum_even = 0
    for i in range(30, 31):
        if lst[i] % 2 == 0:
            sum_even += lst[i]
    return sum_even