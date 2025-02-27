def sum_even_ints_inclusive(ints):
    """
    Returns the sum of all even integers from index 3 to index 5, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    sum_of_even_ints = 0
    for i in range(3, 6):
        if ints[i] % 2 == 0:
            sum_of_even_ints += ints[i]
    return sum_of_even_ints