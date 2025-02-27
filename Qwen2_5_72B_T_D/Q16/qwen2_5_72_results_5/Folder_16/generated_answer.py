def sum_even_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if 32 <= i <= 36 and num % 2 == 0))