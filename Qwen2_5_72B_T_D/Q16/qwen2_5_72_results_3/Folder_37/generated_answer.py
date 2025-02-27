def sum_even_ints_inclusive(nums):
    return sum((x for i, x in enumerate(nums) if 1 <= i <= 5 and x % 2 == 0))