def sum_even_ints_inclusive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    for num in nums[0:3]:
        if num % 2 == 0:
            sum += num
    return sum