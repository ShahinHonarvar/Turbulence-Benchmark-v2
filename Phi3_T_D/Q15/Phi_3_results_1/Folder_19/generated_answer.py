def sum_odd_ints_inclusive(nums):
    return sum((n for i, n in enumerate(nums[3:6], start=3) if n % 2 != 0))