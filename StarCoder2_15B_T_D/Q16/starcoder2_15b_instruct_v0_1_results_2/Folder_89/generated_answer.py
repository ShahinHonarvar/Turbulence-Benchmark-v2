def sum_even_ints_inclusive(nums):
    """
    Returns the sum of all even integers from index 56 to index 82, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    total = 0
    for i in range(56, 83):
        if nums[i] % 2 == 0:
            total += nums[i]
    return total