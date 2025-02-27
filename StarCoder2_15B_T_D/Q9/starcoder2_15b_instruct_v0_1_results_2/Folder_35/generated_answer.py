def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 30 and i <= 48 and (num % 2 == 1)]