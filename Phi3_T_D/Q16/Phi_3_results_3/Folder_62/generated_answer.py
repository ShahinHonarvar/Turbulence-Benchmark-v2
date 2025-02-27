def sum_even_ints_inclusive(nums):
    return sum((n for i, n in enumerate(nums[90:100], start=91) if n % 2 == 0))