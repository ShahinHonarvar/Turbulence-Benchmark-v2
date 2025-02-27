def sum_even_ints_inclusive(int_list):
    """
    Returns the sum of all even integers from index 30 to index 200, both inclusive, in a list.
    If no even integers exist in the specified range, returns 0.
    """
    sum_even = 0
    for i in range(30, 201):
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even