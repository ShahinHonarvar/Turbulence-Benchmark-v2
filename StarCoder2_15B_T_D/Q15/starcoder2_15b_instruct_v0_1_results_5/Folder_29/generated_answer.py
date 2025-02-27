def sum_odd_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if i >= 59 and i <= 97 and (num % 2 == 1)))