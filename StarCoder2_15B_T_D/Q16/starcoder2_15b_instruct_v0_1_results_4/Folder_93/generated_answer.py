def sum_even_ints_inclusive(nums):
    """Returns the sum of all even integers from index 75 to index 94, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    return sum((num for i, num in enumerate(nums) if i >= 75 and i <= 94 and (num % 2 == 0)))