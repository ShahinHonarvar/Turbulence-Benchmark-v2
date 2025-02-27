def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 49 and i < 74 and (num % 2 == 1)]