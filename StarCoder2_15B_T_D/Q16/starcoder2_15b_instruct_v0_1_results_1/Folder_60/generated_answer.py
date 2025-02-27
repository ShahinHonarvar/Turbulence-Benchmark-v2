def sum_even_ints_inclusive(ints):
    """
    Returns the sum of all even integers from index 75 to index 85, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """

    def is_even(num):
        return num % 2 == 0
    return sum(filter(is_even, ints[75:86]))