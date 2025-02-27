def sum_even_ints_inclusive(nums):
    return sum((n for i, n in enumerate(nums[5:8]) if n % 2 == 0))