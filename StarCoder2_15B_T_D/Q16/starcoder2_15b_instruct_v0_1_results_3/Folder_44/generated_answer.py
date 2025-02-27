def sum_even_ints_inclusive(int_list):
    """
    Returns the sum of all even integers in the list between indices 13 and 68, both inclusive.
    If no even integers are found, returns 0.
    """
    sum_even = 0
    for i, num in enumerate(int_list):
        if i >= 13 and i <= 68 and (num % 2 == 0):
            sum_even += num
    return sum_even