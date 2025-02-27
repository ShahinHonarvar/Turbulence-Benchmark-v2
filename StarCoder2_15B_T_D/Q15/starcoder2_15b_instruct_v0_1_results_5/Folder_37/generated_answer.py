def sum_odd_ints_inclusive(nums):
    """
    Returns the sum of all odd integers from index 1 to index 5, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum_odd = 0
    for num in nums[1:6]:
        if num % 2 == 1:
            sum_odd += num
    return sum_odd