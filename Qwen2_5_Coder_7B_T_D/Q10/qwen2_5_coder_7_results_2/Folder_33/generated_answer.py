def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i > 369 and i < 983 and (num % 2 != 0)]