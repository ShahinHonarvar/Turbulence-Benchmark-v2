def sum_even_ints_inclusive(int_list):
    """
    Returns the sum of all even integers from index 32 to index 35, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    sum_even_ints = 0
    for i in range(32, 36):
        if int_list[i] % 2 == 0:
            sum_even_ints += int_list[i]
    return sum_even_ints