def sum_odd_ints_inclusive(nums):
    return sum((x for i, x in enumerate(nums) if 10 <= i <= 100 and x % 2 != 0)) if len(nums) > 10 else 0