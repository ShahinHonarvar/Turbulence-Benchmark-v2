def sum_even_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums, start=1) if i >= 15 and i <= 39 and (num % 2 == 0)))