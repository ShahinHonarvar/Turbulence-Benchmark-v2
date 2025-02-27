def sum_odd_ints_inclusive(nums):
    """
    Returns the sum of all odd integers from index 35 to index 49, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    result = 0
    for i in range(len(nums)):
        if 35 <= i <= 49 and nums[i] % 2 != 0:
            result += nums[i]
    return result