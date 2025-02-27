def sum_odd_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if 10 <= i <= 100 and num % 2 != 0))