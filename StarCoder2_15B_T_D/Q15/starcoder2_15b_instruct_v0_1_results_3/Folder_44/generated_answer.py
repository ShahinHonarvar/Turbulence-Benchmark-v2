def sum_odd_ints_inclusive(nums):
    """
    Returns the sum of all odd integers from index 13 to index 68, both inclusive,
    or 0 if no odd integers exist in the specified range.
    """
    return sum((num for i, num in enumerate(nums) if i >= 13 and i <= 68 and (num % 2 == 1)))