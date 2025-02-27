def sum_even_ints_inclusive(ints):
    """Sums all even integers from index 0 to index 8, both inclusive.
    If no even integers exist in the specified range, returns 0.
    Args:
        ints (list): A list of integers.
    Returns:
        int: The sum of all even integers from index 0 to index 8, both inclusive.
    """
    sum_of_even_ints = 0
    for i in range(9):
        if ints[i] % 2 == 0:
            sum_of_even_ints += ints[i]
    return sum_of_even_ints