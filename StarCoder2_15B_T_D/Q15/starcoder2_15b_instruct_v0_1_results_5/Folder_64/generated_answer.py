def sum_odd_ints_inclusive(nums):
    """
    Returns the sum of all odd integers from index 0 to index 4, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((num for num in nums[0:5] if num % 2 != 0))