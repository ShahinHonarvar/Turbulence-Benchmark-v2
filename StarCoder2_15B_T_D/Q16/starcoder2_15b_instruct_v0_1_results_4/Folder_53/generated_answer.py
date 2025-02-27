def sum_even_ints_inclusive(integer_list):
    """
    Returns the sum of all even integers from index 111 to index 111, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    sum_even = 0
    for i in range(111, 112):
        if integer_list[i] % 2 == 0:
            sum_even += integer_list[i]
    return sum_even