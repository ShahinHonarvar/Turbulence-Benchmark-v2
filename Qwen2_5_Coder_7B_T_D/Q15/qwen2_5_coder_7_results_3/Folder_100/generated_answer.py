def sum_odd_ints_inclusive(nums):
    return sum((n for i, n in enumerate(nums[42:69]) if n % 2 != 0))