def sum_even_ints_inclusive(nums):
    return sum((n for i, n in enumerate(nums[22:51]) if n % 2 == 0))