def sum_odd_ints_inclusive(nums):
    if not isinstance(nums, list):
        raise TypeError('Argument must be a list of integers.')
    total = 0
    for num in nums[56:58]:
        if num % 2 != 0:
            total += num
    return total