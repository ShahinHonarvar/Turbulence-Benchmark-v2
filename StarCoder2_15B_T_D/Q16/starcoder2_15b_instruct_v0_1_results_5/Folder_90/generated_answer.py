def sum_even_ints_inclusive(int_list):
    """
    Returns the sum of all even integers from index 262 to index 746, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    sum_even = 0
    for i in range(262, 747):
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even