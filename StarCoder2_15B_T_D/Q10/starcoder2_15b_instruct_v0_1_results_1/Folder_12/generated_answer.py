def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 23 and i < 45 and (num % 2 == 1)]