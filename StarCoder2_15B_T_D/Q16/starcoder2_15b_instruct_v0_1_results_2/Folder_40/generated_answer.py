def sum_even_ints_inclusive(nums):
    """
    Returns the sum of all even integers from index 0 to index 2, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    return sum((num for num in nums[0:3] if num % 2 == 0))