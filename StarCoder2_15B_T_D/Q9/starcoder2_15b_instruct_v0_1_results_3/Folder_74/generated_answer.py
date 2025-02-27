def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 17 and i <= 78 and (num % 2 == 1)]