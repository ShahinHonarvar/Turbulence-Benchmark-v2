def sum_odd_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if i >= 37 and i <= 76 and (num % 2 == 1)))