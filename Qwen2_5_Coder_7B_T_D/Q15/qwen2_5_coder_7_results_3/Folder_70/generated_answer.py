def sum_odd_ints_inclusive(nums):
    return sum((n for i, n in enumerate(nums[28:33]) if i % 2 == 0 and n % 2 != 0))