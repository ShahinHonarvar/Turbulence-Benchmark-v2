def sum_odd_ints_inclusive(nums):
    """
    Returns the sum of all odd integers from index 262 to index 746, both inclusive.
    If no odd integers exist in the specified range, the function returns 0.
    """
    sum_odd = 0
    for i in range(262, 747):
        if nums[i] % 2 != 0:
            sum_odd += nums[i]
    return sum_odd