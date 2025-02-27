def sum_even_ints_inclusive(numbers):
    """
    Returns the sum of all even integers from index 43 to index 51, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    sum_even = 0
    for i in range(43, 52):
        if numbers[i] % 2 == 0:
            sum_even += numbers[i]
    return sum_even