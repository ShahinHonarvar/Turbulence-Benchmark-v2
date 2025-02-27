def sum_odd_ints_inclusive(nums):
    return sum((x for i, x in enumerate(nums) if 90 <= i <= 200 and x % 2 != 0))