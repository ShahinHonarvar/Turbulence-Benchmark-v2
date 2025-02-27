def sum_odd_ints_inclusive(nums):
    return sum((x for i, x in enumerate(nums[30:38], start=30) if i <= 87 and x % 2 != 0))