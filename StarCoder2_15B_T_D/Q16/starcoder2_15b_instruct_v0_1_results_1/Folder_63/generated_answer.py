def sum_even_ints_inclusive(numbers):
    """
    Given a list of integers, return the sum of all even integers from index 22 to index 88, both inclusive.
    If no even integers exist in the specified range, return 0.
    """
    return sum((number for i, number in enumerate(numbers) if 22 <= i <= 88 and number % 2 == 0))