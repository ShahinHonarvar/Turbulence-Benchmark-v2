def sum_even_ints_inclusive(nums):
    return sum((n for n in nums[:4] if n % 2 == 0))