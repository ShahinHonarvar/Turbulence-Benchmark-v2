def sum_odd_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if 28 <= i <= 40 and num % 2 != 0))