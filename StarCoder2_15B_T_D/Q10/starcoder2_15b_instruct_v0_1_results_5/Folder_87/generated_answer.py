def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 32 and i < 99 and (num % 2 == 1)]