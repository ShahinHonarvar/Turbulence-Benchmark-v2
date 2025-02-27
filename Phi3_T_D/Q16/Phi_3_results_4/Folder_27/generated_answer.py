def sum_even_ints_inclusive(nums):
    return sum((n for i, n in enumerate(nums[66:94], start=66) if n % 2 == 0))